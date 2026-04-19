"""
Tests de non-régression du dataset Séragone.
Passe 2 : vérifications structurelles et métier.
"""
import json
import subprocess
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "tests" / "fixtures"


# ---------- fixtures session ----------

@pytest.fixture(scope="session")
def repo_root():
    return ROOT


@pytest.fixture(scope="session")
def git_tags(repo_root):
    out = subprocess.run(
        ["git", "-C", str(repo_root), "tag", "--list"],
        capture_output=True, text=True, check=True,
    ).stdout.strip().splitlines()
    return [t for t in out if t]


# ---------- tests squelette (Passe 1) ----------

def test_smoke_setup():
    assert ROOT.exists()
    assert (ROOT / "tests").is_dir()


def test_fixtures_load(git_tags):
    assert len(git_tags) >= 4, f"Moins de 4 tags Git détectés: {git_tags}"


# ---------- Passe 2 : 6 tests de non-régression ----------

def test_core_scripts_present(repo_root):
    """Les scripts pivot du pipeline doivent exister."""
    # Le cron maître DOIT exister (pivot du pipeline).
    assert (repo_root / "CRON_MAITRE.cron").exists(), "CRON_MAITRE.cron absent"
    # Au moins un script .py doit exister quelque part dans le repo.
    pys = [f for f in repo_root.rglob("*.py")
           if ".venv" not in f.parts and ".git" not in f.parts]
    assert len(pys) >= 1, "Aucun script Python trouvé dans le repo"


def test_state_files_valid_json(repo_root):
    """Tous les fichiers state/*.json doivent être du JSON valide."""
    state_dir = repo_root / "state"
    if not state_dir.exists():
        pytest.skip("pas de dossier state/")
    bad = []
    for f in state_dir.glob("*.json"):
        try:
            json.loads(f.read_text())
        except json.JSONDecodeError as e:
            bad.append(f"{f.name}: {e}")
    assert not bad, f"JSON invalide: {bad}"


def test_no_committed_secrets(repo_root):
    """Aucune clé API ne doit être commitée (grep minimal)."""
    patterns = ["BEGIN RSA PRIVATE KEY", "AKIA", "sk-proj-", "sk_live_"]
    out = subprocess.run(
        ["git", "-C", str(repo_root), "grep", "-l", "-E",
         "|".join(patterns), "--", ":!tests/"],
        capture_output=True, text=True,
    )
    assert out.returncode != 0 or not out.stdout.strip(), (
        f"Secrets potentiels détectés: {out.stdout}"
    )


def test_cron_syntax(repo_root):
    """CRON_MAITRE.cron : chaque ligne active a ≥6 champs."""
    cron = repo_root / "CRON_MAITRE.cron"
    if not cron.exists():
        pytest.skip("pas de CRON_MAITRE.cron")
    bad = []
    for i, line in enumerate(cron.read_text().splitlines(), 1):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        # Ignorer les assignations de variables d'environnement cron
        # (ex: SHELL=/bin/bash, PATH=..., MAVAR=valeur)
        if "=" in s.split()[0] and " " not in s.split("=", 1)[0]:
            continue
        if len(s.split()) < 6:
            bad.append(f"L{i}: {s!r}")
    assert not bad, f"Lignes cron mal formées: {bad}"


def test_logs_dir_writable(repo_root):
    """logs/ doit exister et être inscriptible."""
    logs = repo_root / "logs"
    assert logs.exists() and logs.is_dir(), "logs/ absent"
    probe = logs / ".pytest_probe"
    probe.write_text("ok")
    probe.unlink()


def test_python_imports_ok(repo_root):
    """Les modules internes critiques doivent s'importer sans erreur."""
    import sys
    sys.path.insert(0, str(repo_root))
    # Découverte : tous les modules .py à la racine et dans scripts/ (si présent).
    import importlib.util
    candidates = []
    for f in (repo_root).glob("*.py"):
        if f.stem.startswith("_") or f.stem == "setup":
            continue
        candidates.append(f.stem)
    if (repo_root / "scripts").is_dir():
        for f in (repo_root / "scripts").glob("*.py"):
            if f.stem.startswith("_"):
                continue
            candidates.append(f"scripts.{f.stem}")
    if not candidates:
        pytest.skip("aucun module Python à tester")
    # On cible uniquement les modules "safe" (sans deps lourdes).
    # Ajuster cette liste selon ton pipeline.
    safe_mods = ["config"]
    mods = [m for m in safe_mods if m in candidates]
    if not mods:
        pytest.skip("aucun module safe trouvé")
    failed = {}
    for m in mods:
        try:
            __import__(m)
        except Exception as e:
            failed[m] = repr(e)
    sys.path.pop(0)
    assert not failed, f"Imports cassés: {failed}"

# ---------- Passe 3 : tests métier read-only ----------

def test_btc_daily_schema(repo_root):
    """btc_daily.csv doit être un OHLCV daily lisible."""
    import csv
    import re

    p = repo_root / "data" / "btc_daily.csv"
    assert p.exists(), "data/btc_daily.csv absent"

    date_re = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    with open(p, newline="", encoding="utf-8") as f:
        r = csv.reader(f)
        header = next(r)
        assert header == ["Date", "Close", "High", "Low", "Open", "Volume"]
        rows = list(r)

    assert rows, "btc_daily.csv vide"
    assert len(rows) > 1000, "historique BTC trop court"

    prev = None
    for row in rows[:50]:
        assert len(row) == 6, f"ligne mal formée: {row}"
        assert date_re.match(row[0]), f"date invalide: {row[0]}"
        for v in row[1:]:
            float(v)
        if prev is not None:
            assert row[0] > prev, "ordre des dates non croissant"
        prev = row[0]


def test_lot_e_files_exist_and_parse(repo_root):
    """Les états vivants Lot E doivent exister et être lisibles."""
    import csv

    files = [
        "data/chaines_epurees_state.json",
        "data/communicants_history.json",
        "data/ec_latest.json",
        "data/live_metrics.json",
        "data/mondes_paralleles_cache.json",
        "data/mondes_paralleles_history.csv",
        "data/phi_engine_memory.json",
        "data/phi_local_20m.json",
        "data/phi_local_100m.json",
        "data/phi_local_500m.json",
        "data/recursif_v1_config.json",
    ]

    missing = []
    bad = []

    for rel in files:
        p = repo_root / rel
        if not p.exists():
            missing.append(rel)
            continue
        if p.suffix == ".json":
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
                assert isinstance(data, (dict, list))
            except Exception as e:
                bad.append(f"{rel}: {e}")
        elif p.suffix == ".csv":
            try:
                with open(p, newline="", encoding="utf-8") as f:
                    rows = list(csv.reader(f))
                assert rows and len(rows[0]) >= 2
            except Exception as e:
                bad.append(f"{rel}: {e}")

    assert not missing, f"Lot E manquants: {missing}"
    assert not bad, f"Lot E invalides: {bad}"


def test_mondes_paralleles_history_has_rows(repo_root):
    """Historique mondes parallèles : header + au moins 1 ligne."""
    import csv

    p = repo_root / "data" / "mondes_paralleles_history.csv"
    assert p.exists(), "mondes_paralleles_history.csv absent"

    with open(p, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    assert len(rows) >= 2, "historique mondes parallèles vide"
    assert rows[0] == ["date", "prix", "n_actif", "n_mondes", "convergence_pct"]


def test_seragone_brain_is_readable(repo_root):
    """Le brain pivot doit exister et rester lisible."""
    p = repo_root / "seragone_brain.py"
    assert p.exists(), "seragone_brain.py absent"
    txt = p.read_text(encoding="utf-8")
    assert "def " in txt, "seragone_brain.py semble vide ou corrompu"
    assert "WEIGHTS" in txt, "WEIGHTS absent du brain"
    assert "PHI_STAR" in txt, "PHI_STAR absent du brain"


def test_cron_references_existing_scripts(repo_root):
    """Les scripts Python référencés dans le cron maître doivent exister."""
    import re

    cron = repo_root / "CRON_MAITRE.cron"
    if not cron.exists():
        pytest.skip("pas de CRON_MAITRE.cron")

    missing = []
    pattern = re.compile(r"python3\s+([A-Za-z0-9_./-]+\.py)")

    for line in cron.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        for rel in pattern.findall(s):
            p = repo_root / rel
            if not p.exists():
                missing.append(rel)

    assert not missing, f"scripts cron manquants: {sorted(set(missing))}"
