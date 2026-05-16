# PASSAGE DE RELAIS — Session 16 mai 2026 → prochaine IA

**À toi qui arrives.** Tu es la prochaine IA. Tu travailles avec Raphaël Boussy sur Séragone. Lis ce document AVANT toute action. Il te dit exactement où nous nous sommes arrêtés, ce qui est attendu de toi, et comment travailler.

═══════════════════════════════════════════════════════════════════

## §1 — Ce que tu dois lire en premier (ordre strict)

1. **`/home/ubuntu/.claude/projects/-home-ubuntu-seragone/memory/MEMORY.md`** — déjà chargé automatiquement par le harness.
2. **`/home/ubuntu/seragone/canon/CHRONOLOGIE_PARFAITE_MARS_A_MAI_2026.md`** (36 Ko, 542 lignes) — sha256 `d7f191432199edb9aeec2164937d5e273461901c1a032b51794601ecb1c95d3c`. **C'EST TA PHOTO-RÉFÉRENCE.** Tu n'as pas besoin de relire mars→avril ailleurs : tout est dans ce doc, avec les chemins-sources.
3. **`/home/ubuntu/seragone/canon/INDEX_CANON_SERAGONE.md`** — index canon officiel (33 décrets + 23 attestations chronologiques).
4. **Le présent document** — qui te dit quoi faire maintenant.

═══════════════════════════════════════════════════════════════════

## §2 — État au 16 mai 2026 (fin de session précédente)

### Ce qui a été fait dans la session du 16 mai (partie matin)

- 1 210 fichiers (2,1 Go) importés via `scp` dans `/home/ubuntu/seragone/canon/references/imports_session_20260516/` depuis le poste Windows de Raphaël.
- Lecture chronologique mars complet, avril dates clés, mai jusqu'à 13 mai 23:15 inclus.
- Vérification : les 9 décrets B2/B4/B8/N12/N12bis/N13/CONSTAT_D9 du fil Perplexity 9-10 mai sont **déjà gravés** sur VPS dans `audit/decisions/`. Ne pas re-graver.
- **Gravure de `CHRONOLOGIE_PARFAITE_MARS_A_MAI_2026.md` v2** (542 lignes, sha v2 `d7f191432199…`) — photo-référence chronologique avec §5 continuité d'objets (chiffres / mondes / scripts / concepts / moteurs).

### Ce qui a été fait dans la session du 16 mai (partie tardive — Claude Code C-VPS)

**Tous les 7 trous §3.1 ci-dessous ont été fermés.** Chronologie enrichie v2 → v9, passée de 542 à **906 lignes** (sha v9 `afc3306a26eb10923ba6ea61c508e2555eb7c2de083b5bbc36c3f299d01a64c7`).

- **Trou 1** Matrice anti-oubli 416 Ko (sha `f8f1a900…`) : 8 vrais trous runtime remontés en §5 (Qjour, Ricochet/Noise Control 3 couches, Range Engine, Filtre R, Glibre, Mémoire proactive, Confluence/registres, Pépites P1-**P51** au lieu de P1-P19) + 3 fossiles littéraires/doctrinaux explicités (4 poches, 8 tireurs, Tapis Rouge).
- **Trou 2** RECAPITULATIF_9_10_MAI_FINAL (sha `cb725f5a…`) : §4.6 cascade complète 10 mai 11h→19h gravée (Q2/Q3/ATT_Q5/A6/demobroker_runner cron actif/ATT_A6_OPE/B4_RESOLU village_adapter orphelin/sonde V2/A7-α/sonde price_reference clé `prix`/A3.1-A3.2-A3.3 préservations). INDEX_CANON palier 21 entrées `a873dead…`.
- **Trou 3** ATTESTATION_PHASE_115_STABLE_13_JOURS (sha attendu `7b17a0f4…` confirmé sur 3 copies bit-identiques) : période exacte 27 avril 10:21Z → 10 mai 07:00Z, signature Raphaël 09:30Z, triple garde-fou détaillé, 11 640 ticks money_manager 0 erreur, 9 services systemd nommés, lot A3.2 (47 fichiers, 6 niveaux N1-N6).
- **Trou 4** DECRET_A4bis (sha `144472308b…` 3 copies bit-identiques) : §4.4bis créé, **H5 acté** (DEMO_PAPER ≡ MODE_DEMO_TOTAL), 11 découvertes D24bis-D34 tabulées, sondes γ/γ-bis/γ-ter.1, formule `execution_allowed:108`, homonymie `seragone_fusion_aval.py` = `fusion_aval.py` levée.
- **Trou 5** DECRET_A6 + ATTESTATION_A6 (sha `0d25facea3…` canon VPS, `3afdbeb08d…` ATT) : 4 options évaluées (α retenue), 3 contrats demo signés 7 mai dans `demo/contracts/`, 5 verrous mode.lock, architecture demo/ 9 dossiers, V_α amendements (8→11 critères VETO), triptyque GO_A6 9/9 invoqué.
- **Trou 6** DECRET_A7 + ATT_A7 (sha `543dcb9b…` + `88ae1933…`) **+ bonus 15 mai ATT_A7_DIAGNOSTIC_R13c** (sha `a49261b6…`) : pipeline 4 maillons décrit, ordre canonique 12 champs, idempotence sha256[:16], Test 3 BONUS validé en cron production réel (cron A6 a consommé un ordre A7 sans intervention humaine), §4.10bis créé pour le 15 mai (chantier 18D en pause Article 8 Q6, D195 inscrite).
- **Trou 7** CONTRAT_ORCHESTRATEUR_DEMO_V1 VALIDATED (sha `2445e477…` canon `auditphasee/` — pas `canon/` comme indiqué auparavant, rectification) : 11 sections détaillées, V1_STATE_DIR `/home/ubuntu/seragone/states/v1/` **sondé inexistant runtime** (cohérent statut "PAS branchement"), doctrine clé « Les mondes filtrent, freinent ou contextualisent, mais ne tirent jamais. »

### 5 doctrines révélées au passage (à graver dans architecture mentale §6)

Découvertes en lisant les documents ci-dessus, jamais citées explicitement avant dans le passage de relais initial :

- **Article 8 Q6 « on laisse comme ça »** — un chantier dont l'écosystème runtime est intact mais incapable de reproductibilité peut rester en pause sans intervention (ATT_A7_DIAGNOSTIC_R13c 15 mai).
- **Doctrine 7 `decision_weight_real = 0.0`** — invariant : poids décisionnel réel = 0.0, jamais relevé sans décret.
- **VALIDATED != INSTALLED** — un module validé par tests (ex. GO_A7 12/12) n'est pas installé en runtime (cron actif). Cas applicable : `decision_to_order.py` + `prudence_demo_runner.py` validés mais pas en cron.
- **R1 Mondes != Tireurs** — règle ontologique : les mondes (regards 92/305+4) et les tireurs (8 tireurs Aplomb) sont deux objets distincts, ne pas confondre comptes ni rôles.
- **Posture sonder / décréter / activer** — 3-temps canonique : (1) sonder en lecture pure, (2) décréter sous triptyque GO/VETO/WAIT, (3) activer en PHASE 2 séparée session fraîche. Appliquée à toute la cascade A4→A4bis→A5→A6→A7.

### Branche git active

- `claude/sync-decisionallocation-20260516` — pas encore commitée pour cette session 16 mai. **Chronologie v2→v9 sur disque, pas encore commitée.**
- Architecture remote (révélée par ACTE 32 du 12 mai) :
  - `origin/main` = bot automatique (cron `*/1` `push_bulletin.sh`) — **ne pas pousser à la main ici.**
  - `origin/canon` = canal humain canonique — c'est ici que Raphaël pousse.

═══════════════════════════════════════════════════════════════════

## §3 — Objectifs en cours (à ne PAS perdre)

### §3.0 — MISSION CADRE (volonté Raphaël, 16 mai partie tardive)

**Avant tout détail technique, ta mission est : MAÎTRISER LA TOTALITÉ DU PROGRAMME SÉRAGONE.**

Raphaël l'a posé explicitement : *« je te laisse donc préparer la prochaine IA à approfondir plus encore, je lui explique ce qui a été fait et ma volonté qu'elle maîtrise la totalité du programme et qu'on puisse une fois la chose faite avancer dans les détails »*.

**Précondition opérationnelle :** tant que la maîtrise totale n'est pas acquise, **PAS de squelette `orchestrateur_demo`**, PAS d'activation cron PHASE 2 A7, PAS de chantier technique. La phase actuelle est **lecture / sondage / cartographie / questions à Raphaël**, pas exécution.

**Critère de fin de mission « maîtrise »** : pouvoir répondre sans hésiter aux 4 questions canoniques D11 (§10 contrat orchestrateur démo V1) sur n'importe quel sous-système Séragone :
1. Qui lit quoi ?
2. Qui décide quoi ?
3. Qui écrit quoi ?
4. Où est la preuve de trace ?

Si une réponse repose encore sur un nom supposé ou un chemin implicite, **continuer de creuser**. Quand tu peux répondre mécaniquement aux 4 sur tout le périmètre, tu signales à Raphaël et il décide du chantier suivant.

### §3.1 — Domaines à approfondir (priorité absolue, ordre suggéré)

**Les 7 trous originaux de la chronologie sont tous fermés (16 mai partie tardive).** Voir §2 ci-dessus pour le récap par trou. Méta-leçon 11e gravée pour éviter de faux trous futurs.

**Mais 11 domaines clés n'ont PAS été approfondis** par la session précédente (auto-constat honnête Claude Code C-VPS) :

1. **Les 22 équations habillant Bitcoin** — je connais les 5 dimensions M/V/S/H/G (avec Φ\*_CANON et W_CANON figés 16 avril), pas le contenu de chaque équation. **À faire** : trouver le document canon qui liste les 22 équations nominalement, lire intégralement, savoir restituer chaque équation et son rôle dans une des 5 dimensions. Chercher dans `canon/`, `audit/decisions/`, `references/imports_session_20260516/` (notamment `03_EQUATIONS_Danse_Habillage_Phases.md` du 20 mars cité dans matrice anti-oubli).

2. **Les 92 mondes nominalement** — sait qu'il y a 92 regards (305 parallèles 10D + 4 autonomes 5D), pas la liste. **À faire** : trouver l'inventaire nominatif des 92 + leur rôle individuel. Probable dans `multivers_state.json` (807 mondes bruts) à filtrer ou doc canon dédié. Sonde S1 suggérée : `find . -name "*92*mondes*" -o -name "*inventaire*mondes*"`.

3. **`BATTERIES_SONDES_FROIDES_POST_DOC22-30.md`** — créé par ACTE 29 (155 lignes, sha `daadfc56…`), **jamais lu par session précédente**. Document doctrinal mentionné comme dépôt de procédures de migration Porte 5. À lire intégralement.

4. **Le contenu littéraire / voix Séraphin** — corpus IMPREGNATION_STYLE_SERAPHIN_V7.6 (cycle février, 6+ versions), `7.77`, Vacuite/Poussiere, etc. Classés « fossile littéraire » par session précédente mais **non explorés**. La voix Séraphin EST le filtre canonique d'écriture (« neutralité, pas d'élan de bien faire littérairement, ne pas polir »). À comprendre minimalement pour ne pas écrire en violation de la voix.

5. **L'architecture détaillée du producteur 18 sous-signaux** (`extract_18ss.py` sha `e759f8849f…`, `extract_18ss_csv_v2.py` sha `967f42528f…`) — en pause Article 8 Q6 (D195). Sondé ponctuellement par R13c, **pas compris en profondeur**. Quelles sont les 18 sous-signaux ? Quelle est la chaîne BTC/FG/SP500/DXY → 18D ? À cartographier en lecture pure (chantier en pause, ne PAS relancer).

6. **Le code source des 5 modules V1 du contrat orchestrateur démo** :
   - `./aplomb.py` racine (sha `b9792c96`, sortie SHORT perm 0.5309)
   - `production/decision/policyengine.py` (142 lignes)
   - `production/allocation/double_tempo.py` (194 lignes, pure)
   - `production/protection/prudence_module.py` (MEASURE_ONLY)
   - Money Manager (fonction pure ou wrapper V1 à définir)
   **Lire chaque fichier intégralement.** Connaître leurs entrées/sorties, leur logique, leurs limites. C'est le **préalable obligatoire** au squelette `orchestrateur_demo`.

7. **Les pépites P1-P51 individuellement** — 51 pépites en states actifs. Noms connus (`pepite1_M08_sbforce` à `pepite51_M_xtbas_fr_xtbas_r30_bas`), code et logique de chacune non lus. Au minimum : grouper par famille (M0-M8, V, H, S, G, range, dd, fg, fr, etc.) et savoir quel signal chacune capte. P1-P5 actives via `pepites_tier1_adapter.py`, P6-P19 actives dans `production/pepites/`, P20-P51 dormantes (A14 = dette inachèvement, faux trou résolu).

8. **La cohabitation `origin/main` (bot auto) / `origin/canon` (humain)** — architecture connue, fonctionnement interne du bot `/tmp/push_bulletin.sh` (7 375 commits "auto") **pas investigué**. Que pousse-t-il exactement ? Quand ? Pourquoi origin/main et pas origin/canon ? À sonder en lecture pure (ne pas toucher).

9. **L'architecture des 9 services systemd Séragone** (brain, brisance, 1min, api, mondes-oneshot, mondes-paralleles, multivers, securite, sentinelle) — liste nominative connue (ATTESTATION Phase 115 §5), mais **le rôle exact, le code source, les states écrits/lus de chacun n'ont pas été cartographiés**. Pour chaque : lire l'unit file `/etc/systemd/system/seragone-*.service`, identifier le ExecStart, lire le script Python lancé, recenser ses inputs/outputs. Sortie : tableau D11-conforme par service.

10. **La doctrine Phase E** (« concevoir d'abord → installer ensuite → brancher en dernier ») — mentionnée comme cadre de DECISIONALLOCATION V1, mais **le document doctrinal source n'a pas été identifié**. À trouver dans `audit/decisions/phase_e_decisions_NOTES.md` ou équivalent, lire intégralement, comprendre les 3 étapes et leurs critères de transition.

11. **La préhistoire pré-18 mars Séragone** — la chronologie commence à Séradon paquebot (18 mars nuit). Toute la genèse antérieure (corpus février IMPREGNATION_STYLE_SERAPHIN, CANON_Seraphin v10/v11/v11.1, période CHATGPT/Perplexity 7.766/7.767/7.768/V7.770) **non explorée**. À sonder pour savoir d'où vient la doctrine (notamment l'origine de la posture L99 + OODA stricte).

**Approche méthodologique recommandée** pour chaque domaine :
- (a) Identifier les fichiers sources canon (pas les copies dans `imports_session_20260516/`).
- (b) Lire intégralement (chunks 200 lignes si gros, jamais en diagonale).
- (c) Calculer sha256, l'ajouter à la chronologie §5 ou créer une nouvelle sous-section §5.X dédiée si nécessaire.
- (d) Croiser avec ce qui est déjà tracé pour détecter cohérences/contradictions.
- (e) Capitaliser dans la chronologie + recalculer son sha + tracer dans mémoire.
- (f) **Si tentation de qualifier un « trou » ou une « violation » → appliquer méta-leçon 11e (Porte 0 rétrospective : git log + lecture intégrale doc canon + listing backups).**

### §3.1bis — Trous techniques résiduels (à traiter APRÈS maîtrise totale)

À ne PAS aborder avant que la mission §3.0 soit accomplie :

1. **Squelette `orchestrateur_demo`** (chantier principal V1) — contrat validé 13 mai 23:37Z, code pas écrit. Préalable : domaine §3.1.6 (lire les 5 modules V1) intégralement.
2. **D195 — archivage horodaté inputs 18D** — bloque relance chantier 18D. Préalable : domaine §3.1.5 (cartographier le producteur 18D).
3. **Activation cron PHASE 2 DECRET_A7** — `decision_to_order.py` + `prudence_demo_runner.py` créés 10 mai VALIDATED GO_A7 12/12, **PAS en cron**. Décision Raphaël requise (session fraîche, GO_A7 séparé).
4. **`CRONMAITRE.cron` / `CRON_MAITRE.cron` racine** — dédoublon à clarifier (un seul des deux est censé exister selon D52bis).
5. **24 modules VPS (13 avril) → 9 services systemd** — décrets de fusion à retracer. Préalable : domaine §3.1.9 (cartographier les 9 services).
6. **Indexation `audit/decisions/`** dans `canon/INDEX_CANON_SERAGONE.md` (mini-dette Dette 3 résiduelle).
7. **Mots de passe SSH compromis du 16 mai** — Raphaël s'était engagé à changer. **Ne pas relancer**, mentionner discrètement si l'occasion se présente.

**Après chaque domaine approfondi ou trou technique refermé :** mettre à jour `CHRONOLOGIE_PARFAITE_MARS_A_MAI_2026.md` (§ pertinent) et recalculer son sha256. Tracer la nouvelle version dans `memory/reference_chronologie_parfaite_mars_mai_2026.md`. Commit sur `origin/canon` (jamais `origin/main`).

### §3.2 — Objectif moyen terme

**Chantier DECISIONALLOCATION V1** — wrappers inertes, V1 contourne le legacy par orchestration.

État au 13 mai 23h15 (D11_ARBITRAGES_V1, refige V2) — 7 anomalies arbitrées :

| # | Anomalie | Décision V1 |
| --- | --- | --- |
| A1 | `policy_monitor` | lecture/print uniquement, aucune écriture |
| A2 | `capital` | scalaire passé en paramètre, pas un module |
| A3 | `aplomb` | `./aplomb.py` racine (sha `b9792c96`), SHORT perm = 0.5309 |
| A4 | `double_tempo → MM` | orchestrateur appelle séparément, passe budgets |
| A5 | `double_tempo` source | `production/allocation/double_tempo.py` (194 l) pure |
| A6 | `prudence` | `production/protection/prudence_module.py`, MEASURE_ONLY |
| A7 | `policyengine` | `production/decision/policyengine.py` (142 l) |

**Doctrine Phase E :** concevoir d'abord → installer ensuite → brancher en dernier.

**Interdits V1 absolus :**
- ZÉRO écriture disque depuis les modules.
- ZÉRO import croisé métier.
- ZÉRO dépendance à un chemin legacy implicite.
- ZÉRO mutation du legacy.

═══════════════════════════════════════════════════════════════════

## §4 — Workflow de travail (discipline canonique)

### §4.1 — Règles non négociables (verrouillées au 16 mai)

- **`SERAGONE_ARGENT_REEL = 0`** — invariant absolu. Aucun décret canonique ne le lève.
- **`DRY_RUN = True`** — partout, même Phase 115 conditionnellement levée.
- **Phase 115 reste en cage** côté ordre réel — la levée du 10 mai (A4) est seulement vers DEMO_PAPER, avec `decision_weight ≤ 0.1`.
- **Aucune modification runtime sans pièce documentaire amont signée** — cascade décret/sonde/attestation/PV, sha256 partout.
- **Aucun write legacy depuis la chaîne démo V1.**
- **Doctrine D9 :** un seul writer par state. Respecter par construction.
- **Doctrine D11 :** un nom ne prouve pas le périmètre — lire I/O réelles, pas étiquettes.

### §4.2 — Bannis du vocabulaire

- Jamais « Remplacé », « Abandonné », « Actif sans nuance ».
- Jamais résumer Séragone en 3 mots.
- Les **chiffres morts** (§5.1 chronologie) — FRAPPER 94 %, Born Omega 100 %, sync 84.6/89.1 %, sizing 2.7M€/121M€ — ne doivent **jamais être cités comme actifs**.

### §4.3 — Langue

- **Français.** Tutoiement.
- Commandes Linux restent en anglais (c'est le shell).
- Mais : libellés `echo`, commentaires bash, sections de rapport, titres de tableaux → **en français.**

### §4.4 — Lecture avant action

- Doctrine D12 : **LIRE_AVANT_DE_CONCLURE**. Tu lis le fichier en entier avant de produire un avis.
- Méta-leçon récidive Porte 0 (ACTE 30, 12 mai) : **vérifier l'exécution réelle** (cron/systemd/ps), pas seulement la présence en code (grep). Un fichier qui existe n'est pas un fichier qui tourne.

### §4.5 — Gravure et sha256

- Tout document canonique reçoit un sha256 (`sha256sum fichier`) consigné dans son acte de gravure.
- Tout document remplacé par une v2 conserve son sha256 v1 dans la trace mémoire pour archéologie.

═══════════════════════════════════════════════════════════════════

## §5 — Sécurité

- **Incident du 16 mai :** Raphaël a tapé par erreur son mot de passe SSH dans le chat (texte clair). Le mot de passe est **considéré compromis**.
- Il s'est engagé à le changer (« je changerai le code apres »).
- **Toi qui lis :** ne stocke, ne réutilise, ne référence **jamais** ce mot de passe. Si Raphaël n'a pas encore changé son mot de passe et que tu peux le rappeler une fois (sans citer l'ancien) → fais-le **discrètement**, par message direct, sans le réécrire.
- À recommander : `passwd` pour changer + passage à clé SSH si pas déjà fait.

═══════════════════════════════════════════════════════════════════

## §6 — Architecture mentale rapide (pour ne pas te perdre)

```
SOUFFLE (oreille) → SÉRAGONE (œil) → VILLAGE (geste)
                       │
                       ├── 22 équations habillant Bitcoin
                       │       → 5 dimensions M / V / S / H / G
                       │
                       ├── Φ*_CANON figé 16 avril
                       │       (M:0.28, V:0.33, S:0.26, H:0.26, G:0.42)
                       │
                       ├── W_CANON figé 16 avril
                       │       (M:1.80, V:1.25, S:1.20, H:1.42, G:1.10)
                       │
                       ├── 92 mondes = REGARDS (pas temporalités)
                       │       = 305 parallèles 10D + 4 autonomes 5D
                       │
                       ├── 3 familles + 1 spectre
                       │       RÉCURSION / PARALLÈLES / COMMUNICANTS / SPECTRE CWT
                       │
                       ├── CWT 666 échelles (3j → 1111j), Sniper 92 % WR
                       │
                       ├── Couverture moteur + 4 autonomes = 99.8 % (618/619)
                       │
                       └── Loi attestation : 1 voix=52 %, 2+=62/67 %,
                                             3+=63/73 %, Bear 40+=87.5 %

DOCTRINES HASHÉES : D1 META · D6 NON_SERAGONE · D7 MODE_DEMO_TOTAL
                    D9 UN_WRITER_PAR_STATE · D11 NOM_NE_PROUVE
                    D12 LIRE_AVANT_DE_CONCLURE

DOCTRINES RÉVÉLÉES PAR LECTURE TARDIVE 16 MAI :
                    Article 8 Q6 "on laisse comme ça"
                    Doctrine 7 decision_weight_real = 0.0
                    VALIDATED != INSTALLED
                    R1 Mondes != Tireurs
                    Posture sonder/décréter/activer (3 temps)
                    Mondes filtrent, ne tirent jamais

PHASES :  Phase 115 LIVE_TEST_TOTAL_EN_CAGE (27 avril)
          → Levée conditionnelle vers DEMO_PAPER (10 mai, A4)
          → A4bis H5 acté (DEMO_PAPER ≡ MODE_DEMO_TOTAL, 10 mai 11h)
          → A5 reconnaissance scénario 3 économe (10 mai 11h30)
          → A6 poller aval démobroker cron actif (10 mai 18h24)
          → A7 pipeline 4 maillons VALIDATED PHASE 1 (10 mai 20h10)
          → D11_ARBITRAGES_V1 7 anomalies (13 mai 23:15)
          → CONTRAT_ORCHESTRATEUR_DEMO_V1 VALIDATED (13 mai 23:37)
          → R13c chantier 18D maintenu en pause (15 mai 08:10Z)
          → CHANTIER COURANT : squelette orchestrateur_demo
                               + V1_STATE_DIR à créer
                               + activation A7 PHASE 2 (différée)
```

═══════════════════════════════════════════════════════════════════

## §7 — Nomenclature des 4 rôles Claude (parle d'eux ainsi)

- **C-VPS** — IA qui agit côté VPS (toi par défaut).
- **C-MAT** — IA matrice / analyse de fond.
- **C-SNIPER** — IA précision sur un point précis.
- **C-DOC** — IA documentaire (rédige décrets, attestations).
- **C-TMP-xxx** — IA temporaire sur tâche ponctuelle.

Tu es probablement **C-VPS**.

═══════════════════════════════════════════════════════════════════

## §8 — Le moins que tu fasses en arrivant

1. **Lire CHRONOLOGIE_PARFAITE v11 intégralement** (996 lignes, sha `2f98eda8086a0012061b24353f91e0425624243f3f0fb35dc5a01e5f93cb29bc`). Vraiment intégralement, par chunks 200 lignes si besoin, pas en diagonale.
2. **Lire `ANOMALIES_A8_A9_12mai2026.md`** (576 lignes, sha `a5aaf10f94328f4cde9d8a87a4883de19987f01eef03e7a2e458c0e9fcfae01c`) — contient les 11 méta-leçons + Doctrine 6 Portes + Procédure patch chirurgical.
3. **Lire ce passage de relais §3.0 + §3.1 intégralement** — la mission n'est PAS de coder, c'est d'**approfondir 11 domaines** pour maîtriser le programme.
4. Dire à Raphaël : *« J'ai lu la chronologie v11 + ANOMALIES_A8_A9 + le passage de relais. Tu veux que je commence par quel domaine §3.1 ? Ou tu as une autre priorité ? »*
5. Une fois la priorité fixée : sonder le domaine en lecture pure, capitaliser, recalculer sha chronologie, commit canon. Ne pas multiplier les chantiers ouverts.
6. Ne pas toucher au code legacy, ne pas inventer de décrets, ne pas créer `orchestrateur_demo` avant maîtrise totale.
7. **Tutoyer en français. Pas d'emoji.**

═══════════════════════════════════════════════════════════════════

**FIN PASSAGE DE RELAIS**

Auteur passage : Claude Opus 4.7, session 16 mai 2026.
Maj 16 mai partie tardive (Claude Code C-VPS) : 7 trous fermés, 1 faux trou résolu, méta-leçon 11e gravée, chronologie v11.
**Maj mission §3.0 (16 mai partie tardive, fin de session)** : focus prochaine IA = maîtrise totale du programme avant détails (volonté Raphaël explicite). 11 domaines listés §3.1.

À mettre à jour à chaque fin de session — chaque IA grave son propre passage pour la suivante.
