#!/usr/bin/env bash
# ===================================================================
# SERAGONE_ONE_TOTAL.sh
# Photographie canonique exhaustive de Séragone en un seul appel.
# Sortie : canon/SERAGONE_ONE_TOTAL.{md,json,txt} + TREE + GIT + HASH
# Lecture seule, aucun effet de bord. Temps : ~30-60s.
# ===================================================================

set -u
cd "$HOME/seragone" || { echo "FATAL: ~/seragone introuvable"; exit 1; }

TS_UTC=$(date -u +%Y-%m-%dT%H:%M:%SZ)
TS_FILE=$(date -u +%Y%m%d_%H%M%S)
OUT=canon
mkdir -p "$OUT"

MD="$OUT/SERAGONE_ONE_TOTAL.md"
JSON="$OUT/SERAGONE_ONE_TOTAL.json"
TREE="$OUT/SERAGONE_ONE_TOTAL_TREE.txt"
GITF="$OUT/SERAGONE_ONE_TOTAL_GIT.txt"
HASH="$OUT/SERAGONE_ONE_TOTAL_HASH.txt"

echo "[1/12] Identité machine..."
HOST=$(hostname)
USR=$(whoami)
IP=$(hostname -I | tr -s ' ')
UP=$(uptime -p 2>/dev/null || uptime)
DISK=$(df -h / | tail -1)
KERNEL=$(uname -srm)

echo "[2/12] Volumétrie..."
TOT_FILES=$(find . -type f -not -path './.git/*' 2>/dev/null | wc -l)
TOT_SIZE=$(du -sh . 2>/dev/null | cut -f1)
ROOT_DIRS=$(find . -maxdepth 1 -type d | wc -l)
declare -A EXT_COUNT
for ext in py md txt json csv sh log yaml toml ini env conf tar gz zip; do
  C=$(find . -type f -name "*.$ext" -not -path './.git/*' 2>/dev/null | wc -l)
  EXT_COUNT[$ext]=$C
done

echo "[3/12] Arbre filesystem (niveau 4)..."
{
  echo "# SERAGONE filesystem tree (niveau 4, exclusions : .git, backups, __pycache__, archive)"
  echo "# Généré : $TS_UTC"
  echo
  find . -maxdepth 4 \
    -not -path './.git*' \
    -not -path './.backups_*' \
    -not -path './backups_*' \
    -not -path '*/archive*' \
    -not -path '*__pycache__*' \
    -not -path '*.bak.*' \
    | sort
} > "$TREE"
TREE_LINES=$(wc -l < "$TREE")

echo "[4/12] Git état complet..."
{
  echo "# GIT STATE — $TS_UTC"
  echo; echo "## BRANCHE COURANTE"
  git branch -v 2>/dev/null
  echo; echo "## 50 DERNIERS COMMITS"
  git log --oneline -50 2>/dev/null
  echo; echo "## STATUS SHORT (limité 200 lignes)"
  git status --short 2>/dev/null | head -200
  echo; echo "## REMOTES"
  git remote -v 2>/dev/null
  echo; echo "## COMMITS LOCAUX NON POUSSÉS"
  git log origin/main..HEAD --oneline 2>/dev/null
  echo; echo "## COMMITS REMOTE NON TIRÉS"
  git log HEAD..origin/main --oneline 2>/dev/null
} > "$GITF"

echo "[5/12] Cron + systemd..."
CRON=$(crontab -l 2>/dev/null | grep -v '^\s*#' | grep -v '^\s*$' | head -120)
TIMERS=$(systemctl list-timers --all 2>/dev/null | grep -iE "seragone|sentinelle|watchdog")
SERVICES=$(systemctl list-units --type=service --all --no-pager 2>/dev/null | grep -iE "seragone|sentinelle|watchdog")

echo "[6/12] Moteurs M1-M8 et principaux engines..."
ENGINES=""
for E in m1_long_engine m2_bear_engine m2_bear_engine_v2 m3_temperance m7_micro_oscillation mondes_paralleles_engine mondes_autonomes mondes_communicants; do
  if [ -f "${E}.py" ]; then
    ENGINES+="$(stat -c "%n | %s o | %y | sha256=$(sha256sum ${E}.py | cut -c1-16)" ${E}.py)"$'\n'
  fi
done

echo "[7/12] States canoniques vivants..."
STATES=""
while IFS= read -r s; do
  [ -f "$s" ] || continue
  STATES+="$(stat -c "%n | mtime=%y | size=%s" "$s") | sha16=$(sha256sum "$s" 2>/dev/null | cut -c1-16)"$'\n'
done < <(ls states/*.json demo/states/*.json *_state.json *state*.json 2>/dev/null | sort -u)

echo "[8/12] Doctrines, décrets, attestations..."
DOCTRINES=$(ls canon/DOCTRINE_*.md 2>/dev/null)
DECRETS=$(find . -maxdepth 5 -name "DECRET_*.md" 2>/dev/null | head -80)
ATTESTATIONS=$(find . -maxdepth 5 -name "ATTESTATION_*.md" -mtime -30 2>/dev/null | head -80)

echo "[9/12] Caches critiques (drift)..."
CACHES=""
for C in cache_mondes_bear_v2.json cache_mondes_bull.json data/m2_bear_cache.json mondes_paralleles_state.json; do
  if [ -f "$C" ]; then
    CACHES+="$(stat -c "%n | mtime=%y | size=%s" "$C") | sha16=$(sha256sum "$C" 2>/dev/null | cut -c1-16)"$'\n'
  fi
done

echo "[10/12] Sentinelles, watchdogs, processes vivants..."
SENTINELLES=$(ps aux | grep -iE "sentinelle|watchdog|m2_bear|mondes_paralleles" | grep -v grep)
LOCKS=$(ls -la .sentinelle.lock .securite.lock 2>/dev/null)

echo "[11/12] Registre modules + Index canon..."
REG=""
if [ -f canon/modulesregistry_v1_operationnel_REMPLI.json ]; then
  REG="canon/modulesregistry_v1_operationnel_REMPLI.json | $(stat -c size=%s/mtime=%y canon/modulesregistry_v1_operationnel_REMPLI.json) | sha16=$(sha256sum canon/modulesregistry_v1_operationnel_REMPLI.json | cut -c1-16)"
fi

echo "[12/12] Assemblage MD + JSON..."

# === MD final ===
{
  echo "# SERAGONE_ONE_TOTAL"
  echo
  echo "**Généré (UTC)** : $TS_UTC"
  echo "**Hôte** : $HOST | **User** : $USR | **IP** : $IP"
  echo "**Uptime** : $UP"
  echo "**Kernel** : $KERNEL"
  echo "**Disque** : $DISK"
  echo
  echo "## Doctrine de lecture"
  echo "- Ce fichier est LA source de vérité unique pour reprise de session IA."
  echo "- Si X n'y figure pas, X n'existe pas (ou le snapshot est périmé)."
  echo "- Re-générer à chaque début de session : \`bash SERAGONE_ONE_TOTAL.sh\`"
  echo
  echo "## 1. Volumétrie"
  echo "- Total fichiers : $TOT_FILES"
  echo "- Taille totale : $TOT_SIZE"
  echo "- Dossiers racine : $ROOT_DIRS"
  echo "- Lignes arbre niveau 4 : $TREE_LINES"
  echo
  echo "| Extension | Compte |"
  echo "|---|---|"
  for k in "${!EXT_COUNT[@]}"; do echo "| .$k | ${EXT_COUNT[$k]} |"; done | sort
  echo
  echo "## 2. GIT (voir fichier détaillé)"
  echo '```'
  git log --oneline -10 2>/dev/null
  echo '```'
  echo "Commits locaux non poussés :"
  echo '```'
  git log origin/main..HEAD --oneline 2>/dev/null || echo "(aucun ou pas de remote)"
  echo '```'
  echo
  echo "## 3. Moteurs M1-M8"
  echo '```'
  echo "$ENGINES"
  echo '```'
  echo
  echo "## 4. States canoniques"
  echo '```'
  echo "$STATES"
  echo '```'
  echo
  echo "## 5. Caches critiques"
  echo '```'
  echo "$CACHES"
  echo '```'
  echo
  echo "## 6. Cron actif"
  echo '```'
  echo "$CRON"
  echo '```'
  echo
  echo "## 7. Timers systemd Séragone"
  echo '```'
  echo "$TIMERS"
  echo '```'
  echo
  echo "## 8. Services systemd Séragone"
  echo '```'
  echo "$SERVICES"
  echo '```'
  echo
  echo "## 9. Sentinelles / watchdogs vivants"
  echo '```'
  echo "$SENTINELLES"
  echo '```'
  echo "Locks : $LOCKS"
  echo
  echo "## 10. Doctrines actives"
  echo '```'
  echo "$DOCTRINES"
  echo '```'
  echo
  echo "## 11. Décrets (liste)"
  echo '```'
  echo "$DECRETS"
  echo '```'
  echo
  echo "## 12. Attestations récentes (30 derniers jours)"
  echo '```'
  echo "$ATTESTATIONS"
  echo '```'
  echo
  echo "## 13. Registre modules"
  echo "$REG"
  echo
  echo "## 14. INDEX_CANON_SERAGONE.md intégral"
  echo '```'
  cat canon/INDEX_CANON_SERAGONE.md 2>/dev/null
  echo '```'
  echo
  echo "---"
  echo "Fichiers annexes :"
  echo "- $TREE ($(wc -l <"$TREE") lignes)"
  echo "- $GITF"
  echo "- $HASH"
} > "$MD"

# === JSON compact ===
python3 - "$MD" "$TREE" "$GITF" "$HASH" "$TS_UTC" "$TOT_FILES" "$TOT_SIZE" > "$JSON" << 'PY'
import sys, json, hashlib, os
md, tree, gitf, hashf, ts, tot, size = sys.argv[1:8]
def sha(p):
  try: return hashlib.sha256(open(p,'rb').read()).hexdigest()
  except: return None
out = {
  "generated_at_utc": ts,
  "total_files": int(tot),
  "total_size": size,
  "artifacts": {
    "md": {"path": md, "sha256": sha(md), "size": os.path.getsize(md) if os.path.exists(md) else 0},
    "tree": {"path": tree, "sha256": sha(tree)},
    "git": {"path": gitf, "sha256": sha(gitf)}
  }
}
print(json.dumps(out, indent=2, ensure_ascii=False))
PY

# === Hash global ===
sha256sum "$MD" "$JSON" "$TREE" "$GITF" > "$HASH" 2>/dev/null

echo
echo "=== OK SNAPSHOT ÉCRIT ==="
ls -la "$MD" "$JSON" "$TREE" "$GITF" "$HASH"
echo
echo "Taille MD : $(wc -l <"$MD") lignes, $(stat -c %s "$MD") octets"
echo "Hash global :"
cat "$HASH"
