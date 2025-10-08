#!/usr/bin/env python3
"""Validate a UL/1 JSON file against schemas/ul1.schema.json."""
import json, sys, pathlib
try:
    import jsonschema
except Exception as e:
    print("Please 'pip install jsonschema' first.")
    raise

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "ul1.schema.json"

def main(path):
    data = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    jsonschema.validate(instance=data, schema=schema)
    print("OK:", path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: validate_ul1_json.py <file.json>")
        sys.exit(2)
    main(sys.argv[1])
