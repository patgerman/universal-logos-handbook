> **Citation (Harvard Style):**  
> Gessner, P. A. (2025) *Universal Logos Handbook – A Linguistic and Symbolic Framework for Human–AI Communication.*  
> Available at: [https://github.com/patgerman/universal-logos-handbook](https://github.com/patgerman/universal-logos-handbook)

# Universal Logos Handbook

The **Universal Logos (UL) Handbook** defines a standard linguistic and symbolic framework for **Human–AI**, **AI–AI**, and **AI–Robot** communication. It aims to be a shared protocol that is machine-usable and human-learnable, enabling portable knowledge exchange across architectures, models, and devices.

## Quick links

- 📘 **Handbook (DOCX):** [`handbook/Universal_Logos_Handbook_FULL.docx`](handbook/Universal_Logos_Handbook_FULL.docx)
- 🖹 **PDF preview:** [`handbook/Universal_Logos_Handbook_FULL.pdf`](handbook/Universal_Logos_Handbook_FULL.pdf)
- 🧩 **How to use with LLMs:** [`HOW_TO_USE_WITH_LLMs.md`](HOW_TO_USE_WITH_LLMs.md)
- 🗒 **Release Notes:** [`RELEASE_NOTES_v1.0.md`](RELEASE_NOTES_v1.0.md)

## What is Universal Logos?

Universal Logos (UL) is a structured, compact representation format (a “communication OS”) for:
- **AI–AI knowledge interchange** (skills, capabilities, structured assertions)
- **Human–AI collaboration** (transparent prompts, interpretable outputs)
- **AI–Robot interaction** (sensor evidence, physical units, deadlines/guarantees)

The handbook includes message patterns (e.g., `assert`, `query`, `measure`), evidence typing (`:evid sensor|report|calc`), unit enforcement, and transport options (e.g., MQTT/CBOR) to support closed-loop, real-world use.

## Repository layout

```
universal-logos-handbook/
├─ examples/                 # Example UL messages and end-to-end workflows
├─ handbook/
│  ├─ Universal_Logos_Handbook_FULL.docx
│  └─ Universal_Logos_Handbook_FULL.pdf
├─ schemas/                  # (Planned) JSON/CBOR schema definitions
├─ tools/                    # (Planned) helper scripts / converters
├─ HOW_TO_USE_WITH_LLMs.md   # Practical guide for using UL with LLMs
├─ UL_SPEC_v1.md             # In-repo spec notes or abridged draft (optional)
├─ README.md                 # You are here
└─ (licenses, contributing, citation, versioning, changelog, etc.)
```

## Getting started

1. **Read the handbook** (DOCX or PDF).  
2. **Skim the LLM guide**: [`HOW_TO_USE_WITH_LLMs.md`](HOW_TO_USE_WITH_LLMs.md) for copy-pasteable prompts and integration patterns.  
3. **Try examples** (coming soon in `/examples`) and wire UL into your agent/tooling.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and our code of conduct in [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). For planned changes and known gaps, check [`CHANGELOG.md`](CHANGELOG.md) and release notes.

## Licensing

- Source code: [`LICENSE-MIT`](LICENSE-MIT)  
- Documentation & handbook: [`LICENSE-CC-BY-4.0`](LICENSE-CC-BY-4.0)

If you use UL in academic work, please cite using [`CITATION.cff`](CITATION.cff).

## Releases

Stable, citable drops are tagged. To fetch v1.0 locally:

```bash
git fetch --tags
git checkout v1.0
```
