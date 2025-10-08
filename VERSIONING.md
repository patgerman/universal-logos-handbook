# VERSIONING.md

We version two things:

1. **UL/1 Schema & Spec** — uses **SemVer** (e.g., `1.0.0`).  
   - **Patch:** editorial fixes to markdown/spec w/o changing JSON Schema.  
   - **Minor:** optional fields or non‑breaking guidance updates.  
   - **Major:** breaking changes to required fields, types, or semantics.

2. **Handbook** — mirrors the spec major/minor, with additional patch levels for editorial changes (e.g., `1.0.2`).

## Release Process

1. Update `CHANGELOG.md`.
2. Tag: `git tag v1.0.0 && git push --tags`.
3. Create a GitHub Release from the tag, attach the DOCX/PDF, and summarize changes.
4. If the JSON Schema changed, update `schemas/ul1.schema.json` and regenerate fixtures in `examples/`.
