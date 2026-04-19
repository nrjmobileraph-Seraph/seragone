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
