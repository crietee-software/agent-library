#!/usr/bin/env python3
"""Allocate the next QTE, INV, or CRN number and append a draft to the register."""

import argparse
import json
from datetime import date
from pathlib import Path

REGISTER = Path("/workspace/artifacts/admin/register.json")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", required=True, choices=["QTE", "INV", "CRN"])
    parser.add_argument("--client", default="")
    parser.add_argument("--title", default="")
    parser.add_argument("--amount", default="")
    args = parser.parse_args()

    REGISTER.parent.mkdir(parents=True, exist_ok=True)
    if REGISTER.exists():
        data = json.loads(REGISTER.read_text())
    else:
        data = {"documents": []}

    year = date.today().year
    prefix = f"{args.kind}-{year}-"
    used = []
    for doc in data.get("documents", []):
        number = doc.get("number", "")
        if number.startswith(prefix):
            try:
                used.append(int(number.rsplit("-", 1)[-1]))
            except ValueError:
                continue
    nxt = (max(used) if used else 0) + 1
    number = f"{prefix}{nxt:03d}"
    data.setdefault("documents", []).append(
        {
            "number": number,
            "kind": args.kind,
            "date": date.today().isoformat(),
            "client": args.client,
            "title": args.title,
            "amount_excl": args.amount,
            "status": "draft",
        }
    )
    REGISTER.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(number)


if __name__ == "__main__":
    main()
