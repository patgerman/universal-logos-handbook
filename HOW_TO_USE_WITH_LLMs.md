# How to Use Universal Logos (UL) with LLMs & Robots

This guide shows how to apply UL across **AI↔AI**, **AI↔Robot**, and **Human↔AI** scenarios. UL provides a **logical core (UL/1)** plus a **Surface Gloss** for humans.

---

## 0) Mental Model

- **UL/1** = *machine‑native message* (JSON or S‑expr) encoding: predicate, roles, time, evidence, confidence.
- **Surface Gloss** = *human‑readable paraphrase* of the same message.
- **Round‑trip:** Agents should preserve semantics when translating between the two.

---

## 1) Prompt Scaffolds (Human → LLM)

**A. Ask for UL/1 + Gloss**

> “Answer in UL/1 JSON **and** provide a short Surface Gloss. Encode the event structure (predicate, roles, time), include an evidence label and a confidence from 0–1.”

**B. Constrain the ontology**

> “Use predicates from this set: `describe, pick, place, move, measure, compare, verify, plan`. Arguments must be explicit key‑value pairs.”

**C. Require citations or traces**

> “Add `evidence` with labels such as `report, citation, perception, statistic, trace`, and include a `meta.trace` string if applicable.”

---

## 2) Agent‑to‑Agent Messages (AI ↔ AI)

**Example — Knowledge handoff**

```json
{
  "ul_version": "1.0",
  "id": "b2b8ab6d-97f1-41ae-8b0b-1fe1c2a91111",
  "from": "Retriever.AI",
  "to": "Reasoner.AI",
  "t": "2025-10-08T08:00:00Z",
  "ctx": "faq.answering",
  "clauses": [{
    "type": "assert",
    "event": "e1",
    "predicate": "describe",
    "args": { "theme": {"ref": "doc:UL-handbook#sec3"}, "topic": "UL/1 message format" },
    "evidence": ["citation"],
    "confidence": 0.88
  }],
  "gloss": "Describing UL/1 message format per doc section 3."
}
```

---

## 3) AI ↔ Robot

**Example — Command a pick action**

```json
{
  "ul_version": "1.0",
  "id": "f0b0b4db-8a21-4a0d-aeee-3454321f1111",
  "from": "Planner.AI",
  "to": ["Robot.Arm", "Safety.Monitor"],
  "t": "2025-10-08T08:30:00Z",
  "ctx": "warehouse.pick.v1",
  "clauses": [{
    "type": "command",
    "event": "e_pick",
    "predicate": "pick",
    "args": { "agent": "arm1", "object": {"ref": "box#A123"}, "from": "bin#7", "to": "conveyor#2" },
    "time": { "start": "2025-10-08T08:31:00Z" },
    "evidence": ["plan"],
    "confidence": 0.95
  }],
  "gloss": "Command: arm1 picks box A123 from bin 7 to conveyor 2."
}
```

**Example — Status report**

```json
{
  "ul_version": "1.0",
  "id": "3aa7a0a5-9b6b-4d81-b5a6-9b1c4eef2222",
  "from": "Robot.Arm",
  "to": "Planner.AI",
  "t": "2025-10-08T08:31:05Z",
  "ctx": "warehouse.pick.v1",
  "clauses": [{
    "type": "assert",
    "event": "e_pick",
    "predicate": "status",
    "args": { "state": "started", "task_ref": "e_pick" },
    "evidence": ["perception"],
    "confidence": 0.99
  }],
  "gloss": "Status: pick task e_pick started."
}
```

---

## 4) Human ↔ AI

Ask the model to **always** return both **UL/1 JSON** and a **Surface Gloss**. Require confidence and evidence tags. Example prompt:

> “Summarize this contract as UL/1 (JSON) with a `describe` predicate over each clause; provide `evidence: [citation]` with paragraph refs; give a short Surface Gloss.”

---

## 5) Good Practices

- **Deterministic structure:** keep predicates and roles consistent per domain.
- **Evidence & confidence:** always include.
- **Time:** when in doubt, add `t` at the message level and `time` at the clause level.
- **Validation:** run `tools/validate_ul1_json.py` or use the JSON Schema directly.
- **Gloss discipline:** the gloss should be faithful to the UL/1 content, not a new claim.

---

## 6) FAQ

**Why JSON and S‑expressions?**  
JSON plays well with tools; S‑exprs are compact and nest cleanly. Both are canonical views of the same semantics.

**How is this different from plain “reasoning traces”?**  
UL/1 is **typed, explicit, and machine‑verifiable**. It standardizes evidence, time, and confidence — and is designed to be auditable across agents.

**Is there a security model?**  
Use UL with your existing authz/authn. Include `meta.source` and `meta.trace` for provenance. Consider signing messages at transport or payload level.

