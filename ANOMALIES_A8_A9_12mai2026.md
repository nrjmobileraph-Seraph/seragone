# ANOMALIES A8, A9 v1 et A10 — Document canonique

**Date de gravure** : 12 mai 2026 10:40 CEST
**Session** : audit Séragone post-refactor 23 avril, sondes G→M + O1
**Auteur** : session collaborative humain + assistant
**Hash money_manager.py final** : `f9b1580c94bbdf3245c1ac4629d2db85bb71485f175f1cd6733a409aeab0aa75`
**Hash state_registry.json v0.2** : `bcbff171f58bc2d88fac74f46610d5b19622b9c4f1a00eb6d0c20dfc445c59bf`

---

## Résumé exécutif

Trois anomalies découvertes et qualifiées lors de la session du 12 mai 2026 :

- **A8** — DoubleTempo vivant, gamma par design sur 4 couches comptables — **FERMÉE en constat** (pas de bug, design intentionnel à canoniser).
- **A9 v1** — 3 fichiers state fossiles synchrones du 22 avril 21:52 lus par money_manager.py — **FERMÉE en runtime** par 3 patchs garde-fou TTL 1h.
- **A10** — 15 fichiers state fossiles satellites (mtimes 19-27 avril) non lus par money_manager.py — **OUVERTE** pour audit consommateurs aval ultérieur.

---

## A8 — DoubleTempo gamma par design

### Constat

Le module DoubleTempo (`doubletempo.py`, vivant, écrit son state) applique 4 couches comptables au capital total 35 000 € :

- V9_PREMIUM = 8 750 €
- TIREURS = 19 250 €
- TEMPÉRANCE = 5 250 €
- RÉSERVE = 1 750 €

Ces 4 couches sont visibles dans chaque tick MM depuis 12 mai 08:27 UTC, ligne `Couches : V9=8750€ | Tireurs=19250€ | Tempérance=5250€ | Réserve=1750€`.

### Qualification

**Pas un bug.** C'est une gamma fonctionnelle par design. Le module DoubleTempo est actif, son fichier source est présent, son state est écrit régulièrement. L'apparente "asymétrie" entre couches est une décision doctrinale stable.

### Action

**Aucun patch nécessaire.** Le constat est gravé dans le présent document pour traçabilité, et le module est référencé dans `state_registry.json` (section `states_vivants`).

---

## A9 v1 — Fossiles toxiques M4/M5/Clones patchés

### Constat initial

Les 3 fichiers suivants étaient lus par `money_manager.py` à chaque tick mais n'étaient plus produits depuis 19+ jours (mtime 22 avril 21:52:11-12 UTC) :

| Fichier | Consommateur MM | Effet runtime AVANT patch |
|---|---|---|
| `states/ours_v2_state.json` | `load_m4_state` (ligne 445) | Injection `M4_Short SHORT mult=0.100 = 3500€` à chaque tick |
| `states/grappillage_state.json` | `load_m5_state` (ligne 457→461) | Inerte (taille_actuelle=0) mais lu |
| `clones_v6_state.json` | `load_clones_state` (ligne 437) | `WAIT, confiance=0.0` cohérent par hasard |

**Synchronicité des mtimes** : les 3 fossiles datent du 22 avril 21:52:11-12, à la même seconde → arrêt orchestré simultané, probablement lié à un refactor non documenté.

### Diagnostic

Aucun producteur actif pour ces 3 states depuis le 22 avril. Les scripts producteurs (`filtre_clones_v6.py` confirmé présent comme source) ne tournent plus. Le MM lisait des données fossiles comme si elles étaient fraîches.

### Solution appliquée — Garde-fou TTL 1h

Pour chacune des 3 fonctions `load_*_state` du `money_manager.py`, ajout d'un test de fraîcheur :

```python
if (time.time() - f.stat().st_mtime) > 3600:
    log.warning(f"<nom> state stale ({(time.time()-f.stat().st_mtime)/3600:.1f}h) -> inactif")
    return {...valeur synthétique inactive...}
```

### Application chirurgicale en 3 phases

| Phase | Fonction | Hash après | Validation runtime |
|---|---|---|---|
| 1/3 | `load_m4_state` | `c3d3618c...` | `M4 state stale (466.6h) -> inactif` à 08:25:02 UTC |
| 2/3 | `load_m5_state` | `7a2f93e7...` | `M5 state stale (466.6h) -> inactif` à 08:28:01 UTC |
| 3/3 | `load_clones_state` | `f9b1580c...` | `Clones state stale (466.6h) -> WAIT forcé` à 08:31:02 UTC |

**Hash original avant tout patch** : `4760b99c...` (20441 octets, 659 lignes).
**Hash final post-A9** : `f9b1580c...` (21106 octets, 669 lignes).
**Diff cumulé** : +10 lignes (1 `import time` + 9 lignes garde-fou réparties en 3 blocs de 3).

### Backups conservés

money_manager.py.pre_A9_patch_20260512_082346.bak (20441 o, original)
money_manager.py.pre_A9_patch_1778574247.bak (20441 o, doublon Python)
money_manager.py.pre_A9_M5_patch_1778574474.bak (20671 o, après M4)
money_manager.py.pre_A9_Clones_patch_1778574655.bak (20889 o, après M4+M5)

text

Rollback complet possible vers n'importe quel état intermédiaire.

### Effet runtime confirmé

- Disparition des injections fossiles `M4_Short SHORT mult=0.100 = 3500€` après 08:24:02 UTC.
- Apparition de 3 warnings par minute : `M4/M5/Clones state stale (XXX.Xh) -> inactif/WAIT forcé`.
- `Tireurs actifs : 0` (au lieu de 1+ avec M4 fossile).
- Service `seragone-brain.service` stable, aucune exception, sémantique aval préservée (`Clones V6 : WAIT` continue d'apparaître identiquement).

### Statut A9 v1

**FERMÉE en runtime.** Le périmètre est strictement borné aux 3 fossiles consommés par MM. Les producteurs absents ne sont pas restaurés (décision doctrinale ouverte) — le garde-fou TTL absorbe l'absence proprement.

---

## A10 — 15 fossiles satellites à investiguer

### ⚠ RÉSOLUTION 12 mai 11:09 UTC — ORPHELINS-INERTES confirmés

Sonde ρ-3 a prouvé mécaniquement :
- Seul `money_manager.py` racine (hash `f9b1580c`, patché A9 v1) est exécuté par cron (`* * * * *`)
- Les 2 autres "money managers" du repo (`money_manager_perplexity_97L.py`, `production/allocation/money_manager.py`) ont mtime 22-23 avril → fossiles A9 eux-mêmes, jamais exécutés
- Les ~13 consommateurs Python de fossiles A10 (m7_micro, m1_long, gardien_silencieux, detecteur_derives, etc.) sont **tous orphelins** : ni cron, ni service systemd, ni processus actif
- Services Séragone runtime actifs = `seragone-brisance.service` + `seragone-securite.service` uniquement → disjoints du périmètre A10

**Aucun patch runtime nécessaire.** A10 fermée comme dette doctrinale d'hygiène (archiver ultérieurement les 13 scripts orphelins). Le mode démo n'est pas compromis.

### Constat initial (préservé)



### Constat

La sonde exhaustive O1 du 12 mai 2026 10:37 UTC (commande `find ~/seragone -name "*_state.json"`) a révélé 15 fichiers state supplémentaires avec mtimes anciens (19 avril → 27 avril) que je n'avais pas détectés lors de mes sondes dirigées initiales.

### Liste exhaustive

| Fichier | mtime | Taille | Lu par MM ? |
|---|---|---|---|
| `m7_state.json` | 2026-04-22 21:52:11 | 210 o | NON |
| `moteurs/m8_tresorerie_state.json` | 2026-04-22 21:17:27 | 373 o | NON |
| `moteurs/m3_temperance_state.json` | 2026-04-22 21:17:27 | 278 o | NON |
| `m3_temperance_state.json` (racine) | 2026-04-22 15:51:17 | 278 o | NON |
| `mondes_long_state.json` | 2026-04-22 20:09:06 | 88 o | NON |
| `tireur_pulse_state.json` | 2026-04-21 20:21:28 | 179 o | NON |
| `bulletin_decision_state.json` | 2026-04-25 09:00:02 | 728 o | NON |
| `gardien_silencieux_state.json` | 2026-04-24 06:34:59 | 230 o | NON |
| `states/allocation_state.json` | 2026-04-23 13:07:46 | 1073 o | NON |
| `states/ricochet_state.json` | 2026-04-23 13:07:46 | 102 o | NON |
| `states/regime_state.json` | 2026-04-23 13:07:46 | 58 o | NON |
| `states/capital_state.json` | 2026-04-23 11:25:41 | 74 o | NON |
| `derives_state.json` | 2026-04-27 15:49:39 | 604 o | NON |
| `q_local_p10_state.json` | 2026-04-19 03:49:55 | 239 o | NON |
| `states/freshness_state.json` | 2026-04-27 18:56:00 | 41674 o | NON (ironique : était supposé être le watchdog) |

### Diagnostic provisoire

**Aucun des 15 satellites n'est lu par `money_manager.py`** (pré-classification du 12 mai 10:39 UTC). Le risque "injection toxique fossile via MM" est circonscrit à A9 v1 déjà patchée.

**Inconnues à investiguer dans une session A10 ultérieure** :
1. Quels autres composants vivants (sniper, brisance, sentinelle, mondes_paralleles, etc.) lisent ces 15 fossiles ?
2. Y a-t-il des chaînes d'injection indirecte (X lit fossile → écrit Y vivant → MM lit Y) ?
3. Lesquels sont des artefacts de modules supprimés (à archiver/supprimer) vs des modules suspendus (à réactiver) ?

### Statut A10

**OUVERTE explicitement.** Aucune action runtime cette session. À investiguer par sonde dirigée consommateurs aval.

---

## Méta-leçon — Sonde exhaustive AVANT sonde dirigée

### Faute méthodologique reconnue

Lors des tours 4-17 de la session, j'ai sondé en mode **dirigé** (grep ciblé sur les 3 fossiles M4/M5/Clones supposés) au lieu de mode **exhaustif** (lister TOUS les states, classifier par mtime). Le mode dirigé confirme l'hypothèse mais ne peut pas révéler ce qui est hors hypothèse. Conséquence : 15 fossiles A10 sont restés invisibles 17 tours durant.

### Règle canonique

> **Toute enquête sur un sous-système Séragone doit commencer par une sonde exhaustive non filtrée, puis classification, puis sonde dirigée — jamais l'inverse.**

Pour les `*_state.json` spécifiquement :

```bash
find ~/seragone -maxdepth 4 -name "*_state.json" -type f 2>/dev/null \
  | grep -vE "\.venv|__pycache__|/archive|/backups|AUDIT_CHRONO|_freeze_" \
  | xargs -I{} stat -c "%y  %10s o  %n" {} | sort -r
```

À rejouer mensuellement (cron 1er du mois) pour détecter dérive.

---

## Doctrine des 5 Portes — pour tout nouveau monde / moteur / pépite

Tout nouvel artefact computationnel introduit dans Séragone doit passer 5 portes obligatoires avant déploiement :

| Porte | Question | Mécanisme |
|---|---|---|
| 1 — Identité | Nom canonique, emplacement code, emplacement state ? | Contract en tête fichier `.py` |
| 2 — Production | Quels states écrit-il, fréquence, TTL ? | Entrée `producer` dans `state_registry.json` |
| 3 — Consommation | Quels states lit-il, garde-fou de fraîcheur ? | Entrée `consumer` + check `time.time() - mtime` obligatoire |
| 4 — Câblage | Lancé par cron, systemd, ou orchestrateur ? Vérifiable comment ? | Script `verif_cablage.py` croisant registre + crontab + systemctl |
| 5 — Mort propre | Si on le supprime, qu'arrive-t-il aux consommateurs aval ? | Procédure migration documentée dans `BATTERIES_SONDES_FROIDES` |

### Origine de la règle

A9 est exactement la classe d'erreur que les Portes 4 et 5 auraient empêchée : un producteur est mort le 22 avril sans procédure de Porte 5, et personne ne s'en est rendu compte pendant 20 jours parce qu'aucune Porte 4 n'auditait le câblage runtime.

---

## Procédure canonique de patch chirurgical

Toute modification d'un fichier de production doit suivre 6 étapes obligatoires :

1. **Backup horodaté** : `cp fichier.py fichier.py.pre_<anomalie>_patch_<timestamp>.bak`
2. **Inventaire exact des zones à modifier** : `grep -nE "<pattern>" fichier.py` doit retourner un compte précis attendu
3. **Snapshot état avant** : `sha256sum`, `wc -l`, `stat`, `tail -N logs/<service>.log`
4. **Édition canonique** : jamais coller du Python dans bash. Toujours via heredoc dans un script `.py` qui lit/réécrit le fichier avec contrôle `if old_block not in code: raise SystemExit("ABORT")`
5. **Validation 5 axes** : syntaxe (`py_compile`) + taille + diff (`diff backup actuel`) + fonction modifiée (`sed -n`) + dépendance (`grep "import time"`)
6. **Observation runtime** : `sleep 70` puis `grep <signature_attendue> logs/<service>.log`

Si une étape échoue, **rollback immédiat** : `cp backup fichier.py && systemctl restart <service>`.

---

## A12-bis — Faux positif du registre v0.2 (corrigé v0.3)

### Constat

Lors du premier dry-run de `state_freshness_watchdog.py` (v0.1, mon outil) sur le registre v0.2, deux states ont été signalés `HIGH stale` :

- `tireurs_state.json` : 23.9h depuis dernier write (mtime 11 mai 08:50)
- `multivers_state.json` : 12.3 min depuis dernier write

J'ai initialement diagnostiqué A12 comme une "A9-bis" — fossile toxique en attente d'injection. J'ai proposé un patch garde-fou TTL côté money_manager.py ligne 523 (`load_autonomes`).

### Sondes A12-ter et A12-quater

- A12-ter a montré que `journees_des_tireurs_v2.py` est producteur unique, présent en code, mais absent du crontab ubuntu.
- A12-ter a confirmé un cycle quasi-quotidien (86158s ≈ 86400s, écart 0.28%).
- A12-quater a révélé l'existence d'un `watchdog_seragone.py` natif Seragone, lancé par cron `*/10 * * * *`, qui surveille 11 states avec TTL en **MINUTES**.
- Le natif déclare `tireurs_state.json: 1500` minutes (= 25 heures) avec garde-fou horaire `if now.hour < 9: log normal`.
- Dernier verdict natif : `2026-05-12T08:40:01Z — daemons_ok 6/6 — states_ok 11/11 — status SAIN — alerts: []`.

### Diagnostic réel

**Aucune anomalie runtime.** Le cycle quotidien à 08:50 UTC est par design. Mon registre v0.2 avait déclaré `ttl_seconds: 120` pour `tireurs_state.json` et `mondes_paralleles_state.json` alors que le natif les tolère jusqu'à 1500 min. **C'était une erreur de calibration de ma part**, pas une vraie anomalie.

De plus, le code `money_manager.py` ligne 523-540 possède déjà un **garde-fou sémantique** : `if _auto_dir == "SHORT"`. Le fossile actuel dit `direction_nette: NEUTRE`, donc aucune injection n'a lieu, même sans patch TTL.

### Action corrective

- Registre `state_registry.json` v0.2 → v0.3 : TTL alignés sur `STATES_CHECK` natif.
- Re-run `state_freshness_watchdog.py` post-v0.3 : **code retour 0** = système sain.
- **Aucun patch runtime appliqué** (M4/M5/Clones de A9 v1 restent les seuls patchs runtime de la session).

### Faute reconnue — méta-leçon

J'allais introduire un patch garde-fou TTL 5 min côté `load_autonomes`, ce qui aurait :
- Désactivé la couche Tireurs (19 250 €) tous les jours entre 08:55 et le lendemain 08:50 (faux positif chronique).
- Doublonné le rôle du `watchdog_seragone.py` natif que je n'avais pas vu.

**La règle dérivée** : avant de patcher ou créer, sonder l'existant. Cette règle devient la **Porte 0** de la doctrine 5 Portes.

### Statut

**FERMÉE** comme faux positif. Le registre v0.3 et le natif sont désormais alignés.

---

## Porte 0 — Sonder l'existant avant créer (méta-leçon élevée)

Ajout à la doctrine des Portes (originellement 5, désormais 6 avec Porte 0 en préalable).

### Énoncé

> Avant de créer un nouveau composant (script, watchdog, registre, doc), exécuter une sonde exhaustive sur le concept dans le dépôt existant. `grep -rln "<concept_clé>" ~/seragone/*.py` puis lire les fichiers hits.

### Origine empirique

Session du 12 mai 2026 : création de `state_freshness_watchdog.py` à 10:42 UTC sans avoir lu `watchdog_seragone.py` natif (présent depuis longtemps, déjà cron`*/10`, fonctionnel et SAIN). Le natif est apparu dans une sonde O2 antérieure mais n'a pas été grepé.

Conséquence évitée de justesse : doublon de rôle, calibration erronée, faux diagnostic A12.

### Procédure canonique Porte 0

Avant toute création de composant nouveau, exécuter :

```bash
CONCEPT="<mot_clef>"
echo "=== Code Python existant sur ce concept ==="
grep -rln "$CONCEPT" ~/seragone/*.py 2>/dev/null
echo "=== Crontab ==="
crontab -l 2>/dev/null | grep -i "$CONCEPT"
echo "=== Services systemd ==="
systemctl list-units --type=service 2>/dev/null | grep -i "$CONCEPT"
echo "=== Timers systemd ==="
systemctl list-timers --all 2>/dev/null | grep -i "$CONCEPT"
echo "=== Docs Markdown ==="
grep -rln "$CONCEPT" ~/seragone/*.md 2>/dev/null
```

Si la sonde retourne du contenu, **lire avant créer**. Si zéro résultat, alors créer.

### Place dans le canon

Porte 0 (préalable) → Porte 1 Identité → Porte 2 Production → Porte 3 Consommation → Porte 4 Câblage → Porte 5 Mort propre.

---

## A14 — Pépites P20-P51 orphelines (dette doctrinale d'inachèvement)

### Constats mécaniques (sonde Dette3 du 12 mai 10:56 UTC)

- 32 scripts `moteur_pepite_{20..51}_*.py` présents à la racine `~/seragone/`
- 0 script `moteur_pepite_{20..51}_*.py` dans `~/seragone/production/pepites/`
- Crontab actuel couvre P1-P19 uniquement (P1-P5 racine, P6-P19 dans `production/pepites/`)
- **Zéro consommateur Python** des states `pepite{20..51}_*_state.json` (grep -rln exhaustif négatif)
- States `pepite{20..51}_*_state.json` : mtime synchrone 4 mai 2026 09:10-09:41 UTC (~8 jours)
- 10 backups crontab disponibles entre 5 et 11 mai dans `~/seragone/backups_crontab/` et `~/seragone/backup_crontab_*.txt`

### Diagnostic mécanique

**Dette doctrinale d'inachèvement**, pas anomalie runtime. La migration vers `production/pepites/` (cf. commentaire crontab `26 avril 2026`) a couvert P1-P19 et s'est arrêtée avant P20-P51.

**Risque toxique** : NUL — zéro consommateur, donc aucune injection possible.

**Risque opérationnel** : MEDIUM — 32 observatoires arrêtés depuis 8 jours, les données qu'ils produisaient (returns 30d, range milieu, fg haut, etc.) ne sont plus à jour. Si une future stratégie veut les ré-exploiter, il faudra restaurer le cron ET re-tester les scripts.

### Décision arborescente (à trancher session A14 future)

| Option | Action | Conséquence |
|---|---|---|
| Restaurer cron P20-P51 | Ajouter 32 lignes crontab `04:8 → 35:9 * * *` | Reprise production observatoire complète |
| Migrer P20-P51 vers `production/pepites/` | Déplacer + crontab + tester | Architecture cohérente avec P6-P19 |
| Archiver P20-P51 | Déplacer scripts + states vers `_bibliotheque_modules/archive_2026_05_12_pepites_P20_P51/` | Suppression propre, traçable |
| Statu quo | Ne rien faire | Dette persiste, scripts orphelins en racine |

### Sondes d'ouverture session A14

```bash
# A14.1 — Quand exactement P20-P51 ont-ils été retirés du crontab ?
diff <(crontab -l) ~/seragone/backups_crontab/crontab_pre_fix_SERAGONE_20260511T205101Z.txt | grep -iE "pepite[2-5]"

# A14.2 — Commit git de retrait (si crontab versionné)
cd ~/seragone && git log -S "moteur_pepite_20" --oneline --all | head -10

# A14.3 — Quel commit a introduit production/pepites/ pour P6-P19 ?
cd ~/seragone && git log -S "production/pepites/moteur_pepite_6" --oneline --all | head -5
```

### Statut

**OUVERTE comme dette doctrinale.** Aucune action runtime urgente. Décision à trancher en session A14 dédiée, idéalement après audit A10 (Dette 1) pour cohérence d'ensemble.

---

## Annexe — Inventaire condensé state_registry.json v0.2

- **11 states vivants** (mtime <1h) — MM, tireurs, brisance, sentinelle, securite, sniper, mondes_paralleles, multivers, chronometer, observer_price_live, policy
- **3 fossiles A9 v1 patchés** — ours_v2, grappillage, clones_v6
- **15 fossiles A10 satellites ouverts** — voir tableau ci-dessus
- **5 pépites cron quotidien actives** (pepite14-17 + pepite1 référence)
- **32 pépites dormantes** (pepite20-51, mtime 4 mai)
- **Hors périmètre** : `_bibliotheque_modules/production_copies/` (archive référence) et `audit/*/` (snapshots horodatés)

---

## Fin du document canonique

Date de gravure : 12 mai 2026 10:40 CEST.
Document à compléter dans la session ouverture A10 (date à définir).


---

## Dette 2 (post-ACTE 30) — FAUX PROBLÈME confirmé

**Date** : 12 mai 2026 11:14 CEST
**Méthode** : Sonde Porte 0 sur `state_freshness_watchdog.py`

**Résultat** :
- Logique exit_code ligne 114-116 correcte : `high_stale` exclut `ABSORBED_BY_PATCH`
- Run réel : exit code 0, 0 HIGH stale non absorbé / 36 vérifiés
- Registre v0.4 cohérent : A10_resolution=ORPHELINS_INERTES_CONFIRMES, porte5_natif_trous (2H+5M) présents

**Verdict** : Dette 2 = faux problème mémoire, comme A12-bis.

**Méta-leçon (4e) confirmée** : Porte 0 s'applique aussi aux propres outils. Toute "dette" doit être sondée avant d'être patchée.

---

## A14 (post-ACTE 30) — FAUX PROBLÈME confirmé

**Date** : 12 mai 2026 11:18 CEST
**Méthode** : Sonde Porte 0 lecture documents canon (10 .md identifiés)

**Découvertes mécaniques** :
- 5 pépites Tier 1 (P1-P5) validées walk-forward, ACTIVES en crontab via `pepites_tier1_adapter.py`
- 14 pépites P6-P19 ACTIVES en crontab via `production/pepites/`
- 3 pépites propres Phase 18 actives en watchlist shadow
- Document maître `DECISION_PERCEPTION_REPERTOIRE_4_STATUTS_2026-05-11.md` : statut canonique fermé "AUCUN fichier à supprimer/renommer aujourd'hui"
- `village_adapter.py` orphelin runtime mais DECRET_B4 = préservation intacte
- Pipeline démo A6/A7 OPÉRATIONNEL en production (3 cron `* * * * *` actifs depuis 10 mai)

**Verdict** : A14 = faux problème mémoire. Le canon est déjà clair sur tous les périmètres invoqués.

**Méta-leçon (5e) gravée** : Quand la mémoire dérive sur le périmètre d'une anomalie, ne pas patcher selon la mémoire — relire le document source canonique. 3 fausses alarmes consécutives dans cette session (A12-bis, Dette 2, A14) confirment la nécessité absolue de Porte 0 préalable.

---

## Post-patch A10 (12 mai 11:21 CEST) — ROLLBACK + Méta-leçon 6

**Incident mécanique** : ma sonde Porte 0 a interrogé `A10_resolution.get('date_resolution')` qui retournait `None`, faisant croire à un squelette. Réalité : `A10_resolution` contenait déjà 8 clés bien documentées (résolution ρ-3 du 11:09 UTC) sous d'autres noms (`date`, `sonde_preuve`, `verdict`, etc.). Mon patch a ajouté 10 clés par-dessus, créant une redondance documentaire (18 clés au total dont 6 dupliquées sémantiquement).

**Action** : rollback via backup `state_registry.json.bak_pre_A10_complete_12mai_1120`. Retour aux 8 clés originales ρ-3.

**Méta-leçon (6e) gravée** : Sonde Porte 0 sur JSON doit énumérer TOUTES les clés présentes (`for k in dict.keys()`), pas interroger seulement les noms supposés via `.get()`. Sinon faux verdict "section vide".

**Bilan session — 4 fausses alarmes confirmées** : A12-bis, Dette 2, A14, A10-squelettique. Toutes résolues par Porte 0 et/ou rollback. Aucun runtime touché à tort.

---

## Dette 1 (post-ACTE 31, 12 mai 11:33 CEST) — COMPORTEMENT NOMINAL confirmé

**Méthode** : Sonde Porte 0 L.6 → L.11 (verbose -u, run manuel, lecture statedemo)

**Découvertes** :
- Les 3 scripts démo cron sont conçus SILENCIEUX (anti-flood doctrinal ATTESTATION_A7)
- Run manuel verbose `-u` : exit 0, 0 output stdout/stderr
- `statedemo.json` contient triple trace canonique fraîche 08:52→08:54 UTC :
  * Decision : auto_a7_position_nette_short
  * Order : AUTO_A7_20260512T085201 SHORT 0.001 BTC-USDT @ 80940.01
  * Prudence : PASS checked
  * Execution : DEMO_EXEC_7a7cb2e60f94 FILLED_DEMO
- Pipeline 4 maillons opérationnel : Decision→Generator→Prudence→Broker en 121s
- Cron 3 jobs `* * * * *` actifs (cron.service depuis 1m25j, ACTIVE)
- Idempotence : tant que decision metier ne change pas, scripts exit early sans réécrire state

**Verdict** : Dette 1 = 6e fausse alarme. Comportement nominal idempotent.

**Méta-leçon (7e) gravée** : Pour pipeline idempotent anti-flood, ne pas mesurer vivacité par mtime fichiers. Lire le timestamp interne du state, qui révèle dernière exécution réelle indépendamment du mtime.

**5 limites V1 mécaniquement observables dans statedemo.json** (préparation Mode démo V2) :
1. symbol "BTC-USDT" hardcoded
2. quantity 0.001 constante
3. side direct (SHORT actuellement)
4. pnl_demo 0.0 + cash_after_demo null (absent)
5. Pas de champ reconciliation

---

## Dette 2 (post-ACTE 31, 12 mai 11:35 CEST) — FERMÉE source identifiée

**Méthode** : Sonde D2.1 → D2.7 (systemd, cron, ps, grep writers)

**Découvertes** :
- `watchdog_state.json` mis à jour toutes les 10 min, mtime 09:30 UTC (4 min avant sonde)
- Source : cron `*/10 * * * * cd /home/ubuntu/seragone && python3 watchdog_seragone.py >> logs/watchdog.log 2>&1`
- 11 services systemd `seragone-*` actifs (brain, brisance, api, sentinelle, securite, paralleles timer, multivers timer, 1min, mondes-oneshot, etc.)
- **PAS** de service systemd nommé `watchdog_seragone` (par design : c'est un cron)
- `chef_dependency_manifest.py` ligne 99 : `"watchdog_state.json": "watchdog"` = simple clé de dict registre, PAS un writer
- **Doctrine 9 RESPECTÉE** : 1 seul writer (`watchdog_seragone.py`), 1 manifeste documentaire

**Verdict** : Dette 2 = 7e fausse alarme. Comportement nominal cron. Pas de service systemd attendu.

**Méta-leçon (8e) gravée** : Un nom de state dans un fichier `manifest`/`registry` n'implique pas un writer. Vérifier le contexte (clé de dict vs `open()` write) avant de crier violation Doctrine 9.

**Registre canonique enrichi** :
- `watchdog_state.json` → writer = `watchdog_seragone.py` (cron `*/10`)
- À ajouter dans `state_registry.json` section writers si pas encore présent

---

## Dette 3 (post-ACTE 31, 12 mai 11:38 CEST) — DÉCISION OPPOSABLE confirmée

**Méthode** : Sonde D3.1 → D3.6 (find, grep, lecture canonique 2 docs perception)

**Découvertes** :
- 2 documents de décision gravés 11 mai dans `audit/decisions/` :
  1. `DECISION_PERCEPTION_REPERTOIRE_4_STATUTS_2026-05-11.md` (20260511T064740Z)
  2. `DECISION_NC_ENGINE_PERCEPTION_DEPRECATED_2026-05-11.md` (20260511T064347Z)
- 8 fichiers `production/perception/` tous STATUÉS :
  * STATUT A (5 fichiers orphelins chambre travail) : convergence.py, dimensions.py, range_engine.py, state_vector.py, strategie_range_complete.py
  * STATUT B (1 fork expansif expérimental) : ricochet_regimes.py
  * STATUT C (1 duplication cross-dossier volontaire) : vrais_yeux_stretched.py (perception + mondes byte-identique)
  * STATUT D (1 fork régression neutralisé) : nc_engine.py.DEPRECATED_FORK_REGRESSION_2026-05-11
- 0 référence "perception" dans `state_registry.json` (cohérent : orphelin canonique)
- 0 process Python actif touche `production/perception/`
- 0 entrée "perception" dans `canon/INDEX_CANON_SERAGONE.md` (mini-trou doctrinal, à graver session future)

**Action canonique 12 mai** : AUCUNE (décision 11 mai opposable, conforme directive minimaliste session).

**Verdict** : Dette 3 = 8e fausse alarme. Décision déjà gravée hier dans `audit/decisions/`. Ma recherche initiale à la racine était trop étroite.

**Méta-leçon (9e) gravée** : Avant de crier "doc introuvable", chercher dans `audit/decisions/` ET sous-arbres. Les décisions canoniques de Séragone vivent dans cette arborescence, pas systématiquement à la racine.

**Mini-dette future détectée (non bloquante)** :
- `canon/INDEX_CANON_SERAGONE.md` n'indexe pas les 2 décisions perception/
- À graver en session dédiée "indexation des décisions audit/decisions/"

---

## Dette 4 (post-ACTE 31, 12 mai 12:00 CEST) — FERMÉE à 80% (hygiène git massive)

**Méthode** : Phases P1 → P3 mécaniques (archive externe + rm + .gitignore durci)

### P1+P2 — Archive externe + rm AUDIT_CHRONO (9 Go libérés)
- Archive `~/external_archives/AUDIT_CHRONO_20260501_archive_20260512T094723Z.tar.gz` (4.4 Go, 5603 fichiers)
- sha256 archive : `0cc0052cae17da76bc06dd4049458f2bc7d848912f1eba0e1561117d062a6548`
- Sources supprimées : AUDIT_CHRONO_SERAGONE_TOTAL_20260501_101502/ (6.8 Go), _PARTS/ (2.3 Go), _LITE/ (1.5 Mo)
- 2 tar.gz originaux 1er mai déplacés vers external_archives (cleanup racine)
- Manifest joint pour récupération future
- Hash global ACTE 28 (`63cb850ff28f7469`) reste preuve canonique

### P3 — .gitignore durci (54 → 187 lignes)
- Backup : `.gitignore.backup_pre_dette4_20260512T095831Z`
- sha256 nouveau : `2935769e83c4d4f38435ad18fdf5c0d2013a7487a24a2e70ec3eef511e9e10e3`
- Patterns ajoutés : backups horodatés, audits éphémères, DEMO logs lourds, PEPITES chambre travail, scripts 0[0-9]_*, déchets crash shell, etc.
- Exception canonique préservée : audit/decisions/, audit/rapports/, audit/meta/, audit/packs/

### Métriques avant/après
- Fichiers `??` git : 1316 → **846** (-36%, -470 fichiers)
- Fichiers `M` git : 38 → 40 (runtime tick normal)
- Disque used : 63% → **51%** (-9 Go)
- Seragone repo : 22 Go → **13 Go**

### Architecture remote révélée (diagnostic divergence)
- `origin/main` = canal "auto" (cron `* * * * * /tmp/push_bulletin.sh`, 7375 commits "auto")
- `origin/canon` = canal canonique humain (dernier = ACTE 28 `413385cc` du 11 mai)
- Local main = 13 commits ACTE 19-31 humains
- ACTE 32 → push sur `origin/canon` (canal canonique cohérent)

### Mini-dettes futures (non bloquantes)
1. Raffinement `.gitignore` v2 pour passer de 846 → <100 fichiers `??` (session dédiée)
2. Tri humain racine seragone : 483 `.py`, 108 `.json`, 50 docs canoniques à committer/ranger
3. Indexation `audit/decisions/` dans `canon/INDEX_CANON_SERAGONE.md` (Dette 3 résiduelle)
4. Bug pattern .gitignore : `.candidat` / `.validated` non happés (probable guillemet/espace)

**Verdict** : Dette 4 = FERMÉE à 80%. Action mécanique majeure réussie. 9 Go libérés, hygiène git nettement améliorée.

**Méta-leçon (10e) gravée** : Pour un repo avec divergence remote (canal auto + canal humain), pousser ACTE doctrinal sur le canal canonique (`origin/canon`), pas sur `origin/main`. Évite conflits massifs avec bot.
