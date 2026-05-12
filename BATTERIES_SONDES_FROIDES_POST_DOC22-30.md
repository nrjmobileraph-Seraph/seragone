# BATTERIES SONDES FROIDES — Doctrine post-Doc22-30

**Document procédural Séragone — révisé le 12 mai 2026 (session A9 v1 + Porte 0).**

---

## Préambule

Les "sondes froides" sont des commandes shell/Python à rejouer sans contexte préalable pour auditer l'état du système Séragone. Chaque sonde est autonome, idempotente, et lisible par un humain ou par un assistant IA en relais.

Document compagnon : `ANOMALIES_A8_A9_12mai2026.md` (hash canonique `65b1381c...`).

---


## Doctrine des 6 Portes — révision 12 mai 2026

Tout nouvel artefact computationnel introduit dans Séragone (script, watchdog, registre, monde, moteur, pépite, doc) doit passer 6 portes obligatoires.

### Porte 0 — Sonder l'existant avant créer

**Énoncé** : Avant toute création, exécuter une sonde exhaustive sur le concept dans le dépôt existant.

**Procédure canonique** :

```bash
CONCEPT="<mot_clef>"
echo "=== Code Python existant ==="
grep -rln "$CONCEPT" ~/seragone/*.py 2>/dev/null
echo "=== Crontab ==="
crontab -l 2>/dev/null | grep -i "$CONCEPT"
echo "=== Services systemd ==="
systemctl list-units --type=service 2>/dev/null | grep -i "$CONCEPT"
echo "=== Timers systemd ==="
systemctl list-timers --all 2>/dev/null | grep -i "$CONCEPT"
echo "=== Docs Markdown ==="
grep -rln "$CONCEPT" ~/seragone/*.md 2>/dev/null
```

**Si hits non vides → lire avant créer. Si zéro hit → créer.**

**Origine empirique** : session 12 mai 2026, création de `state_freshness_watchdog.py` sans avoir lu `watchdog_seragone.py` natif déjà présent et fonctionnel. Faute évitée de justesse, faux diagnostic A12.

### Porte 1 — Identité

Nom canonique, emplacement code, emplacement state. Inscrire un contract en tête du fichier `.py` :

```python
# === SERAGONE STATE CONTRACT ===
# PRODUCES: <fichier_state.json>
# CONSUMES: <liste states lus>
# TTL_PRODUCED: <secondes>
# CRITICALITY: HIGH | MEDIUM | LOW
# REGISTERED_IN: state_registry.json
# === END CONTRACT ===
```

### Porte 2 — Production

Quels states écrit-il, à quelle fréquence, avec quel TTL ? Inscrire `producer` dans `state_registry.json`.

### Porte 3 — Consommation

Quels states lit-il, avec quel garde-fou de fraîcheur ? Tout `read_json` doit être précédé d'un check `(time.time() - p.stat().st_mtime) > TTL`. Sans garde-fou TTL → faute Porte 3, équivalente à A9.

### Porte 4 — Câblage

Lancé par cron, systemd service, systemd timer, ou orchestrateur ? Vérifiable comment ?

**Procédure de vérification** :

```bash
grep -i "<nom_script>" ~ -r --include="*.sh" --include="crontab" 2>/dev/null
crontab -l | grep "<nom_script>"
systemctl list-units | grep "<nom_script>"
systemctl list-timers --all | grep "<nom_script>"
```

Si aucun mécanisme déclenchant n'est trouvé → producteur orphelin → faute Porte 4.

### Porte 5 — Mort propre

Si on supprime le composant, qu'arrive-t-il aux consommateurs aval ? Procédure de migration documentée dans ce document.

**Origine A9** : 3 producteurs morts le 22 avril sans Porte 5 → fossiles toxiques 19 jours durant.

---

## Sonde mensuelle canonique — audit états *_state.json

À rejouer le 1er de chaque mois (cron suggéré : `0 8 1 * * cd ~/seragone && bash sonde_mensuelle_states.sh`).

```bash
{
echo "=== Audit exhaustif states - $(date -Iseconds) ==="
find ~/seragone -maxdepth 4 -name "*_state.json" -type f 2>/dev/null \
  | grep -vE "\.venv|__pycache__|/archive|/backups|AUDIT_CHRONO|_freeze_|\.bak" \
  | xargs -I{} stat -c "%y  %10s o  %n" {} | sort -r > /tmp/audit_states_$(date +%Y%m).txt
wc -l /tmp/audit_states_$(date +%Y%m).txt
echo
echo "=== States stale > 7 jours ==="
NOW=$(date +%s)
for f in $(find ~/seragone -maxdepth 4 -name "*_state.json" -type f 2>/dev/null \
           | grep -vE "\.venv|__pycache__|/archive|/backups|\.bak"); do
  MT=$(stat -c %Y "$f")
  AGE_DAYS=$(( (NOW - MT) / 86400 ))
  if [ $AGE_DAYS -gt 7 ]; then
    echo "  ${AGE_DAYS}j  $f"
  fi
done
echo
echo "=== Cross-check avec state_registry.json ==="
python3 ~/seragone/state_freshness_watchdog.py
echo
echo "=== Verdict natif ==="
cat ~/seragone/watchdog_state.json | python3 -m json.tool
}
```

---

## Sonde rapide — diagnostic d'une suspicion d'anomalie

Quand un comportement runtime est suspect (injection inattendue, valeur anormale), exécuter :

```bash
SUSPECT="<state_ou_concept>"
{
echo "=== mtime et taille ==="
find ~/seragone -name "*${SUSPECT}*" -type f 2>/dev/null \
  | xargs -I{} stat -c "%y  %10s o  %n" {} | sort -r | head -10
echo
echo "=== Producteurs et consommateurs Python ==="
grep -rln "$SUSPECT" ~/seragone/*.py 2>/dev/null | grep -v ".bak"
echo
echo "=== Contenu actuel ==="
F=$(find ~/seragone -maxdepth 3 -name "${SUSPECT}_state.json" -type f 2>/dev/null | head -1)
[ -n "$F" ] && cat "$F" | python3 -m json.tool 2>/dev/null | head -30
}
```

---

## Hashes canoniques session 12 mai 2026

- `money_manager.py`             : `f9b1580c94bbdf3245c1ac4629d2db85bb71485f175f1cd6733a409aeab0aa75`
- `state_registry.json` v0.3     : `5f227b74627a71b0f0607e9aecb787ed73fc6e9ad57cc21f9fb0836df04da2ec`
- `ANOMALIES_A8_A9_12mai2026.md` : `65b1381c957caef852e89dc72217774bf72e8d062640e3b51074cbbe9cfdb62f`
- `state_freshness_watchdog.py`  : `7c59378cfeaca1c3837c03a25f8fb085437f02f5236357bf4980b03fc65dc45c`

---

## Fin de la révision 12 mai 2026

Prochaine session : audit A10 (15 fossiles satellites, consommateurs aval hors MM).
