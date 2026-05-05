# AMENDEMENT V1Z-Q-BIS — DURCISSEMENT DU DECRET V1ZQ AVANT SIGNATURE PHASE 1

Date UTC: 2026-05-05T20:30:35Z

Mode: amendement nominal documentaire. On ajoute, on n efface rien. V1ZQ original reste committe tel quel. Cet amendement rend explicites quatre durcissements et une variation acceptee, afin que la signature Phase 1 ne se fasse pas sur un texte trop souple.

## 0. Ancrage mecanique sur V1ZQ

- V1ZQ MD : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZQ_DECRET_REEXEC_BORN_FULL_LOG_20260505_202351/CONTROLE_MULTIMONDES_V1ZQ_DECRET_REEXEC_BORN_FULL_LOG.md` sha256=`a2a60a45dfa05fd230360cedd4ea78c4b2f700cab2c83cdfd71fd7f0c8a5f75d`
- V1ZQ manifest : `auditactionsv1/CONTROLE_MULTIMONDES_V1ZQ_DECRET_REEXEC_BORN_FULL_LOG_20260505_202351/manifest.json` sha256=`e06004424b49abcea7e15200d10befaf17f5c7c6ae310682f0d209272d037ed2`

Si l un de ces sha256 evolue ulterieurement, cet amendement reste ancre au point fige ci-dessus.

## 1. Quatre durcissements obligatoires

### 1.1 Phase 1 doit ECHOUER si sha256 script copie != V1ZJ

Le script `born_temps_validation.py` copie en sandbox V1ZQ doit presenter sha256 = `d9acb122719206a370f1058254d1cfc6b51d3586cce1d379426915c2bac1367d` (valeur V1ZJ figee). Sinon : `exit 1`. Sans cette verification, V1ZQ peut tourner sur un binaire different de V1ZJ et la comparaison stdout devient invalide.

### 1.2 Phase 1 doit ECHOUER si sha256 sitecustomize != V1ZJ

Le sitecustomize copie en sandbox V1ZQ doit presenter sha256 = `9abaa362fcb7b78eb2f2e933794a3df9e8413012a9edf3b212f9ae0298d0fedf` (valeur V1ZJ figee). Le `2>/dev/null || true` du V1ZQ original autorise une absence silencieuse ; ce comportement est annule par cet amendement. Le mode V1ZJ `..._pandas_sitecustomize_redirect_no_patch` rend le sitecustomize indispensable.

### 1.3 Phase 2 doit capturer hash JUSTE AVANT execution

Avant la commande `timeout 60s /usr/bin/python3 born_temps_validation.py`, capturer dans `$OUT/hashes_live_juste_avant_phase2.sha256` les sha256 des memes caches live que Phase 1. Phase 3 fait alors un triple diff : avant tout, juste avant exec, juste apres exec.

### 1.4 Phases 1 / 2 / 3 doivent verifier signature explicite

Chaque bloc commence par :

```bash
[ -f "$OUT/phaseN_signed.txt" ] || { echo "ERREUR: Phase N non signee"; exit 1; }
```

Avec depot manuel de :

- `echo "JE SIGNE V1ZQ DECRET PHASE 1 — PREPARATION SANDBOX V1ZQ" > $OUT/phase1_signed.txt`
- `echo "JE SIGNE V1ZQ DECRET PHASE 2 — EXECUTION CAPTURE STDOUT COMPLET" > $OUT/phase2_signed.txt`
- `echo "JE SIGNE V1ZQ DECRET PHASE 3 — COLLECTE NON-POLLUTION" > $OUT/phase3_signed.txt`

Avant lancement de la phase correspondante. Sans ce fichier, refus mecanique.

## 2. Une variation acceptee documentee

### 2.1 Sandbox V1ZQ dans auditactionsv1 au lieu de HOME

V1ZJ tournait dans HOME via le mode `one_script_sandbox_home_real_usrbinpython3_pandas_sitecustomize_redirect_no_patch`. V1ZQ centralise dans `auditactionsv1/CONTROLE_MULTIMONDES_V1ZQ_REEXEC_BORN_FULL_LOG_20260505_202351/sandbox_born_full_log`.

Cette variation est acceptee pour centraliser les artefacts d audit. Si `born_temps_validation.py` depend subtilement du cwd HOME, le stdout V1ZQ peut differer marginalement de V1ZJ ; la comparaison `stdout_tail V1ZJ inclus dans stdout_full V1ZQ` reste pertinente mais pas une reproduction cwd-identique stricte.

## 3. Statut canonique

- Type : amendement nominal, on ajoute, on n efface rien.
- Effet sur V1ZQ committe : zero.
- Effet runtime : zero.
- Lecture obligatoire : V1ZQ + V1ZQ-bis avant toute signature Phase 1.

## 4. Verdict V1ZQ-bis

- V1ZQ_BIS_AMENDEMENT_OBLIGATOIRE : durcissements 1.1 a 1.4 a appliquer dans les blocs Phase 1/2/3.
- V1ZQ_BIS_SECURITE : aucune execution, aucun patch, aucun cron, aucun broker, aucune sortie Phase 115, vrais_yeux.py INTOUCHABLE.

---

Aucun fichier runtime modifie. Aucun fichier V1ZQ modifie. Phase 115 preservee. decision_weight=0.0.
