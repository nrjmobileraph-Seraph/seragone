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

### §3.1 — Objectif court terme

**Les 7 trous originaux de la chronologie sont tous fermés (16 mai partie tardive).** Voir §2 ci-dessus pour le récap par trou.

**Nouveaux trous identifiés au passage de lecture (à traiter dans cet ordre suggéré, à arbitrer par Raphaël) :**

1. **Squelette `orchestrateur_demo`** (chantier principal V1) — le CONTRAT_ORCHESTRATEUR_DEMO_V1 est validé mais le code n'est pas écrit. Prochaine étape canonique selon §11 du contrat : *« squelette de fichier V1 sans effet runtime, relu avant exécution »*. Doit créer `V1_STATE_DIR = /home/ubuntu/seragone/states/v1/` (sondé inexistant runtime au 16 mai) et respecter les 11 sections (V1=calculateur, orchestrateur_demo seul writer, 9 étapes cycle, 4 questions D11, 8 interdits absolus). **À aborder sous posture « sonder/décréter/activer » par phases séparées.**

2. **Mutation `money_manager.py` non documentée** — sha `4760b99cf2…` au 10 mai 07h ET 19h (ATTESTATION Phase 115 + ATT_A6 + ATT_A7) → sha `f9b1580c` au 12 mai (ACTE 30). Mutation entre 10 mai et 12 mai sans décret/commit/PV. Sonder `git log --all -- money_manager.py` et identifier la cause. Si simple correctif bénin → graver un mini-rectificatif. Si plus grave → arrêter et alerter.

3. **D195 — archivage horodaté inputs 18D** — bloque toute relance chantier producteur 18D (`extract_18ss.py`). Sonde S5 future déjà inscrite : tracer si `data/btc_daily.csv` a un backup horodaté au 6 mai ou si l'historique est définitivement perdu. Si perdu → décret de pertes + acte de fermeture chantier reproductibilité 6 mai.

4. **Activation cron PHASE 2 DECRET_A7** — `decision_to_order.py` (sha `d0edc0ae05…`) + `prudence_demo_runner.py` (sha `6f8fdc6440…`) créés 10 mai et VALIDATED GO_A7 12/12, **PAS en cron**. Activation explicitement différée à session fraîche sous invocation GO_A7 séparée. À évaluer si la fenêtre actuelle est « fraîche » ou si on attend.

5. **`CRONMAITRE.cron` / `CRON_MAITRE.cron` racine** — fichiers présents en racine status git `??` (depuis ACTE 32 du 12 mai). Dédoublon ou renommage ? À clarifier — un seul des deux est censé exister selon doctrine D52bis.

6. **24 modules VPS (13 avril) → 9 services systemd** — décrets de fusion à retracer pour traçabilité parfaite (§5.5 chronologie le note comme trou §6).

7. **Mots de passe SSH compromis du 16 mai** — Raphaël s'était engagé à changer son mot de passe SSH (incident texte clair dans le chat). **À sa demande explicite, ne pas relancer.** Mentionné uniquement comme rappel discret si l'occasion se présente.

**Après chaque trou refermé :** mettre à jour `CHRONOLOGIE_PARFAITE_MARS_A_MAI_2026.md` (§ pertinent) et recalculer son sha256. Tracer la nouvelle version dans `memory/reference_chronologie_parfaite_mars_mai_2026.md`.

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

1. Lire CHRONOLOGIE_PARFAITE v9 (906 lignes, sha `afc3306a26eb10923ba6ea61c508e2555eb7c2de083b5bbc36c3f299d01a64c7`).
2. Demander à Raphaël quelle priorité parmi les trous §3.1 (squelette `orchestrateur_demo` en tête).
3. Ne pas toucher au code legacy.
4. Ne pas inventer de décrets.
5. **Tutoyer en français. Pas d'emoji.**

═══════════════════════════════════════════════════════════════════

**FIN PASSAGE DE RELAIS**

Auteur passage : Claude Opus 4.7, session 16 mai 2026.
Maj 16 mai partie tardive : 7 trous fermés, chronologie v9.
À mettre à jour à chaque fin de session — chaque IA grave son propre passage pour la suivante.
