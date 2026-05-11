# DECRET Q5 — INSCRIPTION_CANONIQUE_META_ET_RESOLUTION_D11

**Identifiant** : Q5
**Date** : 2026-05-11 ~09:15 UTC
**Producteur** : Raphaël Boussy + Assistant IA
**Statut** : ACTIF
**Portée** : documentaire pure (0 modification runtime Python, 0 modification shell)

## §1. OBJET
Q5 régularise canoniquement le moteur META sur VPS et résout D11 entre les deux
meta_controller.py. Aucune modification code/shell/service.

## §2. PIÈCES PROBANTES
- DOCTRINE VISION canon/DOCTRINE_MOTEUR_META_SERAGONE.md hash 00daf21727f8281a853f09f9b82d98f7fefe60efaa00403ae012799e1ee7eb3b
- BLUEPRINT audit/meta/META_GLOBAL_ENGINE.md v1.1 hash 1f6c60575b8c253ed9c8be3ece4dcd4c74c61a8ecb0c4cdf3c47e9d2464e97f4
- AMENDEMENT A4 hash 236dc3875823865753ce3bfdb02d3ffeffb401b351f1fea4dd89e533e159976d
- meta_state.json c0699b472feaea442b3cbfef6926faaecdce725fe1b4e086afd07a8f271c6151
- states/meta_config.json e61f206a5ad5709b4286dddc917ec21e41227af9b3fae46e34a177b5c1a650f3

### 2.2 Preuve collision D11
orchestrateur.sh l.170 appelle production/allocation/meta_controller.py
production/meta/meta_controller.py n'est appelé par aucun shell.

## §3. DÉCISION CANONIQUE
### 3.1 Blueprint promu BLUEPRINT_CANONIQUE_ACTIF (statut opé OBSERVATOIRE_STADE_1, Stades 2-3 VERROUILLÉS)
### 3.2 Les 6 modules production/meta/ inscrits au registry
### 3.3 Résolution D11 SANS RENOMMAGE :
  - production/meta/meta_controller.py = META_CONTROLLER_CANON (non câblé, Stade 2+ verrouillé)
  - production/allocation/meta_controller.py = PERF_WEIGHT_CONTROLLER (alias shell meta_controller, appelé orchestrateur.sh l.170)
### 3.4 Rectification doctrinale douce : la phrase VISION l.118 désigne perf_weight. VISION non modifiée.
### 3.5 A4 confirmé ACTIF post-Q5.
### 3.6 Extension MONDES reportée à décret ultérieur.

## §4. INVARIANTS 6x6 préservés (cf. trace).
## §5. POSTURE L99 + OODA + D7§4 + D9 + D11.
## §6. SIGNATURE Raphaël Boussy + Assistant IA, 2026-05-11.
