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
- money_manager.py           = 4760b99cf257c5e89f3e056fb0c3e9ab5bf35c0bfb51cc3b5a441737a0ee96d9
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
