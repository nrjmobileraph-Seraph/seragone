# CONTROLE MULTIMONDES V1Z-Y-TER — PHASE 1-TER 27D SANDBOX LAYOUT FIX

Date UTC : 2026-05-05T23:05:03Z
HEAD : ecdaa401df1e1972fd972d73e48784baf4a8418f
Ancrages : V1ZZ-bis (ecdaa401) / V1ZZ (717f9c8c) / V1ZY-bis (cd39ea2b) / V1ZY (ad7afa27) / V1ZX (b2cca117) / V1ZW (4f2a18c3)

## 1. Nature du document

Phase 1-ter du decret V1ZX. **Correctif layout sandbox uniquement**, aucune execution. Suite a echec V1ZZ-bis (FileNotFoundError sur `historique_27eq.csv` ligne 14 du script), V1ZY-ter ajoute les 2 CSV directement a la racine sandbox via `cp -p` depuis `inputs/`, sans modifier `inputs/` ni le script. Le layout final permet au script de trouver les fichiers via les litteraux simples `pd.read_csv('...csv')`.

## 2. Verdict V1ZY-ter

**V1ZYTER_PHASE1TER_27D_LAYOUT_OK_PRET_V1ZZTER**

Layout sandbox corrige : 2 CSV ajoutes a la racine sandbox (cp -p depuis inputs/ vers racine), sha256 verifies identiques, 0 symlink, caches live identiques avant/apres. inputs/ preserve intact. Sandbox prete pour V1ZZ-ter qui ne touchera plus au layout.

## 3. Cause origine confirmee mecaniquement

Lecture du `stderr_full_v1zzbis.log` :

```
File ".../sandbox_27d_reexec/test_27d_4approches.py", line 14, in <module>
    hist = pd.read_csv('historique_27eq.csv')
FileNotFoundError: [Errno 2] No such file or directory: 'historique_27eq.csv'
```

Le script utilise un chemin simple (sans prefixe `inputs/`), donc cherche dans `cwd` qui est la racine sandbox. V1ZY avait place les CSV dans `sandbox/inputs/`. Le correctif consiste a doubler la presence des CSV (racine + `inputs/`) plutot que deplacer.

## 4. Operation V1ZY-ter

| Source | Destination | sha256 | Taille |
|---|---|---|---|
| `sandbox_27d_reexec/inputs/historique_27eq.csv` | `sandbox_27d_reexec/historique_27eq.csv` | `550c948a5339e0483a0aa9d286ff2295e9bf0d2fc08fc1b628ad4cf6f4a045d8` | 1836199 |
| `sandbox_27d_reexec/inputs/couches_123_daily.csv` | `sandbox_27d_reexec/couches_123_daily.csv` | `ae7def2ecce126d13e5a3a82f316cb126e963f9813f1e495f5d5a4ea11651fec` | 239888 |

- Methode : `cp -p` (preservation mtime, copie physique)
- `inputs/` preserve intact (philosophie : on ajoute, on n efface pas)
- 0 symlink dans toute la sandbox
- sha256 racine == sha256 inputs verifie pour les 2 CSV

## 5. Layout sandbox final

```
  couches_123_daily.csv                                        size=    239888  sha256=ae7def2ecce126d13e5a3a82f316cb126e963f9813f1e495f5d5a4ea11651fec
  historique_27eq.csv                                          size=   1836199  sha256=550c948a5339e0483a0aa9d286ff2295e9bf0d2fc08fc1b628ad4cf6f4a045d8
  inputs/couches_123_daily.csv                                 size=    239888  sha256=ae7def2ecce126d13e5a3a82f316cb126e963f9813f1e495f5d5a4ea11651fec
  inputs/historique_27eq.csv                                   size=   1836199  sha256=550c948a5339e0483a0aa9d286ff2295e9bf0d2fc08fc1b628ad4cf6f4a045d8
  test_27d_4approches.py                                       size=     14220  sha256=2debd5d63c04d64ca8311e7f316c282e5c1ba32b2ced8056334b9bd9364ae36f
```

Verification : 5 fichiers (1 script + 2 CSV racine + 2 CSV inputs/), 0 symlink.

## 6. Attestation non-pollution

- `hashes_live_avant_phase1ter.sha256` snapshot caches live AVANT
- `hashes_live_apres_phase1ter.sha256` snapshot caches live APRES
- `diff_phase1ter.txt` strictement vide
- Aucun cache live touche
- Aucun broker, cron, systemd, ecriture live
- vrais_yeux.py INTOUCHABLE
- Phase 115 preservee, decision_weight=0.0

## 7. Artefacts V1ZY-ter

| Fichier | Role |
|---|---|
| CONTROLE_MULTIMONDES_V1ZYTER_PHASE1TER_27D_SANDBOX_LAYOUT_FIX.md | ce document |
| manifest_v1zyter.json | metadonnees machine-readable |
| hashes_live_avant_phase1ter.sha256 | snapshot caches live AVANT |
| hashes_live_apres_phase1ter.sha256 | snapshot caches live APRES |
| diff_phase1ter.txt | diff caches (DOIT etre vide) |
| sandbox_layout_before_v1zyter.txt | inventaire layout sandbox AVANT |
| sandbox_layout_after_v1zyter.txt | inventaire layout sandbox APRES |
| sandbox_layout_sha256_v1zyter.txt | sha256 complet sandbox APRES |

Plus 2 fichiers ajoutes en sandbox :

| Fichier | Source |
|---|---|
| sandbox_27d_reexec/historique_27eq.csv | cp -p depuis inputs/ |
| sandbox_27d_reexec/couches_123_daily.csv | cp -p depuis inputs/ |

## 8. Posture finale

Sandbox prete pour V1ZZ-ter. Apres commit/push V1ZY-ter et relecture, Raphael devra deposer une nouvelle signature `phase2ter_signed.txt` puis demander explicitement V1ZZ-ter qui combinera : env compat V1ZZ-bis (PYTHONPATH user-site) + layout sandbox V1ZY-ter (CSV a la racine).

D12 candidate : V1ZY-ter = VALIDATED (correctif layout) != INSTALLED != PRODUCTION_ACTIVE.

---

*Posture L99 + OODA stricte maintenue.*
*Aucune execution. Raphael voit. Claude calcule.*