#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
D9/D11 NEUTRALIZED NON-CANON ENTRYPOINT.

This file is intentionally not a writer.
Canonical Mondes writer: mondes_paralleles_engine.py

Do not import or delegate to the canonical writer here:
keeping a second executable entrypoint would recreate a D9 ambiguity.
"""

import sys

MESSAGE = (
    "D9_NONCANON_WRITER_NEUTRALIZED: "
    "use mondes_paralleles_engine.py as the only canonical Mondes writer"
)

def main() -> int:
    print(MESSAGE, file=sys.stderr)
    return 64

if __name__ == "__main__":
    raise SystemExit(main())
