# Product Vision

## 1. Core Idea

OpenChipAgentPlatform is an integrated open-source chip design agent platform.

The user should be able to describe a small digital design in natural language and get a reproducible design workflow:

```text
specification
  -> RTL
  -> testbench
  -> simulation
  -> debug loop
  -> synthesis
  -> reports
  -> eventually physical design
```

The platform should not be a black-box "AI chip designer". It should be an auditable engineering assistant that records every decision, command, file, log, patch, and result.

## 2. Why This Is Valuable

Open-source chip design is powerful but fragmented:

- Users must install many tools.
- Each tool has different input formats, logs, errors, and configuration files.
- Flow failures are hard to understand.
- LLM-generated RTL often compiles incorrectly or passes syntax but fails functionally.
- Existing agents are usually focused on one task, not the whole design loop.

OpenChipAgentPlatform can create value by providing:

1. A unified user experience.
2. Reproducible workflows.
3. Automatic tool execution and log interpretation.
4. Feedback-driven RTL and testbench repair.
5. A standard artifact structure for review.
6. Clear explanations of what changed and why.

## 3. Target Users

### Learners

Students and beginners who want to understand chip design from RTL to layout without spending weeks setting up tools.

### Researchers

Researchers working on LLM-for-EDA, RTL generation, automated verification, or design-space exploration.

### Open-source hardware developers

Developers building small IP blocks, RISC-V peripherals, accelerators, or educational SoCs.

### EDA workflow engineers

Engineers exploring how agent systems can automate repetitive flow tasks, report analysis, and debug loops.

## 4. What Would Make It "Powerful"

The platform becomes powerful only if it creates a real closed loop:

```text
generate -> run tools -> parse failure -> repair -> rerun -> summarize
```

The important part is not that an LLM writes Verilog once. The important part is that the system can keep evidence, run objective checks, and converge.

## 5. Product Boundary

The first versions should not claim:

- production-ready autonomous SoC design;
- guaranteed timing closure;
- complex UVM/CDC/DFT signoff;
- replacement for expert hardware engineers;
- commercial-grade physical implementation.

The first versions should claim:

- small RTL module generation;
- simulation-based verification loop;
- synthesis check;
- report parsing;
- reproducible artifact management;
- educational and research usefulness.

## 6. One-Sentence Positioning

OpenChipAgentPlatform is an open-source orchestration layer that connects LLM agents with open EDA tools to create reproducible chip design workflows from specification to verified RTL and, eventually, RTL-to-GDS.

