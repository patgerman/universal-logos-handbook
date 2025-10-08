# UL_SPEC_v1.md — Universal Logos / UL/1 Specification (Proposed v1.0)

> **Status:** Draft for community review. Backward compatibility guaranteed only after a tagged release (see `VERSIONING.md`).

## 1. Overview

UL/1 defines a **message** containing metadata and one or more **clauses**. Each clause encodes a typed predicate with explicit roles, optional time, evidence, and confidence. A **Surface Gloss** provides a faithful human paraphrase.

Two equivalent serializations are supported:
- **JSON** (canonical for validation and tooling)
- **S‑expressions** (compact for agent‑to‑agent traffic)

## 2. Message Envelope

| Field        | Type                   | Required | Notes |
|--------------|------------------------|----------|-------|
| `ul_version` | string                 | yes      | Semantic version, e.g. `"1.0"` |
| `id`         | uuid/string            | yes      | Unique per message |
| `from`       | string                 | yes      | Sender id |
| `to`         | string or string[]     | yes      | One or more recipients |
| `t`          | RFC3339 timestamp      | yes      | Message creation time |
| `ctx`        | string                 | no       | Domain/task context (`namespace.action.variant`) |
| `clauses`    | array<Clause>          | yes      | One or more |
| `gloss`      | string                 | no       | Human paraphrase of the whole message |
| `meta`       | object                 | no       | Freeform provenance (`source`, `trace`, etc.) |

## 3. Clause

| Field        | Type              | Required | Notes |
|--------------|-------------------|----------|-------|
| `type`       | enum              | yes      | `assert | query | command | evaluate | hypothesize | plan | status | explain` |
| `event`      | string            | yes      | Event handle (e.g., `e1`, `e_pick`) |
| `predicate`  | string            | yes      | Domain verb, e.g., `describe`, `pick`, `verify` |
| `args`       | object            | yes      | Role arguments as explicit key→value pairs |
| `time`       | object            | no       | `{ start?, end?, tense? }` (RFC3339 times; tense ∈ `past|present|future`) |
| `evidence`   | string or string[]| no       | e.g., `report, citation, perception, statistic, trace` |
| `confidence` | number            | no       | 0.0–1.0 |

**Guideline:** Predicates and role names should be curated per domain. Keep them stable and documented.

## 4. JSON Schema

The canonical JSON Schema lives in `schemas/ul1.schema.json`.

## 5. S‑Expression Form (illustrative)

```
UL/1
id: f64a6d7c-4a9d-4c9a-9d5c-2b6eac3e4d11
from: Planner.AI
to: (Robot.Arm Safety.Monitor)
t: 2025-10-08T08:45:12Z
ctx: warehouse.pick.v1
(command
  :event e_pick
  :pred pick
  :args { agent arm1 object (REF box#A123) from bin#7 to conveyor#2 }
  :time { start 2025-10-08T08:46:00Z }
  :evid plan
  :conf 0.94
)
Surface Gloss: Command: arm1 picks box A123 from bin 7 to conveyor 2.
```

## 6. Evidence & Confidence

- `evidence` is a short tag or list of tags indicating *why* the agent believes the clause (e.g., `perception`, `citation`, `trace`).  
- `confidence` is a scalar 0–1 expressing subjective certainty. Systems may adopt **calibration** protocols separately.

## 7. Names & Conventions

- Project name: **Universal Logos (UL)**
- Machine core: **UL/1**
- Human paraphrase: **Surface Gloss**
- Write “UL/1 message”, not “UL1” or “UL message”.

## 8. Safety & Security (non‑normative)

UL/1 is payload‑level. Use signatures, transport encryption, and access control as appropriate. Consider redacting `meta.trace` in public artifacts.

## 9. Versioning

Minor versions may add *optional* fields. Major versions may change required structure. See `VERSIONING.md`.

## 10. Examples

See `examples/` for AI↔AI knowledge handoff, AI↔Robot commands, and Human↔AI summarization.

