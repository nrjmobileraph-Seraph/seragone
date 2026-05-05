# CONTROLE MULTIMONDES V1Z-Y-BIS — CROSSCHECK 27D DEPENDANCES

Date UTC : 2026-05-05T22:45:30Z
HEAD au lancement : ad7afa278a3eb394ca3a457645682b0b45a138b3
Ancrages : V1ZY (ad7afa27) / V1ZX (b2cca117) / V1ZW (4f2a18c3) — tous ancetres verifies

## 1. Nature du document

Crosscheck **lecture seule pure** des dependances de `test_27d_4approches.py` contre l ecosysteme 27D voisin de l arbre racine. Aucune execution. Aucun import. Aucun cp/mv hors auditactionsv1. Aucun touch caches live. But : verifier mecaniquement qu aucun fichier 27D voisin n est utilise par le script avant que V1ZZ ne lance le subprocess sandbox.

## 2. Verdict V1ZY-bis

**V1ZYBIS_27D_OK_DEPENDANCES_FERMEES_PRET_V1ZZ**

Seules historique_27eq.csv et couches_123_daily.csv apparaissent en litteral. Aucun voisin 27D trouve en litteral, en import, ni atteint dynamiquement. Aucun pattern glob/listdir/rglob/iterdir/walk dans le script. Sandbox V1ZY suffisante pour V1ZZ.

## 3. Methode

- `ast.parse` + `walk Constant str` -> extraction litteraux str
- `ast.parse` + `walk Import/ImportFrom` -> extraction imports
- `grep -nE` cible sur le seul script, 3 axes : ecosysteme 27D, patterns dynamiques (glob/pathlib/listdir/walk/rglob/iterdir/fnmatch), extensions et fonctions de lecture (open, read_csv, read_json, json.load, pd.read, np.load)
- Classification par fichier : DEP_CERTAINE_LITERAL / DEP_PROBABLE_IMPORT / DEP_POSSIBLE_DYNAMIC / NON_LOCALISE_PAR_GREP_AST_CIBLE

## 4. Resultats AST

| Mesure | Valeur |
|---|---|
| Litteraux str detectes | 205 |
| Imports detectes | 5 |
| Modules top-level importes | datetime, json, numpy, pandas, warnings |
| Patterns dynamiques detectes (reels) | (aucun) |
| Patterns dynamiques (tous, incl. import pathlib) | (aucun) |

## 5. Matrice de dependance — synthese

| Categorie | Fichier | Classification | Deja copie V1ZY |
|---|---|---|---|
| input_v1zy_copie | `couches_123_daily.csv` | **DEP_CERTAINE_LITERAL** | OUI |
| input_v1zy_copie | `historique_27eq.csv` | **DEP_CERTAINE_LITERAL** | OUI |
| voisin_27d | `banc_27d_enrichi_v4.csv` | **NON_LOCALISE_PAR_GREP_AST_CIBLE** | non |
| voisin_27d | `calculer_couches_123_5min.py` | **NON_LOCALISE_PAR_GREP_AST_CIBLE** | non |
| voisin_27d | `generer_historique_27eq.py` | **NON_LOCALISE_PAR_GREP_AST_CIBLE** | non |
| voisin_27d | `mondes_27d_constructeur.py` | **NON_LOCALISE_PAR_GREP_AST_CIBLE** | non |
| voisin_27d | `mondes_27d_definitions.json` | **NON_LOCALISE_PAR_GREP_AST_CIBLE** | non |
| voisin_27d | `mondes_27d_resultats.json` | **NON_LOCALISE_PAR_GREP_AST_CIBLE** | non |
| voisin_27d | `mondes_27d_v2.py` | **NON_LOCALISE_PAR_GREP_AST_CIBLE** | non |
| voisin_27d | `mondes_27d_v2_resultats.json` | **NON_LOCALISE_PAR_GREP_AST_CIBLE** | non |
| voisin_27d | `provinces_27d_live.py` | **NON_LOCALISE_PAR_GREP_AST_CIBLE** | non |
| voisin_27d | `provinces_thresholds.json` | **NON_LOCALISE_PAR_GREP_AST_CIBLE** | non |

Detail complet : `dependency_risk_matrix.tsv`.

## 6. Synthese par classe

- Voisins 27D dep certaine/probable NON copies : 0 -> (aucun)
- Voisins 27D dep possible dynamique : 0 -> (aucun)
- Inputs V1ZY certains (litteral) : 2 -> couches_123_daily.csv, historique_27eq.csv

## 7. Contraintes canoniques rappelees

```
Phi*_CANON   (figé 16 avril 2026)  : (M:0.28, V:0.33, S:0.26, H:0.26, G:0.42)
W_CANON                            : (M:1.80, V:1.25, S:1.20, H:1.42, G:1.10)
Capital paper                      : 35 000 EUR
Cible exchange                     : Kraken (paper, decision_weight=0.0)
Phase actuelle                     : 115 LIVE_TEST_TOTAL_EN_CAGE
Modules INTOUCHABLES               : vrais_yeux.py, vrais_yeux_stretched.py, village_le_vrai.py
```

Aucune valeur n a ete touchee par V1ZY-bis.

## 8. Posture finale

Sandbox V1ZY suffisante pour V1ZZ. Apres commit/push V1ZY-bis et relecture, depot signature `phase2_signed.txt` dans le REEXEC_DIR V1ZY puis redaction V1ZZ_PHASE2_27D_EXEC.

D12 candidate : V1ZY-bis = VALIDATED (audit) != INSTALLED != PRODUCTION_ACTIVE.

---

*Posture L99 + OODA stricte maintenue.*  
*Aucune execution. Raphael voit. Claude calcule.*