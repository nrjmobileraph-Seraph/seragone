"""
seragone_atomic.py — BLUEPRINT_CODE_REFERENCE

Statut canonique : BLUEPRINT_CODE_REFERENCE
Doctrine source  : D9 §6 (DOCTRINE_9_UN_WRITER_PAR_STATE.md)
Hash doctrine    : ba7064fa97399a05c5fdab9f50fc370c71285338dc76e1e258237718202dbba5
Date de création : 2026-04-30
Auteur canonique : Raphaël Boussy + Claude Opus 4.7

Ce module matérialise le pattern d'écriture atomique POSIX
recommandé par D9 §6 lignes 253-338. Il fournit une seule fonction :

    write_state_atomic(state, target_path)

USAGE :
    from tools.seragone_atomic import write_state_atomic
    write_state_atomic({"key": "value"}, "/path/to/state.json")

GARANTIES :
    - Un reader lira soit la version N, soit la version N+1,
      jamais un fichier partiellement écrit.
    - L'écriture est atomique POSIX si target_path est sur un
      seul filesystem.
    - fsync force la persistence disque avant le remplacement
      atomique.

NOTE CANONIQUE D11 stricte sur os.replace vs os.rename :
    D9 §6 ligne 293 utilise os.rename(tmp_path, target_path).
    Ce module utilise os.replace au lieu d'os.rename pour les
    raisons suivantes :
        1. os.replace écrase silencieusement le fichier cible
           si présent, comportement attendu pour un writer de
           state qui remplace régulièrement.
        2. os.rename lève une erreur sur Windows si le fichier
           cible existe déjà (asymétrie cross-platform).
        3. os.replace est garanti atomique POSIX comme os.rename
           sur Linux. Aucune perte de garantie.
    Cet écart par rapport au texte littéral D9 §6 est documenté
    et pourrait faire l'objet d'un AMENDEMENT_INTERPRETATIF_
    D9_7_OS_REPLACE Day N+ si stabilité prouvée.
    D9 elle-même reste inchangée (hash ba7064fa... maintenu).

POSTURE CANONIQUE :
    - BLUEPRINT_CODE_REFERENCE : disponible à l'import
    - N'IMPOSE PAS son adoption (pas d'interface forcée)
    - N'AUCUNE modification de modules existants par ce module
    - Aucun runtime déclenché par l'import
"""

import json
import os
import tempfile


def write_state_atomic(state: dict, target_path: str) -> None:
    """Écrit state dans target_path de façon atomique POSIX.

    Garantie : un reader lira soit la version N, soit la version N+1,
    jamais un fichier partiellement écrit.

    Préconditions :
        - target_path est sur un seul filesystem
        - le dossier parent existe ou peut être créé
        - le dossier parent est writable

    Args:
        state: dictionnaire Python sérialisable en JSON.
        target_path: chemin absolu ou relatif du fichier de
            destination.

    Raises:
        OSError: si le filesystem refuse l'écriture.
        TypeError: si state n'est pas sérialisable en JSON.
        Toute exception levée par tempfile, os.fdopen, json.dump,
        os.fsync ou os.replace est propagée après nettoyage du
        fichier temporaire.
    """
    target_dir = os.path.dirname(target_path) or "."
    os.makedirs(target_dir, exist_ok=True)

    # 1. Créer le fichier temporaire DANS LE MÊME DOSSIER
    #    (le remplacement atomique requiert le même filesystem)
    fd, tmp_path = tempfile.mkstemp(
        prefix=".tmp_",
        suffix=".json",
        dir=target_dir,
    )

    try:
        # 2. Écrire dans le fichier temporaire
        with os.fdopen(fd, "w") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())  # force écriture disque

        # 3. Remplacement atomique vers la cible
        #    os.replace écrase silencieusement la version
        #    précédente si elle existe (cf. NOTE CANONIQUE
        #    en docstring du module).
        os.replace(tmp_path, target_path)

    except Exception:
        # Nettoyage si échec
        if os.path.exists(tmp_path):
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
        raise


# FIN seragone_atomic.py

# D9 compatibility alias.
# Some canon writers historically import writestateatomic without underscores.
writestateatomic = write_state_atomic

