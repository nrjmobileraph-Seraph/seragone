# ACTE 26 — Position canonique MOTEUR META (Stades 1/2/3) + déclassement legacy state

**Date (UTC)** : 2026-05-11T21:07:29Z
**Hash univers pré-acte** : `4d3aec8db73484ca`
**Session** : reprise du fil MOTEUR META après digression SERAGONE_ONE V1 → A7

## 1. Exposé

Suite à la découverte que le chantier MOTEUR META était le véritable fil
interrompu avant les actes 22-25, cet acte grave la POSITION CANONIQUE
actuelle des trois stades tels que définis par la Doctrine
(DOCTRINE_MOTEUR_META_SERAGONE.md, 28 avril, sha `00daf21727f8281a…`)
et le Blueprint (META_GLOBAL_ENGINE.md v1.1, 28 avril,
sha `1f6c60575b8c253e…`), et respecte strictement DECRET Q5
(`c451c31697aec918…`) qui verrouille les Stades 2-3.

## 2. Position canonique par stade

| Stade | Rôle doctrinal | État runtime | Respect Q5 |
|---|---|---|---|
| **1 OBSERVATOIRE** | mesurer, diagnostiquer, garder mémoire | ✅ ACTIF : mondes_autonomes (4 Phi), multivers (191×8), perf_weight | ✅ |
| **2 CROISEMENT/ASSIMILATION/PROJECTION** | faire émerger lecture cohérente | ⏳ VERROUILLÉ | ✅ respecté |
| **3 SOLLICITATION CRÉATION** | détecter manque, demander module | ⏳ VERROUILLÉ | ✅ respecté |

## 3. Preuves runtime Stade 1

- mondes_autonomes.py : 4 mondes Phi (Rythme, Anti-V, Persistance, Rebond),
  cycle ~60s, écrit dans `states/mondes_autonomes_state.json`,
  log `logs/mondes_autonomes.log` (1.37 Mo, frais à T-3min)
- seragone-multivers.service : 191 mondes × 8 couches, timer oneshot,
  log `logs/multivers.log` (200 Ko+, frais 20:49)
- perf_weight_controller : `production/allocation/meta_controller.py`
  appelé par `orchestrateur.sh l.170`, alimente `states/meta_config.json`
  (poids moteurs, bonus_confiance, qualificateurs_actifs)

## 4. Déclassement legacy state

Le fichier `states/mondes_paralleles_state.json` (38 octets, 23 avril,
`{n_actif: 0, n_gp_actif: 0}`) est NON MIS À JOUR depuis 18 jours.
Cause : le runtime écrit désormais dans `mondes_autonomes_state.json`.

Décision : renommage (pas suppression) en
`mondes_paralleles_state.LEGACY_OBSOLETE_20260423.json`, remplacé par
un marker explicite. Aucun script runtime impacté (référence legacy
uniquement dans backup/research copies).

## 5. Chantier stade 2/3 — futur

Déverrouillage stades 2-3 = chantier de conception dédié, APRÈS la démo.
Q5 §3.1 reste en vigueur jusqu'à gravure d'un DECRET_Q6_DEVERROUILLAGE.

## 6. Liens avec actes 22-25

- Acte 22 SERAGONE_ONE : connaissance totale incluant DOCTRINE_MOTEUR_META
- Actes 23/23-bis : réactivation multivers = STADE 1 observatoire
- Acte 25 : pipeline A7 end-to-end = consommateur aval du stade 1
  (via meta_config.json → money_manager → decision_to_order)

## 7. Successeur

ACTE 27 — Attestation DOCTRINE_7_v2 MODE_DEMO_TOTAL opérationnel
(pré-requis final avant démo).
