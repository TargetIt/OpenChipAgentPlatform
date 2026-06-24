# Research Overview

This directory records the initial research and product thinking for OpenChipAgentPlatform.

The goal is to understand whether we can build an integrated chip-design agent platform by combining existing open-source agents, LLM-based RTL generation systems, and open-source EDA tools.

## Documents

- [01-landscape-survey.md](01-landscape-survey.md): survey of related open-source tools, agents, benchmarks, EDA flows, and PDKs.
- [02-product-vision.md](02-product-vision.md): product idea and why an integrated platform matters.
- [03-system-architecture.md](03-system-architecture.md): proposed architecture for an end-to-end chip design agent orchestrator.
- [04-mvp-roadmap.md](04-mvp-roadmap.md): staged implementation roadmap.
- [05-risks-and-open-questions.md](05-risks-and-open-questions.md): technical risks, product risks, and research questions.

## Key Conclusion

There is no mature open-source "ChipAgent replacement" that can reliably take a real-world chip from natural language to production GDS today.

However, the ecosystem has enough building blocks to create a valuable open-source platform:

- LLM/agent research for RTL generation and EDA workflow automation.
- Open-source simulation, linting, and verification tools.
- Open-source synthesis and RTL-to-GDS flows.
- Open PDKs and open tapeout harnesses.
- Benchmarks for measuring generated RTL quality.

The opportunity is to build the missing orchestration layer: a reproducible, auditable, end-to-end agent workflow that connects these pieces.

