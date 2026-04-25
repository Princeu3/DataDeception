#!/usr/bin/env python3
"""DataDeception schema validator.

Walks data/ and validates every JSON file against the appropriate schema.
Also checks referential integrity:
- Every deception record's product_id resolves to a product file.
- Every deception record's tactic_ids resolve to tactic files.
- ID naming conventions (kebab-case for products, snake_case for tactics).

Run: .venv/bin/python validate.py
Exit 0 on success, 1 on any validation failure.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012
except ImportError:
    print("ERROR: jsonschema or referencing not installed.", file=sys.stderr)
    print("Run: .venv/bin/pip install jsonschema referencing", file=sys.stderr)
    sys.exit(2)


REPO = Path(__file__).resolve().parent
SCHEMA_DIR = REPO / "schema"
DATA = REPO / "data"


def load_json(p: Path) -> dict:
    with open(p) as fh:
        return json.load(fh)


def build_registry() -> Registry:
    """Build a referencing Registry of all schemas, keyed by both their $id and filename."""
    registry = Registry()
    for p in SCHEMA_DIR.glob("*.schema.json"):
        schema = load_json(p)
        resource = Resource(contents=schema, specification=DRAFT202012)
        sid = schema.get("$id")
        if sid:
            registry = registry.with_resource(uri=sid, resource=resource)
        registry = registry.with_resource(uri=p.name, resource=resource)
    return registry


def validator_for(schema_filename: str, registry: Registry) -> Draft202012Validator:
    schema = load_json(SCHEMA_DIR / schema_filename)
    return Draft202012Validator(schema, registry=registry)


def validate_dir(dirname: str, schema_filename: str, registry: Registry) -> tuple[int, int]:
    validator = validator_for(schema_filename, registry)
    ok = bad = 0
    for p in (DATA / dirname).glob("*.json"):
        data = load_json(p)
        errors = sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path))
        if errors:
            bad += 1
            print(f"\n[INVALID] {p.relative_to(REPO)}", file=sys.stderr)
            for err in errors:
                path = ".".join(str(x) for x in err.absolute_path) or "<root>"
                print(f"  - {path}: {err.message}", file=sys.stderr)
        else:
            ok += 1
    return ok, bad


def check_referential_integrity() -> tuple[int, int]:
    products = {p.stem: load_json(p) for p in (DATA / "products").glob("*.json")}
    tactics = {p.stem: load_json(p) for p in (DATA / "tactics").glob("*.json")}
    ok = bad = 0
    for p in (DATA / "deceptions").glob("*.json"):
        rec = load_json(p)
        errs = []
        if rec["product_id"] not in products:
            errs.append(f"unknown product_id: {rec['product_id']}")
        for t in rec.get("tactic_ids", []):
            if t not in tactics:
                errs.append(f"unknown tactic_id: {t}")
        prefix = rec["product_id"]
        if not rec["id"].startswith(prefix + "__"):
            errs.append(f"record id '{rec['id']}' does not start with '{prefix}__'")
        if errs:
            bad += 1
            print(f"\n[REFERENTIAL] {p.relative_to(REPO)}", file=sys.stderr)
            for e in errs:
                print(f"  - {e}", file=sys.stderr)
        else:
            ok += 1
    return ok, bad


def check_id_conventions() -> tuple[int, int]:
    ok = bad = 0
    kebab = re.compile(r"^[a-z0-9-]+$")
    snake = re.compile(r"^[a-z0-9_]+$")
    for p in (DATA / "products").glob("*.json"):
        d = load_json(p)
        if kebab.match(d["id"]):
            ok += 1
        else:
            bad += 1
            print(f"[CONVENTION] product id not kebab-case: {d['id']}", file=sys.stderr)
    for p in (DATA / "tactics").glob("*.json"):
        d = load_json(p)
        if snake.match(d["id"]):
            ok += 1
        else:
            bad += 1
            print(f"[CONVENTION] tactic id not snake_case: {d['id']}", file=sys.stderr)
    return ok, bad


def main():
    registry = build_registry()

    print("Schema validation")
    p_ok, p_bad = validate_dir("products", "product.schema.json", registry)
    t_ok, t_bad = validate_dir("tactics", "tactic.schema.json", registry)
    d_ok, d_bad = validate_dir("deceptions", "deception.schema.json", registry)
    print(f"  products:   {p_ok} ok, {p_bad} invalid")
    print(f"  tactics:    {t_ok} ok, {t_bad} invalid")
    print(f"  deceptions: {d_ok} ok, {d_bad} invalid")

    print("\nReferential integrity")
    r_ok, r_bad = check_referential_integrity()
    print(f"  deception cross-refs: {r_ok} ok, {r_bad} broken")

    print("\nID conventions")
    c_ok, c_bad = check_id_conventions()
    print(f"  ids: {c_ok} ok, {c_bad} non-conforming")

    total_bad = p_bad + t_bad + d_bad + r_bad + c_bad
    if total_bad:
        print(f"\nVALIDATION FAILED: {total_bad} issue(s)", file=sys.stderr)
        sys.exit(1)
    print("\n✓ All validations passed.")


if __name__ == "__main__":
    main()
