- 2026-04-28 — DOCTRINE_MOTEUR_META_SERAGONE.md
  Statut : VISION CANONIQUE
  Rôle : définit le moteur META comme organe d'évolution, d'humilité épistémique,
  de détection d'aveuglement, de ranking, de lifecycle et de proposition de nouveaux modules.

- 2026-04-28 — DOCTRINE_NON_SERAGONE.md
  Statut : DOCTRINE 6 ACTIVE
  Rôle : définit le statut NON_SERAGONE pour tout module présent sur le VPS
  Séragone mais appartenant à un projet distinct hors périmètre canon ;
  ces modules ne sont ni promouvables ni archivables sans accord explicite,
  et conservent leur cycle de vie indépendant.

- 2026-04-28 — DOCTRINE_7_MODE_DEMO_TOTAL.md
  Statut : DOCTRINE 7 v1 SUPERSEDED (remplacée par D7 v2, 2026-05-11)
  Hash : cec31501181280a50bd8e29f405719771f198eb5ff8203a468f29266db5f311d (préservé)
  Archive : audit/archives_canon_20260511T082058Z/DOCTRINE_7_v1_ARCHIVE_20260511T082058Z.md
  Rôle historique : première pose canonique du mode "vraie utilisation,
  fausse réalité financière" ; mention OKX remplacée par Kraken en v2.

- 2026-05-11 — DOCTRINE_7_v2_MODE_DEMO_TOTAL.md
  Statut : DOCTRINE 7 v2 ACTIVE (Kraken pur)
  Hash : bd0d1a06a193a458f899a513971913e639e69f728dd97bfe64781d296991d6e7
  Rôle : remplace D7 v1 (SUPERSEDED), purge OKX textuelle, grave Kraken
  comme cible exchange unique, absorbe A1 (D7_5_EXCHANGE_REEL) et
  A3 (D7_8_EXCHANGE) en doctrine formelle ; règle d'or inchangée :
  ne pas bloquer Séragone, bloquer seulement le réel financier.

- 2026-04-28 — DOCTRINE_9_UN_WRITER_PAR_STATE.md
  Statut : DOCTRINE 9 ACTIVE
  Rôle : un seul writer par fichier state ; chaque module écrit son propre
  _state.json ; un agrégateur fusionne en lecture seule sans écriture
  concurrente ; pattern d'écriture atomique POSIX (temp + rename) obligatoire ;
  cohabite avec D7 et structure les contrats d'état pour MODE_DEMO_TOTAL et META.

- 2026-04-29 — DOCTRINE_11_NOM_NE_PROUVE_PAS_PERIMETRE.md
  Statut : DOCTRINE 11 ACTIVE
  Rôle : le nom d'un service, fichier, module ou processus ne prouve pas son
  périmètre réel ; seuls ExecStart, WorkingDirectory, Environment, chemins
  absolus et résolus, descripteurs et sockets ouverts, fichiers et logs
  effectivement écrits, et code source effectivement exécuté prouvent ce
  qu'un composant lit, écrit, sert ou orchestre ; complète D9 sur l'identification
  mécanique du writer effectif.

---

## Notes

D8 (lecture intégrale obligatoire) reste candidate à reformuler.

D10 (un seul dossier source par flux) reste candidate forte, à confirmer
après Q5-B10.

Discipline candidate "Writer canonique mort" (Q5-B9) reste à laisser maturer.

D11 est active à partir de Phase E Day 7.

[2026-05-09 23:16:58 UTC] canon_lot_a3_1_preservation_20260509_231658 — 39 fichiers (G1=3, G2=absent, G3=37), voir MANIFEST.md

[2026-05-11 08:29:34 UTC] Q4 — D7 v2 gravée (bd0d1a06...), D7 v1 SUPERSEDED (cec31501... préservé), A1+A3 absorbés ; voir DECRET_Q4_D7_v2_GRAVEE_ABSORBE_A1_A3_2026-05-11.md (aa084680...)

[2026-05-11 ~09:15 UTC] Q5 — INSCRIPTION_CANONIQUE_META + RESOLUTION_D11 ;
  voir audit/decisions/DECRET_Q5_INSCRIPTION_CANONIQUE_META_2026-05-11.md
  Blueprint META_GLOBAL_ENGINE.md v1.1 (1f6c6057...) promu BLUEPRINT_CANONIQUE_ACTIF ;
  Stade 1 OBSERVATOIRE autorisé ; Stades 2-3 VERROUILLÉS.
  D11 tranchée sans renommage : production/meta/meta_controller.py = META_CONTROLLER_CANON ;
  production/allocation/meta_controller.py = PERF_WEIGHT_CONTROLLER (orchestrateur.sh l.170).
  Rectification doctrinale douce §3.4 (VISION non modifiée, 00daf217... préservé).
  A4 (236dc387...) confirmé ACTIF. Extension MONDES reportée.

[2026-05-11 ~12:05 UTC] LECTURE_CANONIQUE_LES_VRAIS_MONDES — 566L, 5 dims M V S H G extraites (sommes=1.00), couplage S<-V, pattern ^1.5, backtest __main__ ; voir audit/decisions/LECTURE_CANONIQUE_LES_VRAIS_MONDES_2026-05-11.md

[2026-05-11 ~12:08 UTC] ATTESTATION_Q5 — sceau Q5 patron Q2/Q3/Q4, recoupe 8 hashes (decret+registry+3 canons META+2 backups+INDEX post-acte17) + invariants 6x6 + D11 physique confirmee ; voir audit/decisions/ATTESTATION_Q5_INSCRIPTION_META_2026-05-11.md

[2026-05-11 ~12:20 UTC] CARTOGRAPHIE_MONDES_SUITE6 — 6 modules prod, 4 states racine canoniques ; cardinalites runtime reelles : 191 paralleles + 4 autonomes (Rythme/Anti-V/Persistance/Rebond) + 8 canaux communicants x 24 signaux + 0 long ; rectification doctrinale : "70 mondes" est faux (70 = lag/seuil/%), total reel = 203 entites ; couplage chef<->mondes par JSON ; 3 orphelins Python ; voir audit/decisions/CARTOGRAPHIE_MONDES_SUITE6_2026-05-11.md
2026-05-11 ~12:32 UTC | REVISION_SUITE6_CARTOGRAPHIE_MONDES — patche D19 (832a4535…) : 0 orphelin (pas 3), 9 services + 2 timers systemd découverts, migration cron→timer 9 mai, 3 incoherences ouvertes (I1 cardinalite, I2 double brisance, I3 chemin) ; preuves suite6d a1671a6c… + suite6d_bis 9bd8215f… ; voir audit/decisions/REVISION_SUITE6_CARTOGRAPHIE_MONDES_2026-05-11.md

[2026-05-11 ~12:33 UTC] APPENDIX_REVISION_SUITE6_ARCHITECTURE_SYSTEMD — complete D20 (532bc587…) tronque ; 9 services + 2 timers systemd Seragone inventories + 13 PID python3 actifs + details I1/I2/I3 ouverts + 6 points SUITE-6 en attente ; voir audit/decisions/APPENDIX_REVISION_SUITE6_ARCHITECTURE_SYSTEMD_2026-05-11.md
2026-05-11 ~19:25 UTC | CLOTURE_SESSION_SUITE6_VOIE3PRIME — V4 adoptee : respect doctrine 26 mars 'NE BRANCHE RIEN', decouverte regenerer_c1_canon.py comme producteur canon bloque doctrinalement ; dossier 'Bascule Canon V2' transmis a session future ; invariants 6x6 preserves 18h15+ ; snapshot 88112f79 ; voir audit/decisions/CLOTURE_SESSION_SUITE6_VOIE3PRIME_2026-05-11.md

## Scellement final session 11 mai 2026 (post-cloture V4)

Reference : audit/scellement_final_11mai_20260511T192747Z/

| Acte | Fichier | Hash SHA256 |
|------|---------|-------------|
| 28 | audit/decisions/CONSTAT_MODE_DEMO_PHASE2_DEJA_ACTIVE_DEPUIS_10MAI_2026-05-11.md | 8305bad3d0d50dfb1fee50fe6ddcad9c30da9d06107ace182d64104448a547b7 |
| 29 | audit/decisions/VALIDATION_FILTRE_SECURITE_PIPELINE_DEMO_A7_2026-05-11.md | 31b64f3d34c01ad47d1a4b576bd639dabde47b32f1669843eebb3045a057c9a4 |
| 30 | audit/decisions/CARTOGRAPHIE_CANONIQUE_TOTALE_SERAGONE_11MAI_2026-05-11.md | 61358af826c0f2ea85cb4083b4c184b0a7b72af044962801f01a6ab908c0e18d |
| 31 | audit/decisions/META_SCELLEMENT_MONDES_PARALLELES_ET_MULTIVERS_2026-05-11.md | 02433feffe29257a296bbb7cabf96979ed967ea51f4368dcfb67067c7c5ebe96 |
| 32 | audit/decisions/INVENTAIRE_PEPITES_MOTEURS_M1_M8_2026-05-11.md | d5c832289606fc6a15d9d136c099c9dae01bb39e0c4539b884c007f106802c41 |
| 33 | audit/decisions/ATTESTATION_CLOTURE_DEFINITIVE_SESSION_11MAI_2026-05-11.md | 92a7940a504d0be4b6c72e35434078aed2c1e8932393cceb268361868cf758cf |

Invariants 6x6 post-scellement final (immutables toute la session) :
- vrais_yeux.py              = f8de03b6025d5a9fddbd9e9cfc69ac342e9f26e651e9be57a876910c499e5850
- money_manager.py           = f9b1580c94bbdf3245c1ac4629d2db85bb71485f175f1cd6733a409aeab0aa75
- chef_orchestre_v1_state.py = 0b251bfdf2356cb559e8a5fef6539b889560febca277315a7da4c3acb6507330
- seragone_pilot.py          = 661f50815c876e79ff26f2d15d44ce44b39f590c01fed53a98b2793880e61cdd
- ailes_dor.py               = d7e9ef14f7e680af0b516b1eb573a295433855131194d5e2347d6ef82c76d8eb
- les_vrais_mondes.py        = 06ef3a6639d3e4ea08e76c2c5e29a04d6c8764a1f95fd84ff497d8d17cbc354c

16 chantiers transmis session N+1 : voir acte 30 section 12.


## ACTE 22 — SERAGONE_ONE V1 (20260511T203916Z)
- Chemin : `audit/grave_22_seragone_one_v1_20260511T203916Z/`
- Source unique de vérité : `canon/SERAGONE_ONE.md`
- Générateur : `tools/seragone_one.py` (cron horaire min 15)
- Wrapper : `seragone-total`
- Hash univers : `439cc638637886ae`

## ACTE 23 — MASK seragone-multivers (20260511T204342Z)
- Chemin : `audit/acte23_mask_multivers_20260511T204342Z/`
- Action : systemctl mask service + timer (réversible)
- Raison : service dead + writer cassé (voir suite6g1-g5)
- Successeur : ACTE 24 futur voie 3prime

## ACTE 23-bis — ANNULATION acte 23 (20260511T204536Z)
- Chemin : `audit/acte23bis_ANNULATION_20260511T204536Z/`
- Motif : acte 23 basé sur diagnostic faux (oneshot confondu avec dead)
- Action : re-enable + start timer
- Leçon : toujours lire journalctl avant mask

## DOCTRINE 12 — LIRE AVANT DE CONCLURE (20260511T204701Z)
- Chemin : `canon/DOCTRINE_12_LIRE_AVANT_DE_CONCLURE.md`
- Contexte : fait suite au couple ACTE 23 + 23-bis
- Règle cœur : logs réels avant tout diagnostic, jamais les noms de dossiers

## ACTE 24 — Pipeline A7 end-to-end + fix $SERAGONE (20260511T205215Z)
- Chemin : `audit/acte24_A7_endtoend_FIX_SERAGONE_20260511T205215Z/`
- Cause : $SERAGONE non défini en env cron
- Fix : chemins absolus dans crontab
- Preuve : logs remplis après fix

## ACTE 24-bis — Précision idempotence A7 (20260511T205437Z)
- Chemin : `audit/acte24bis_PRECISION_pipeline_idempotent_20260511T205437Z/`
- Précise : le silence A7 est du DESIGN (SKIP_IDEMPOTENT)
- Démo : injection hash reset + observation end-to-end
- Deuxième leçon Doctrine 12 dans la soirée

## ACTE 25 — Pipeline A7 END-TO-END démontré (20260511T205953Z)
- Chemin : `audit/acte25_A7_ENDTOEND_DEMONTRE_20260511T205953Z/`
- Chaîne : generator → prudence V2 D85 → demobroker (3 min end-to-end)
- Preuves : ordre AUTO_A7_20260511T205502 + exec DEMO_EXEC_ccd1b550a4d7
- Rapport : `demo/reports/RAPPORT_A7_ENDTOEND_20260511.md`
- Garde-fous : real_finance_used: false ✅

## ACTE 26 — Position canonique MOTEUR META Stades 1/2/3 (20260511T210729Z)
- Chemin : `audit/acte26_POSITION_CANONIQUE_META_STADES_20260511T210729Z/`
- Stade 1 OBSERVATOIRE : ACTIF (mondes_autonomes + multivers + perf_weight)
- Stade 2 CROISEMENT : VERROUILLE (Q5 §3.1 respecté)
- Stade 3 SOLLICITATION : VERROUILLE (Q5 §3.1 respecté)
- Legacy déclassé : mondes_paralleles_state.json → LEGACY_OBSOLETE_20260423
- Chantier futur : DECRET Q6 déverrouillage après démo
2026-05-11 21:48 UTC  ATTESTATION_BASCULE_CANON_V2 — DECRET_RETROACTIF_11 FULFILLED_EMPIRICALLY (multivers V2 actif) — audit/decisions/ATTESTATION_BASCULE_CANON_V2_2026-05-11.md 348a5a57a093df946610b6a850ddb934b537d869756f409ab22e3a18a0e3248a
2026-05-11 21:51 UTC  ATTESTATION_P1_DIAGNOSTICS_I1_I4 — 4 incohérences résolues documentairement — audit/decisions/ATTESTATION_P1_DIAGNOSTICS_I1_I4_2026-05-11.md 03642ab897c6883ad481a33044045f04397e53cc7669e7ff33f799d7cdf60c51

## ATTESTATION_P2_LECTURE_CANONIQUE_A4_A7_ZETA1_2026-05-11
- fichier : audit/decisions/ATTESTATION_P2_LECTURE_CANONIQUE_A4_A7_ZETA1_2026-05-11.md
- sha256 : 422357d3b076d03fabf675880ebe2c0859792f2d1de599b2c2065a14077dc2cf
- date UTC : 2026-05-11T21:57:00Z
- chantier ζ1 RÉSOLU DOCUMENTAIREMENT (CARTOGRAPHIE §12.C)
- lecture canonique formelle : DECRET_A4 + DECRET_A5 + DECRET_A6 + DECRET_A7
- annexes lues : ATT_A6_OPE + ATT_A7_OPE + VALIDATION_FILTRE_SECURITE_A7 + ATT_V4_H5_GO_A5
- trace Phase O : p2_phase_O_20260511T215452Z (sha256 56ee2833505616a163768ddc4a17203d7f371c549d764334f85e84a11f139518)
- trace Phase A : p2_phase_A_20260511T215706Z (sha256 bee01ef2ba575e04d89a6c1c15c3694b92d0ac2db38fe0f5d0042ee129b966fd)
- 6x6 AVANT == APRÈS (scellement doctrinal pur, zéro runtime)

## ATTESTATION_B_LECTURE_MONDES_GAMMA3_2026-05-11
- fichier : audit/decisions/ATTESTATION_B_LECTURE_MONDES_GAMMA3_2026-05-11.md
- sha256 : 18d9088a250df33063af056d09cda902b4e68159225275ff857f68c5f2080c85
- lecture canonique : mondes_communicants + mondes_autonomes + mondes_paralleles_engine + inventaire γ3 (7 familles)
- trace Phase O : b_lecture_mondes_phase_O_20260511T215902Z

## CORRECTION_GAMMA3_VRAIS_YEUX_STRETCHED_HARMONISATION_RHO2_2026-05-11
- fichier : audit/decisions/CORRECTION_GAMMA3_VRAIS_YEUX_STRETCHED_HARMONISATION_RHO2_2026-05-11.md
- sha256 : 6e80fe968ec8a97e2813ab9418b2668a4f4384486687e087fd7edb3b231bccd0
- action : vrais_yeux_stretched.py racine harmonisé sur production (13010758f417… → a5d633bb81cf…)
- backup cryptographique : archive/vrais_yeux_stretched_v130_20260409_backup_20260511T220351Z.py

## CONSTAT_I4_HYPOTHESE_COMPUTE_ALL_DIMS_2026-05-11
- fichier : audit/decisions/CONSTAT_I4_HYPOTHESE_COMPUTE_ALL_DIMS_2026-05-11.md
- sha256 : 9fb6d0e311c9bf032ef6c36bfad1ae310daf100792d70cb3fb52aba9d94482a0
- H1 (compute_all_dims manquant) potentiellement résolu par ρ2 — à confirmer session I4-focus future

## CONSTAT_I4_CLARIFICATION_POST_SONDE_EMPIRIQUE_2026-05-11
- fichier : audit/decisions/CONSTAT_I4_CLARIFICATION_POST_SONDE_EMPIRIQUE_2026-05-11.md
- sha256 : 75b21fb663003a699efed76968a2015299af3fc6f0ed85795130b69e24bba2c4
- sonde empirique : exit 0 en 54s, mondes_paralleles_engine.py tourne sans crash
- H1 (compute_all_dims) FALSIFIÉE comme cause d'I4
- ρ2 préservée (utile préventivement, pas cause I4)
- nouvelles hypothèses H5 (wrapper timer), H6 (v4.bak), H7 (mondes_autonomes), H8 (cache 7 mondes)

## CONSTAT_I4_CAUSE_CONFIRMEE_H10_BROADCAST_10D_18D_2026-05-12
- fichier : audit/decisions/CONSTAT_I4_CAUSE_CONFIRMEE_H10_BROADCAST_10D_18D_2026-05-12.md
- sha256 : e4d1e20bf2fb023d79e8b6db06e54f553c9f7dad02f6265b64ddc2c26e0d29f7
- cause I4 : ValueError broadcast (10,) vs (18,) ligne 555 eval_today — cache 18D vs code 10D
- H10 CONFIRMÉE empiriquement, H1-H9 falsifiées ou partielles
- timer systemd reste désactivé, résolution ρ3-a à exécuter session dédiée

## ATTESTATION_RHO3A_REBUILD_CACHE_10D_SUCCES_2026-05-12
- fichier : audit/decisions/ATTESTATION_RHO3A_REBUILD_CACHE_10D_SUCCES_2026-05-12.md
- sha256 : 27c3a3d8bc1defa442162b70da2d9134dd6b2fc92ecf5c93a8e085caff91ceb5
- action : mondes_paralleles_engine.py --rebuild (210s, exit 0)
- cache avant : 6a7bd5a7074c… (191 mondes 18D, 144374 o)
- cache après : c9aa23aa7f11… (628 mondes 10D, 451134 o)
- test reprod : exit 0, 86s, 23/628 actifs
- I4 CLOS empiriquement, timer reste désactivé (réactivation séparée)

## ATTESTATION_TIMER_I4_REACTIVATION_2026-05-12
- fichier : audit/decisions/ATTESTATION_TIMER_I4_REACTIVATION_2026-05-12.md
- sha256 : 1d36927f09c8ff5e97d18f241192103ca4ad7768abd2394500bc61a6a9a281bf
- action : enable + start timer après 3 runs EXIT 0 consécutifs
- observation 5 min : 2 success / 0 fail
- I4 runtime pleinement restauré

## DECISION_INDEX_CANON_NON_EXHAUSTIF_2026-05-12
- fichier : audit/decisions/DECISION_INDEX_CANON_NON_EXHAUSTIF_2026-05-12.md
- sha256 : 0b295905c908bb2608a02ed6fd5a87ff8f51b1d33561788311d3672165bbea73
- décision : INDEX_CANON liste les décisions MAJEURES sélectivement, pas exhaustivement
- critère sélection : DECRETs, ATTESTATIONs, DOCTRINEs, CARTOGRAPHIEs structurantes
- source brute exhaustive : audit/decisions/ (mémoire totale)
- couverture actuelle : 24/87 (27,6%), accepté comme légitime

## APPLICATION_D6_NON_SERAGONE_FINARY_PATCH_RACINE_2026-05-12
- fichier : audit/decisions/APPLICATION_D6_NON_SERAGONE_FINARY_PATCH_RACINE_2026-05-12.md
- sha256 : 7f5254ae910736c81d2c68eae477455da96de583e99c09403acf83e0174316b1
- application D6 NON_SERAGONE aux 2 fichiers finary_patch.py + finary_patch_v2.py racine
- statut : conservés sur disque, ignorés git via pattern dédié

## MD1_RESOLU_PAR_TRACE_EXISTANTE_2026-05-12
- fichier : audit/decisions/MD1_RESOLU_PAR_TRACE_EXISTANTE_2026-05-12.md
- sha256 : 503f76bd7eac8fcdc12eb2eb4b6068e62a546a846efc47730d9377dce6a4e541
- MD1 = fausse alarme structurelle, tri déjà tracé dans 5+ artefacts canon
- méta-leçon #15 gravée : chercher trace avant qualifier dette

## ATTESTATION_I2_DOUBLON_BRISANCE_CLOS_2026-05-12
- fichier : audit/decisions/ATTESTATION_I2_DOUBLON_BRISANCE_CLOS_2026-05-12.md
- sha256 : 71d625efa9fd357205dc121b118909e8d54734ee41322e3e3dc32d523e02385c
- I2 clos : doublon manuel brisance.py PID 2520658 killé -TERM, PID systemd 2520838 actif

## ATTESTATION_HASH_D7v2_GELE_2026-05-12
- fichier : audit/decisions/ATTESTATION_HASH_D7v2_GELE_2026-05-12.md
- sha256 attestation : b109edc7c0bb27bec024deb4a90121c3af91fc02c2b64eb09c744b2194fc9503
- hash D7v2 gravé : bd0d1a06a193a458f899a513971913e639e69f728dd97bfe64781d296991d6e7
- résout placeholder ligne 9 DOCTRINE_7_v2_MODE_DEMO_TOTAL.md sans toucher au fichier doctrine

## ATTESTATION_DEMO_TOTALE_OPERATIONNELLE_2026-05-12
- fichier : audit/decisions/ATTESTATION_DEMO_TOTALE_OPERATIONNELLE_2026-05-12.md
- sha256 attestation : b59be7d59dcddaf46585e20a5ff7eff95ad49c3d9a3834b70f66245a80d190a2
- snapshot runtime : audit/rapports/SNAPSHOT_DEMO_TOTALE_2026-05-12_2045UTC.txt
- sha256 snapshot : b6e472d088126166fb3611855829b673efd6cda25d4c018c0a409f5b1c895b7f
- verdict : Séragone DÉMO TOTALE OPÉRATIONNELLE — 9 services, 2 timers, 17 crons, 7 process Python, demo/ pipeline actif
- doctrine cadre : D7 v2 (hash bd0d1a06a193a458f899a513971913e639e69f728dd97bfe64781d296991d6e7)

## AUDIT_COMPLETUDE_DEMO_2026-05-12
- fichier : audit/decisions/AUDIT_COMPLETUDE_DEMO_2026-05-12.md
- sha256 : b7643131e47ba253008fff197b10d5d3af251fed083737cb9c8f865751a415b2
- verdict : Séragone démo totale OPÉRATIONNELLE EXCELLENTE, 0 trous bloquants
- 4 trous suspects analysés : T1 T3 T4 = faux positifs, T2 = hors scope démo (D11 futur)

## ATTESTATION_OBSERVABILITE_TRADES_DEMO_2026-05-12
- fichier : audit/decisions/ATTESTATION_OBSERVABILITE_TRADES_DEMO_2026-05-12.md
- sha256 : 53acee8af9dc06b49731ebd0426d31128e1144b8eb7f52154da9214329d1f6ec
- verdict : TOUS outils tournent ✅ / 0 trade gagnant aujourd'hui 🔴 / 13 SHORT non clôturés / fees -0.52 USDT

20260512T214130Z — DECRET_RESTAURATION_FAMILLE_M_v1_2026-05-12 — Décret-cadre documentaire restaurant M3, M5, M6, M7, M8 (5 chantiers ouverts, conditions de validation gravées) ; aucun runtime modifié ; aucun cron ajouté ; Phase 115 préservée ; sha256 7259f3239064e1a3a932901cebb9e0b3d510c7f3321aad9e200ebeddb517a49f.

20260512T214257Z — DIFF_M5_DEDOUBLEMENT_D11_2026-05-12 — Sonde mécanique D11 du dédoublement nominal M5 (m5_grappillage.py vs Grapillage_puissance_bear) ; trace mécanique gravée ; verdict canonique en attente ; aucun runtime modifié ; sha256 989bb9e32b85e9f6cc58a7d90186c81c733d8f75a5a4ef316f8ce1ac439be44a.

20260512T214816Z — DECRET_M5_VERDICT_NOMINATIF_D11_2026-05-12 — Verdict canonique D11 ; Grapillage_puissance_bear.py reconnu souverain de facto M5 ; m5_grappillage.py reconnu placeholder vide ; aucun runtime modifié ; sha256 674420a3817050c0a2cb9850194a791542f7de9db1f3597871c115bdd17c9214.

20260512T215024Z — SONDE_M3_TEMPERANCE_LECTURE_2026-05-12 — Sonde mécanique M3 (corps, state, callers, cron, CSV) ; décision canonique en attente ; aucun runtime modifié ; sha256 e2f55c30f60cee646abdcc570e8b39a1ae8022b081e0f7ef0a5531142773a69d.

20260512T215340Z — DECRET_M3_STATUT_CANONIQUE_2026-05-12 — Verdict Option α ; M3 reconnu moteur validé doctrinalement, non installé au canon ni en production active ; pattern D12 attesté ; plan de validation par backtest walk-forward gravé en 3 actes ultérieurs ; aucun runtime modifié ; sha256 326b64ff8191ab47bb5272abf4c00457cebeec79f73393faca449714f732a9d8.

20260512T215640Z — SONDE_M8_TRESORERIE_LECTURE_2026-05-12 — Sonde mécanique M8 (corps, state, callers, cron, pépite P1, CSV) ; décision canonique en attente ; aucun runtime modifié ; sha256 8ef5304834f06f1a895554ff725b1de2f2744e637e060792d13b9912d233ef1f.

20260512T215938Z — DECRET_M8_STATUT_CANONIQUE_2026-05-12 — Tranchage D11 dédoublement bit-identique (production/moteurs/m8_tresorerie.py souverain, moteurs/moteur_tresorerie_active.py legacy) ; constat absence contrat MM ; pattern D12 hybride attesté ; plan validation 4 actes conditionnels gravé ; aucun runtime modifié ; sha256 261bb65545460e78e177405f6ecca71632a98f1d4edeac95f0d98ffc18308bf5.

20260512T220246Z — SONDE_M6_PEPITE_P18_LECTURE_2026-05-12 — Sonde mécanique pépite P18 (unique trace M6 sur VPS) ; caractérisation pré-création/promotion ; aucun runtime modifié ; sha256 f70e0671aae0c5e673dd1bf0557eec10b8b0dd4899487e2c23c3cfeb13f16bcf.

20260512T220450Z — DECRET_M6_RECONNAISSANCE_P18_EQ_M6_2026-05-12 — D11 inversé ; reconnaissance canonique mécanique que pépite P18 EST M6 souverain de facto ; cron 09:02 actif, backtest interne 75/80% WR ; 5e cause canonique de disparition identifiée (dégradation par appellation) ; aucun runtime modifié ; sha256 812bc55acb2b41d9085334a0434d922bfa2f6768dfb829aa54df2d788ae6db4f.

20260512T220628Z — SONDE_M7_DONNEES_FACTICES_LECTURE_2026-05-12 — Sonde mécanique M7 ; preuve bug données hardcodées ; recherche collector_binance ; recherche pépite P19 (candidat M6-like) ; aucun runtime modifié ; sha256 1f46ebe1165e0915e67b3477e66e407a3117c5d6370accb1140b8f533d2c513a.

20260512T220954Z — DECRET_M7_HYBRIDE_P19_PARTIEL_BUG_2026-05-12 — Verdict hybride M7 : (1) P19 reconnue M7-tension-partiel ; (2) m7_micro.py marqué INVALID_BUG_HARDCODE (nouvelle catégorie canon) ; (3) tranchage D11 dédoublement bit-identique ; (4) plan réparation collector_binance différé en 4 actes conditionnels ; aucun runtime modifié ; sha256 68d785596ac41c1072fe51416f0e7730f0c4b82f193a0e65b4605b61a2a57852.

20260512T221350Z — SONDE_COLLECTOR_BINANCE_PERIMETRE_READONLY_2026-05-12 — Sonde mécanique du module API binance ; séparation endpoints read-only vs trade ; preuves Phase57/62/63 ; préparation acte ultérieur A du plan M7 ; aucun runtime modifié ; sha256 4994b16d90231d73f29db6c69620f558ab9f6d5811963669bfac1d606cc7b354.

20260512T221606Z — DECRET_COLLECTOR_BINANCE_READONLY_CONFIRME_2026-05-12 — Verdict Option γ : module 100% read-only par construction (WebSocket public, 0 endpoint privé, 0 clé API, 0 signature HMAC, 0 fonction trade) ; daemon @reboot actif ; plan réparation M7 prêt (HTTP GET local sur 8765) ; aucun runtime modifié ; sha256 336f357fcd2879795649e99e8ca0d052f1351e4fd058e1e3f5a2d916ac11fb0d.

20260512T221843Z — REPARATION_M7_VIA_HTTP_GET_LOCAL_2026-05-12 — Bug INVALID_BUG_HARDCODE levé ; hardcodés remplacés par HTTP GET local sur collector_binance:8765 ; sha256 m7 bdb61cb6be1448d8e6484ac046952f71710571e2636d9a49e1baf943a028488d → 09dd576b47ffbd8338a7bbacc555f6c95a4578303fdc3e485cdcffcd297caca8 ; backup horodaté ; M7 reste hors cron, aucun side-effect runtime ; invariants 6×6 préservés ; sha256 acte fff321ab09fd63961270eb486b2b33963b7b2ec2d3f9ebd01b8fe489661516d6.

20260512T222117Z — ATTESTATION_FAMILLE_M_CANONIQUE_v1_2026-05-12 — Synthèse canonique 14 actes session 12 mai ; statut clarifié M3/M5/M6/M7/M8 ; M7 réparé ; 5 causes mécaniques de disparition identifiées ; chiffres marché LIVE attestés (BTC 80616, OBI 0.8035) ; daemon collector_binance 25j uptime ; plan 15 actes futurs conditionnels ; sha256 b1ff2ae077b1795c77b1dd0099940c26458de75fcdf1a6362578291faa5ad0da.

20260512T222614Z — SONDE_GENESE_CANONIQUE_M1_M2_2026-05-12 — Sonde mécanique sur l'asymétrie canonique M1/M2 vs M3/M8 (question Raphaël) ; states actuels, cron, décrets, backtests, validation interne ; verdict en attente ; aucun runtime modifié ; sha256 989248c786c5184e0581e0a2a6cb538fc85f1f0d062d0711842f17a94a5d5a7e.

20260512T222809Z — DECRET_DOCTRINE_VALIDATION_CANONIQUE_v1_2026-05-12 — Gravure doctrinale : 2 formes canoniques de validation (A mondes natifs / B walk-forward strict) ; M2 reconnu validé par Forme A ; M1 reconnu dormant ; M3/M7/M8 confirmés Forme B ; asymétrie apparente résolue ; aucun runtime modifié ; sha256 ecd85e2dcb69a3538c60f37814c03ac7046ea5e7d98d79ecabe90eb841ca35c0.

20260512T224831Z — DECRET_A8_LEVEE_PHASE_115_GRADUEE_2026-05-12 — Protocole canonique de sortie graduée de Phase 115 ; 6 paliers P0-P5 (0.0/0.1/0.25/0.5/0.75/1.0) ; conditions de passage (durée 7j + WR>=60% + DD<=5% + invariants OK + décret signé) ; conditions de retour forcé automatique ; cage non sanctionnante ; calendrier minimal 35 jours pour P5 ; aucun runtime modifié ; sha256 81164d4fc174e6883548e6e76d5b438bf52a0b50e9e943e367d801cbeb035bbc.

20260512T225021Z — TEST_M7_DRY_RUN_EXECUTION_2026-05-12 — Test ponctuel post-réparation M7 ; lecture live OBI confirmée ; m7_state.json mis à jour (1er depuis 21 jours) ; backup horodaté ; runtime hors cron préservé ; sha256 26b2f4de94fe39f406f1b4f90b07b7884d92a142a40139f33339fd0d45330066.

20260512T225305Z — SONDE_APLOMB_DEPENDANCE_TACTIQUE_2026-05-12 — Caractérisation Aplomb post-découverte M7 dependance ; localisation state + writers + lecteurs + cron + logs ; verdict en attente ; aucun runtime modifié ; sha256 d61811bb9f13a827f0eb15401d90bdff5fa66f7d8507b91507532d480684432d.

20260512T225940Z — SONDE_APLOMB_BUG_NOMINAL_CONFIRMATION_2026-05-12 — Confirmation mécanique hypothèse rupture nominale aplombstate.json vs aplomb_state.json entre tireur_aplomb et moteurs M ; ne réparer rien ce soir ; sha256 acf554d210c1e86fde586a18e73b0dddc9fc2916ca6ea14216148f10e46a7ec4.

20260512T230228Z — DECRET_DECOUVERTE_CASCADE_BUGS_APLOMB_M7_2026-05-12 — Carte mécanique d'une cascade de 4 bugs structurels rendant la pipe Aplomb→M7 inerte depuis ~2 mai ; BUG 1 rupture nominale aplomb_state.json vs aplombstate.json ; BUG 2 type permission string au lieu de float ; BUG 3 Aplomb en mode local_policy_fallback (engine canon hors cron) ; BUG 4 input bull périmé 6 jours ; plan R1-R4 + V1-V2 pour session future ; aucune réparation engagée ; sha256 2cd32d325c780fab6f659b57275ebf1deb4c6f7a5bf246ec6b6b3bb46ad6573c.

20260512T230513Z — SONDE_TIREUR_APLOMB_PERMISSION_DEFINITION_R1a_2026-05-12 — Lecture pure préparatoire à R1b ; localisation du bug type permission dans tireur_aplomb.py ; aucun runtime modifié ; sha256 fe9d65f968d5f5cc4da72018c4eec16da20c1671bdd8ae47237b061ffa7d63ba.

20260512T230740Z — REPARATION_R1_M7_CONVENTION_APLOMB_CANON_2026-05-12 — Alignement m7_micro.py sur convention canon Aplomb mai 2026 ; M1 nom fichier (aplomb_state→aplombstate) + M2 champ canon (permission→intensity) ; résout BUG1+BUG2 du DECRET_CASCADE ; sha256 m7 09dd576b47ffbd8338a7bbacc555f6c95a4578303fdc3e485cdcffcd297caca8 → ba8b063107ed77478f084135e0080c29725d923078bd41d5054f82cda3bb332a ; backup horodaté ; tireur_aplomb intouché ; M7 hors cron préservé ; sha256 acte 57fb9353e4611ddc626f1420fdb6746c192c99f646fbe56b7ac13a1d99ec7092.

20260512T231127Z — V1_TEST_M7_DRY_RUN_POST_R1_2026-05-12 — Test pratique post-R1 ; verdict mécanique sur lecture aplombstate + intensity + obi live ; sha256 8ecfaccd5c183b6238b4dd65c64945bb5d0a0d7f2773c7e86e80d70e603da4d1.

20260512T231303Z — SONDE_BUG5_M7_BASE_DIR_PATH_2026-05-12 — Découverte BUG 5 non cartographié : BASE_DIR de m7_micro.py pointe vers production/moteurs/ au lieu de la racine où vit aplombstate.json ; réparation R1bis en attente ; sha256 7a1617dd81d6a1e98d55bc3146f86d90f735eaf7f13530156bdfcd2800f2c560.

20260512T231435Z — REPARATION_R1bis_M7_SERAGONE_ROOT_2026-05-12 — Résolution BUG 5 : ajout SERAGONE_ROOT canon racine + utilisation dans load_aplomb_state ; sha256 m7 ba8b063107ed77478f084135e0080c29725d923078bd41d5054f82cda3bb332a → fb5a40d917f464930e0660c03259602bb9b2d8d5e66605ff1a7e44747baef8aa ; backup horodaté ; M7 hors cron ; sha256 acte d6e7cd74f3f912d2601a2dace815f6e63638e5058b1228a254be4c15cb24c069.

20260512T231619Z — V1bis_TEST_M7_DRY_RUN_POST_R1bis_2026-05-12 — Validation pratique post R1+R1bis ; inspection des 2 paths m7_state.json (racine + local) ; verdict mécanique automatisé fraîcheur + valeurs canon ; sha256 498dc8d2077565ea01ca4e7c778f4e8b087fa2fe6b8f02f54203ac0f3a491fa0.

20260512T231907Z — SONDE_BUG3_APLOMB_MODE_FALLBACK_2026-05-12 — Investigation du mode local_policy_fallback de tireur_aplomb.py ; comparaison 3 versions aplomb.py engine canon ; test exécution isolée de evaluate_aplomb() ; aucun runtime modifié ; sha256 a524586002cc2d92c025a1f08bfe74736ab13ea60627c4fb24b64668ae0ba56d.

20260512T232119Z — DECRET_DECOUVERTE_BUG3_APLOMB_ENGINE_FONCTIONNE_2026-05-12 — DECOUVERTE MAJEURE : aplomb.py engine canon FONCTIONNE et produit permission=0.5309 ≥ 0.5 ; tireur_aplomb.py ignore complètement l'engine et reste en local_policy_fallback ; pattern identique à M5 ; plan R4 (3 options α/β/γ) prêt pour session dédiée ; aucune réparation engagée ; sha256 2195b045f668ee958cc78ad961a249b12a175ee60464f89a03deeac2f5fea680.

20260512T232417Z — REPARATION_R4_TIREUR_BRANCHE_ENGINE_CANON_2026-05-12 — Engine canon aplomb.py branché dans tireur_aplomb.py (Option α try/except) ; intensity passe de fallback ~0.097 à canon ~0.53 ; source champ devient dynamique ; M7 peut proposer setups via Phase 115 cage decision_weight=0 ; sha256 tireur 8ce8f3cb4fd2b8a8606aa31e5b2cec77cdcafa371c25718ee85783bb7968f79a → 8da168d8fc310993b6ada0c448e1f4a325e4e880b831e887be7d33dc7b7769eb ; backup horodaté ; sha256 acte 2afabd2442be7e3e774fd09c5eac4dae73226fc5b7b9aa5c0bbe5a7d042e8922.

20260512T232746Z — SONDE_BUG4_BULL_MONDES_PARALLELES_STALE_2026-05-12 — Investigation bull state stale ~6j ; localisation files + tireurs + cron + service timer + journal + code engine canon ; aucun runtime modifié ; sha256 95384682950099a59e84e1e02233a65ab83505e9de7414b1136eca7c731f5bac.

20260512T233057Z — SONDE_BUG4_PIPELINE_INPUT_MONDES_2026-05-12 — Investigation pipeline d'input mondes_paralleles ; identification CSV input + scripts collecteurs + crons + événements systémique 5-7 mai ; aucun runtime modifié ; sha256 fdede112e62509b5bde147b2202603c24f1e06edf63630300a697d9a87fae881.

20260513T084236Z — SONDE_BUG4_R5a_VRAI_INPUT_BLOQUANT_2026-05-12 — Identification du CSV bloquant t_last au 6 mai parmi candidats (btc, seragone_4117j, dxy, sp500, eth) ; check update_data.py vs mondes_paralleles_engine reads ; sha256 3f11a098b86dd41439295855cb28dd62e692996faf62438eaf223534a2569ca6.

20260513T084743Z — SONDE_BUG4_R5b_WRITER_SERAGONE_4117J_2026-05-13 — Sonde finale identification writer seragone_4117j_complet.csv : compute_ec_daily.py vs autres ; pourquoi stale depuis 6 mai ; check logs eclaireurs + cron ; sha256 3424ea299afd7e2c7d5be54eea588b9452a98c42209dba962aca2c091f2be729.

20260513T085106Z — SONDE_CARTOGRAPHIE_META_MOTEURS_2026-05-13 — Sonde doctrinale fondamentale : matrice canonique de 18 moteurs (EXISTS/CRON/TIMER/IN_META/IN_INDEX) ; révèle outils orphelins type regenerer_complet_canon.py producteurs de matière canon mais hors orchestration ; questionne D11 ; sha256 21cd94b33e8d2f9b1f86abe3d81717d1e93191b521bb6fabb5b15641d93b29ca.

20260513T090935Z — REPARATION_R5_REGENERER_CANON_2026-05-13 — Exécution manuelle regenerer_complet_canon.py pour rafraîchir seragone_4117j_complet.csv stale depuis 6 mai ; verdict FAILED ; sha256 602401b900701c9e06f4caa73eba1a6e3b6da1ffe395c0b029f84438278d0415.

20260513T091146Z — REPARATION_R5bis_ALIGNMENT_NOMMAGE_2026-05-13 — Copie data/seragone_4126j_complet_canon.csv → seragone_4117j_complet.csv ; alignement writer/reader ; verdict PARTIAL ; sha256 f70ff46db8df3c2a039bed92386ca38c75a36a720d7075cc4b1f63ef1a964aa9.

## ATTESTATION_P2_LECTURE_CANONIQUE_A4_A7_ZETA1_2026-05-11
- sha256 422357d3b076d03fabf675880ebe2c0859792f2d1de599b2c2065a14077dc2cf
- date_UTC 2026-05-11T215600Z
- chantier_zeta1 RESOLU CARTOGRAPHIE 12.C
- lecture_canonique_formelle A4 A5 A6 A7 + annexes

## ATT_PHASE_O_B_LECTURE_MONDES_20260514T190838Z
- sha256 ed011ad6239d06e3e166f5c69054fdbf543759a0e03ac87137e9e0b9dfc4818a
- date_UTC 2026-05-14T19:08:38Z
- chantier_phaseOB SCELLE 3 modules mondes
- verdict 1 voix sur 9 sur input stale 8j
- dettes_capitalisees D93 a D129 (37)

## GAMMA_4_DIAGNOSTIC_UPSTREAM_20260514T191441Z
- sha256 5f895f786b2e192a3065d86a9ff064764cb35e7692e4ba162584276b64b06c31
- date_UTC 2026-05-14T19:14:41Z
- chantier_gamma4 RESOLU diagnostic, correctifs differes
- cause_racine cryptoquant_scraper 593h + fix_virgules one-shot
- dettes D137 a D142 (6)

## GAMMA_8_INVARIANTS_5_SUR_6_20260514T192438Z
- sha256 a4084c96ed6cf892400445fda9cb313ad341e1560fc58821c1652cacac351099
- date_UTC 2026-05-14T19:24:38Z
- chantier_gamma8 RESOLU 5/6 TENUS 1 PATCHE LEGITIME
- patch_money_manager garde-fou stale 3600s sur 3 load_state
- INDEX ligne 95 mise à jour : sha 4760b99c -> f9b1580c
- dettes capitalisees D152 D154 D156 D157

## ALPHA_3_FINAL_CHRONOLOGIE_4117J_20260514T193125Z
- sha256 702660e6a3a49552df96f8b32e0e63f98b07e433efdd5e5e63e8e9646afa2787
- date_UTC 2026-05-14T19:31:25Z
- chantier_alpha3final FERMEE complete
- chronologie 3 sha 4ccfbd0a -> b216c149 -> 0e3adcbb
- aucune violation doctrinale, INDEX cohérent
- chaine logique R5b -> R5_FAILED -> R5bis_PARTIAL -> γ4 -> α3final
- dettes D158 D166_RETIREE D169 D170 D171 D172

## R5TER_TRACE_FAILED_LUE_20260514T193556Z
- sha256 9c7db892642f4ab4916aebac6b29678330ad7bc1abcf58d523b8e5c4fd799b32
- date_UTC 2026-05-14T19:35:56Z
- chantier_R5ter FERMEE — fermeture parfaite alpha3final
- R5_FAILED qualifié constat doctrinal pas crash technique
- R5bis_PARTIAL canon 4126j contient zéros heritage upstream
- SP500 gelé 17 mars 2026 (57j, pas 25j) — D175
- pyramide 6 niveaux cassure D177
- chaîne 13 mai -> 14 mai 7 actes canoniques attestés
- dettes D173 D174 D175 D176 D177 D178

## R7_R10_SYNTHESE_PRODUCTEUR_CSV_18D_20260514T195659Z
- sha256 c041f7fc96148e4542b9e8f5481b96a7fdd5cea3b39d871caabfd06fedc541a0
- date_UTC 2026-05-14T19:56:59Z
- chantier_R7_R10 FERME — cause structurelle isolée
- CSV 18D gelé 2026-05-06, sha a8ddf77e...
- 4144 lignes, 8 jours manquants 7→14 mai
- producteur automatisé absent, dernière reconstruction manuelle
- voie A4-robuste retenue, R12 squelette validé
- dettes D183 D184 D185 D186 D187 D188

## R15bis_PRODUCTEUR_18D_INTROUVABLE_DOCTRINALEMENT_20260514T201552Z
- sha256 dfb102d37c9e8f7a8ab023a01766b600fb656ce0fdae15d36bac16b8fe1ed672
- date_UTC 2026-05-14T20:15:52Z
- chantier_R15bis FERME — producteur 18D introuvable doctrinalement
- aucun to_csv vers sous_signaux_18_complet dans repo actif
- toutes compute_*_v2 retournent float agrege
- hypothese : script jetable 6 mai non conserve
- voies A1bis et A4 invalidees, survivantes A5/A5bis/A6
- decision reportee a Raphael a froid
- dettes D203 D204 D205 D206 D207

## DECRET_Q6_SOCLE_M0_M8_2026-05-15
- sha256 da45a2b948bdbbee10c58cd388f418db8f6ea9fadec20b601dafc8b4e975432b
- date_session 2026-05-15T02:12:00+02:00
- date_disque  2026-05-15T07:52:19Z
- statut DECIDE lecture seule
- 8 articles socle M0-M8
- doctrines empilees R1 VALIDATED!=INSTALLED Doctrine7 Genealogie

## AMENDEMENT_Q6_ARTICLE_5_RECTIFICATIF_2026-05-15
- sha256 021738100490f7477102a5a324f08284435672866248277e6bac08910585b995
- date_UTC 2026-05-15T07:52:40Z
- statut RECTIFICATIF empilement non reecriture
- P1-P19 fraiches mtime 14 mai, P20-P51 figees mtime 4 mai
- cause rollback 27/04 19:06 UTC
- question ouverte mtime 4 mai vs rollback 27 avril inscrite

## AMENDEMENT_A2bis_FERMETURE_QUESTION_OUVERTE_20260515T075815Z
- sha256 83838d809db97c05e1bcdfc3e17fab80c31f25da13a60ec88389129036636e56
- date_UTC 2026-05-15T07:58:15Z
- statut FERMETURE par sonde froide S1
- 4e violation VALIDATED != INSTALLED documentee (30/04 22:25 UTC)
- crontab actif 15/05 = 200 lignes, sha 3fb36dcfefaabd5f..., 0 P20-P51
- dette D192 mutations post-10/05 20:46 non documentees

## AMENDEMENT_A5_FERMETURE_D192_20260515T080144Z
- sha256 c0bb1219fe228fe74672234c88929a6c9009fb64ee7b3df364f760626f880c7f
- date_UTC 2026-05-15T08:01:44Z
- statut FERMETURE par sonde froide S2
- D192 fermee : 21 miroirs cosmetiques + 2 ajouts cockpit + 2 reactivations A7
- Aucune violation VALIDATED != INSTALLED
- D193 tracer decrets tools/seragone_one.py et SERAGONE_ONE_TOTAL.sh

## AMENDEMENT_A6_FERMETURE_D193_20260515T080619Z
- sha256 468bbab2d023aff2432a0a04680bd1bffaef54690aecffdfd23f567f6ef1af78
- date_UTC 2026-05-15T08:06:19Z
- statut FERMETURE par sonde froide S3
- D193 fermee : decret grave_22_seragone_one_v1_20260511T203916Z trouve
- 2 modules lecture seule absolue, aucune violation
- D194 clarifier audit/decisions/ vs audit/grave_*/ inscrite

## ATTESTATION_A7_DIAGNOSTIC_R13c_20260515T081007Z
- sha256 a49261b668bfe9ccd9f82f97ed461083a65d25879fb491fc2a34e4659ec7d810
- date_UTC 2026-05-15T08:10:07Z
- statut DIAGNOSTIC, chantier 18D maintenu en pause Article 8 Q6
- cause majeure : input data/btc_daily.csv reecrit quotidiennement
- v2 conceptuellement correct, echec vient de l'input pas du code
- D195 archivage horodate inputs inscrite, sonde S5 future

## RECTIFICATIF_A8_RECADRAGE_R13c_PAR_ARCHEOLOGIE_20260515T081712Z
- sha256 e1aa403e3d7504a9891692677836ab418063ed736bb8b865d147d5ec24ac4f95
- date_UTC 2026-05-15T08:17:12Z
- statut RECTIFICATIF, recadre A3 et A7 par archeologie complete
- Reference chaine canonique : R5bis (13/05) + R13c-R14-R14bis-R15bis (14/05) + CLOTURE_VOIE3PRIME (11/05)
- Doctrine 26 mars 'NE BRANCHE RIEN' reaffirmee
- D195 redirigee vers chaine canonique anterieure, NON inscrite comme dette nouvelle
- D196 lecon canonique : relire INDEX_CANON avant tout amendement R13c/C1/Bascule
- Sonde S8 et patch v2 ANNULES

## DECRET_A9_REGULARISATION_COLLISION_D195_D196_20260515T082210Z
- sha256 79d07cc1d81f884059d62626e0fde913330e41d7a03d99c304e23e18281a2399
- date_UTC 2026-05-15T08:22:10Z
- type DECRET regularisation pure modele Q2/Q3 du 10 mai
- D195 d'A7 renumerotee en D203, D196 d'A8 renumerotee en D204
- D195 et D196 reservees par R14 (14/05) conservees canoniquement
- D194 reconnaissance partielle par DECISION_INDEX_CANON_NON_EXHAUSTIF (12/05)
- pattern amendement interpretatif 30/04 cite pour conformite future
- D205 nouvelle inscrite : audit coherence retroactive numerotation
- A7 et A8 conserves intacts sur disque (empilement, jamais effacement)

## DECRET_A9bis_RECTIFICATIF_COLLISION_TRIPLE_20260515T082444Z
- sha256 1114d3b8ab3c79edea5c475ad044f3312850078a54ec9a0763a85ad1a6f02266
- date_UTC 2026-05-15T08:24:44Z
- type RECTIFICATIF de A9 par sonde S10 archeologique
- A9 avait cree triple collision D203/D204/D205 vs R15bis 14/05 ligne 441
- D195 d'A7 -> D208 (premier libre verifie), D196 d'A8 -> D209, audit numerotation -> D210
- D203 D204 D205 D206 D207 reservees par R15bis preservees
- chaine canonique Q1->Q6 reconnue (A1 ce matin = DECRET_Q6)
- D211 lecon canonique meta : sonde retrospective dans session de gravure
- A9 conserve intact sur disque (empilement, jamais effacement)

## ATTESTATION_A10_CLOTURE_HONNETE_SESSION_15MAI_20260515T082757Z
- sha256 de2b348778a58272740ec35d1ea66e031b258363388887b9722ddb51816f133e
- date_UTC 2026-05-15T08:27:57Z
- type ATTESTATION cloture session lucide
- 10 actes graves, 10 sondes froides, 6 erreurs archeologiques rectifiees
- 0 patch runtime, 0 module touche, 0 crontab modifie
- A9bis NON confronte par sonde retrospective, audit reporte session future
- D212 inscrite : audit retrospectif A9bis par session future reposee
- agent reconnait myopie archeologique structurelle
- canon Seragone intact 64 jours preserves

## RECTIFICATIF_PERPLEXITY_SESSION_15MAI_MATIN_20260515T090818Z
- sha256       8548df510f1fb30ade10e2999d32c8848c7b214806947423cce9f432e77b4b08
- date_UTC     2026-05-15T090818Z
- nature       rectificatif erreurs Perplexity 09h00-11h00 CEST
- empilement   E1 a E6 nommees, aucune reecriture
- ne touche ni Q6 socle ni R13c ni R14 suspendue

## DECRET_Q6_SOCLE_M0_M8_2026-05-15
- sha256       f48b8ae8b12fdaf8625bd65eee9151474006bed9d208935c77daa771085f7a14
- date_session 15 mai 2026 02:12 CEST
- date_disque  2026-05-15T091033Z
- 8 articles socle M0-M8, mondes derives, META observation, D7

## AMENDEMENT_Q6_ARTICLE_5_RECTIFICATIF_2026-05-15
- sha256       06066b86fa9d12dfa86889877c356fc1e110d3771512de68229306d071ffb35c
- empilement P1-P19 vivantes / P20-P51 figees 4 mai
- D300 writer mondes_paralleles_state.json non identifie

## ATT_D300_RESOLUE_TIMER_PARALLELES_VIVANT_2026-05-15
- sha256       67885ad5ff7a01436abb3fe3822b6b860793bd7043e63df6304ef135fb3cc1b9
- date_disque  2026-05-15T091127Z
- nature       attestation mecanique, D300 close
- constat      timer systemd seragone-mondes-paralleles ACTIF
                + timer multivers ACTIF
                + loop bash run_mondes_one_shot_loop.sh PID 2519871 depuis 9 mai
- contradiction STATUS_PAUSE 6 mai documentaire, jamais materialise runtime
- doctrine 7  intacte decision_weight_real=0.0

## R14_PARTIELLEMENT_RESOLU_MOTEUR_PARALLELES_2026-05-15
- sha256       3e4d84f9f6700a32b0c60305152f5acfd51c34f6a3762e08675002e675d85826
- date_disque  2026-05-15T091616Z
- producteur_states  mondes_paralleles_engine.py 3f834b1f88...
- producteur_CSV_18D NON IDENTIFIE - reste ouvert
- CSV soussignaux18complet.csv  ABSENT racine
- stack_runtime  ENTIEREMENT VIVANTE (contradicte STATUS_PAUSE)

## A5_AMENDEMENT_R14_NOM_CANONIQUE_CSV_2026-05-15
- sha256       d4232ee436c87b77d3d3e1b5a5d098cea686f656951ce55441fd388380b499ee
- date_disque  2026-05-15T091814Z
- E7 nommee    sous_signaux_18_complet.csv (avec underscores)
- localisation /home/ubuntu/seragone/sous_signaux_18_complet.csv
- sha_csv      a8ddf77ec31b03fac640d97bc7b3255d6696796e93492945378b1450c751d5b3
- 19 colonnes  pas 18 (index + 18 signaux probable)
- nettoyage    6 mai 12:54 dates vides (-30Ko)

## ATTESTATION_STALEINPUT_18D_OPERATIONNEL_20260515T184623Z
- dateUTC : 2026-05-15 1846
- fichier : audit/ATTESTATION_STALEINPUT_18D_OPERATIONNEL_20260515T184623Z.md
- sha256 : 6ff50efc81387802f5cc3cb9703fe0d2331e8f7ea32096ffc61e8d9dccc595d9
- statut : attestation documentaire froide, lecture seule
- objet : état opérationnel stale_input des mondes parallèles au 15 mai 2026
- CSV 18D : /home/ubuntu/seragone/sous_signaux_18_complet.csv sha a8ddf77e...
- state : stale_input true, input_lag_days 9, date 2026-05-06
- garde-fous : aucune activation, aucun patch runtime, aucun timer touché
- continuité : R15bis producteur 18D introuvable doctrinalement préservé

## DECRET_A7_3_SEMANTIQUE_NEUTRAL_POSITION_DEMO_2026-05-15
- sha256       3eefcc21f9b1250222d30339bea7f81ba01008a0d13c8df16607fd2fcc0a1961
- date_disque  2026-05-15T192500Z
- fichier      auditdecisions/DECRETA73SEMANTIQUENEUTRALPOSITIONDEMO2026-05-15.md
- type         DECRET SEMANTIQUE LECTURE SEULE
- objet        NEUTRAL finale 0.0 signifie TARGET_FLAT
- cas A7.3     target=0, ledger_net=-0.081 BTC SHORT, PnL latent net estime 126.42 USD
- semantique   CLOSE_TO_FLAT candidat, etat operationnel HOLD_READONLY
- interdits    aucun ordre, aucun runtime, aucun cron, aucun module Python, aucun state, aucune finance reelle

## ATTESTATION_A7_3_PNL_LATENT_POSITION_DEMO_NON_CLOSE_2026-05-15
- sha256       4bde904ccda8a6b8dff8c05fa48267ba43a8ee79d3933453ac0d22ed45cceb40
- date_disque  2026-05-15T192500Z
- fichier      auditdecisions/ATTESTATIONA73PNLLATENTPOSITIONDEMONONCLOSE2026-05-15.md
- type         ATTESTATION LECTURE PURE
- mesure       89 executions FILLED_DEMO, short total 0.085 BTC, buy total 0.004 BTC
- position     ledger demo net -0.081 BTC SHORT
- prix_spot    79105.64
- prix_moyen_short 80711.11 USD
- pnl_latent_net_estime 126.42 USD
- divergence   cible Money Manager flat / ledger demo short ouvert
- suite         sonde froide faisabilite CLOSE avant tout decret d'activation

## INDEXATION_A73_NEUTRAL_POSITION_DEMO_20260515T193822Z
- sha256       8735c3bfbf7bea974dcf11298341b2965ea8886710d63f9a3830f685db3fa895
- date_UTC     20260515T193822Z
- fichier      auditdecisions/INDEXATIONA73NEUTRALPOSITIONDEMO20260515T20260515T193822Z.md
- nature       indexation documentaire post-0quinquies
- garde_fous   aucun runtime touche, aucun cron touche, aucune activation

## RECTIFICATIF_R4_POSITION_DEMO_NETTE_LEDGER_PRIME_2026-05-15
- reference    RECTIFICATIFR4POSITIONDEMONETTELEDGERPRIME
- sha256       9fe0fb0afe2f2699b62f27e2277a09ebda905b9f97b42b40077cd686bd5aa6f0
- taille       5047
- date_disque  2026-05-15T19:59:34Z
- fichier      auditdecisions/RECTIFICATIFR4POSITIONDEMONETTELEDGERPRIME_20260515T195934Z.md
- type         RECTIFICATIF DOCUMENTAIRE PUR
- portee       MODE_DEMO_TOTAL uniquement
- objet        ledger net reconstruit depuis executions demo prime sur position_after_demo broker
- contexte     A73 / R3, TARGETFLAT, ledger demo net -0.081 BTC, candidat froid BUY 0.081 BTC
- garde_fous   aucune activation, aucun ordre, aucun runtime, aucun cron, aucun module Python, aucun state, aucune finance reelle
