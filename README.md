# Universal Logos (UL) Handbook

A free, open reference for a **universal, machine‑native + human‑readable protocol** for communication across **AI↔AI**, **AI↔Robot**, and **Human↔AI**.

> “Universal Logos — the shared language of meaning between humans and machines.”

---

## What is Universal Logos (UL)?

Universal Logos (UL) is a **dual‑channel meta‑language**:

- **Logical core (UL/1):** a canonical, machine‑native message format (S‑expressions and a JSON equivalent) encoding **event structure, roles, modality, evidence, time, and confidence**.
- **Surface Gloss:** a concise, human‑readable paraphrase of the same content, designed for clarity and auditability.

UL’s goal is to **remove ambiguity**, **standardize intent**, and make communication **portable across models, agents, and platforms**.

---

## Scope & Use Cases

UL is designed for three primary communication modes:

1. **AI ↔ AI:** inter‑agent messaging, tool‑use, planning, chain‑of‑thought summarization, model‑to‑model knowledge exchange.
2. **AI ↔ Robot:** perception→action pipelines, tasking & control, safety gating, explainable autonomy (XAI/XRAI).
3. **Human ↔ AI:** transparent queries/answers, verifiable reasoning, and audit trails for high‑stakes domains.

See **[`HOW_TO_USE_WITH_LLMs.md`](HOW_TO_USE_WITH_LLMs.md)** for practical prompts, recipes, and integration patterns.

---

## Repository Layout

```
/
├─ README.md
├─ HOW_TO_USE_WITH_LLMs.md
├─ LICENSE-MIT
├─ LICENSE-CC-BY-4.0
├─ LICENSES.md                # clarifies dual licensing (text vs code)
├─ VERSIONING.md              # how we version spec & docs
├─ CHANGELOG.md               # human-readable change log
├─ CITATION.cff
├─ CODE_OF_CONDUCT.md
├─ CONTRIBUTING.md
├─ schemas/
│  └─ ul1.schema.json         # JSON Schema for UL/1 messages
├─ examples/
│  ├─ ul1_examples.md
│  └─ robotics/
│     ├─ arm_pick.ul1.json
│     └─ status_report.ul1.json
├─ tools/
│  └─ validate_ul1_json.py    # validate files against ul1.schema.json
└─ handbook/
   └─ Universal_Logos_Handbook_FULL.docx  # (move existing DOCX here)
```
> **Note:** In the current repo, the DOCX sits in the root. To match this layout, please move it into `handbook/`.

---

## Quick Start

1. **Read the Handbook** (DOCX in `handbook/`). Consider also exporting a **PDF** and **Markdown** version for easier diffing.
2. **Learn to use UL with models:** see **[`HOW_TO_USE_WITH_LLMs.md`](HOW_TO_USE_WITH_LLMs.md)**.
3. **Try the spec:** start from **[`UL_SPEC_v1.md`](UL_SPEC_v1.md)** and the **[`examples/`](examples/)** folder.
4. **Validate messages:** run `python tools/validate_ul1_json.py examples/robotics/arm_pick.ul1.json`.

---

## UL/1 at a Glance (JSON form)

```json
{
  "ul_version": "1.0",
  "id": "f64a6d7c-4a9d-4c9a-9d5c-2b6eac3e4d11",
  "from": "Planner.AI",
  "to": ["Robot.Arm", "Safety.Monitor"],
  "t": "2025-10-08T08:45:12Z",
  "ctx": "warehouse.pick.v1",
  "clauses": [{
    "type": "command",
    "event": "e_pick",
    "predicate": "pick",
    "args": { "agent": "arm1", "object": {"ref": "box#A123"}, "from": "bin#7", "to": "conveyor#2" },
    "time": { "start": "2025-10-08T08:46:00Z" },
    "evidence": ["plan"],
    "confidence": 0.94
  }],
  "gloss": "Command: arm1 picks box A123 from bin 7 to conveyor 2."
}
```

More in **`UL_SPEC_v1.md`**.

---

## Versioning & Releases

- We use **SemVer** for the **UL/1 JSON schema** and **handbook versions** (e.g., `v1.0.0`).
- Tag releases (e.g., `v1.0.0`) and publish via GitHub Releases with a short summary from `CHANGELOG.md`.

See **[`VERSIONING.md`](VERSIONING.md)** for details.

---

## License

- **Text & diagrams → CC BY 4.0** (`LICENSE-CC-BY-4.0`)  
- **Code & schemas → MIT** (`LICENSE-MIT`)

See **[`LICENSES.md`](LICENSES.md)** for a plain‑language mapping. By contributing, you agree that **text** you add is CC BY 4.0 and **code/schemas** are MIT.

---

## Citing

Cite the repository via the GitHub‑generated “Cite this repository” button (from `CITATION.cff`). Example (APA‑style):

> Gessner, P. A. (2025). *Universal Logos (UL) Handbook* (Version 1.0). GitHub. https://github.com/patgerman/universal-logos-handbook

---

## Maintainer

**Patrick A. Gessner**

