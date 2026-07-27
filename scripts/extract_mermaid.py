#!/usr/bin/env python3
"""Extract the single canonical Mermaid block for CI rendering."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    text = args.source.read_text(encoding="utf-8")
    blocks = re.findall(r"```mermaid\s*\n(.*?)\n```", text, flags=re.DOTALL)
    if len(blocks) != 1:
        raise ValueError(f"expected one Mermaid block, found {len(blocks)}")

    args.output.write_text(blocks[0].strip() + "\n", encoding="utf-8")
    print(f"Extracted canonical Mermaid diagram to {args.output}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
