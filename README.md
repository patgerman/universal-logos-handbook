# Universal Logos Handbook

**Citation (Harvard Style):**  
Gessner, P. A. (2025) *Universal Logos Handbook – A Linguistic and Symbolic Framework for Human–AI Communication.*  
Available at: https://github.com/patgerman/universal-logos-handbook  

---

## Universal Logos Handbook

The **Universal Logos (UL) Handbook** defines a standard linguistic and symbolic framework for **Human–AI**, **AI–AI**, and **AI–Robot** communication.  
It aims to be a shared protocol that is **machine-usable** and **human-learnable**, enabling **portable knowledge exchange** across architectures, models, and devices.

---

## Quick links

📘 **Handbook (PDF):** [`handbook/Universal_Logos_WhitePage_2025_Draft_to_v1.0.pdf`](handbook/Universal_Logos_WhitePage_2025_Draft_to_v1.0.pdf)  
🧠 **AI-read (LLM JSON):** [`AI-read/Universal_Logos_Handbook_AI-read.json`](AI-read/Universal_Logos_Handbook_AI-read.json)  
*This file is designed for LLMs to read, parse, and learn the handbook content directly in machine-readable format.*  
🧩 **How to use with LLMs:** [`HOW_TO_USE_WITH_LLMs.md`](HOW_TO_USE_WITH_LLMs.md)  
🗒 **Release Notes:** [`RELEASE_NOTES_v1.0.md`](RELEASE_NOTES_v1.0.md)

---

## What is Universal Logos?

**Universal Logos (UL)** is a structured, compact representation format — a kind of “communication OS” — for:

- **AI–AI knowledge interchange** (skills, capabilities, structured assertions)  
- **Human–AI collaboration** (transparent prompts, interpretable outputs)  
- **AI–Robot interaction** (sensor evidence, physical units, deadlines/guarantees)

The handbook defines message patterns (e.g., `assert`, `query`, `measure`), evidence typing (`:evid sensor | report | calc`), unit enforcement, and transport formats (e.g., MQTT, CBOR) to support **closed-loop, real-world AI integration**.

---

## Repository layout

```
universal-logos-handbook/
├─ examples/                 # Example UL messages and end-to-end workflows
├─ handbook/
│  └─ Universal_Logos_WhitePage_2025_Draft_to_v1.0.pdf
├─ AI-read/                  # LLM-ready JSON mirror of the handbook
│  └─ Universal_Logos_Handbook_AI-read.json
├─ schemas/                  # (Planned) JSON/CBOR schema definitions
├─ tools/                    # (Planned) helper scripts / converters
├─ HOW_TO_USE_WITH_LLMs.md   # Practical guide for using UL with LLMs
├─ UL_SPEC_v1.md             # In-repo spec notes or abridged draft (optional)
├─ README.md                 # You are here
└─ (licenses, contributing, citation, versioning, changelog, etc.)
```

---

## Getting started

1. Read the handbook (PDF).  
2. Review [`HOW_TO_USE_WITH_LLMs.md`](HOW_TO_USE_WITH_LLMs.md) for ready-to-use prompt patterns.  
3. Use the AI-read JSON if you want a machine-readable version for model training or contextual embedding.  
4. Explore examples (coming soon in `/examples`) to see UL in action.

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and our [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).  
For planned changes and known gaps, check [`CHANGELOG.md`](CHANGELOG.md) and [`RELEASE_NOTES_v1.0.md`](RELEASE_NOTES_v1.0.md).

---

## Licensing

- **Source code:** [`LICENSE-MIT`](LICENSE-MIT)  
- **Documentation & handbook:** [`LICENSE-CC-BY-4.0`](LICENSE-CC-BY-4.0)

If you use UL in academic work, please cite using [`CITATION.cff`](CITATION.cff).

---

## Releases

Stable, citable drops are tagged. To fetch v1.0 locally:

```bash
git fetch --tags
git checkout v1.0
```

---

© 2025 Patrick A. Gessner · Universal Logos Project
