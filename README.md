# OpenChipAgentPlatform

OpenChipAgentPlatform is a research and product exploration project for building an end-to-end open-source chip design agent platform.

The core idea is to integrate LLM agents, open-source EDA tools, verification workflows, synthesis flows, and physical design flows into one reproducible system:

```text
Natural language specification
  -> design clarification
  -> RTL generation
  -> testbench generation
  -> simulation and debug loop
  -> synthesis
  -> place and route
  -> timing / area / power report analysis
  -> final artifacts and review report
```

The project starts from research. The `research/` directory records the initial landscape survey, product concept, architecture proposal, and MVP roadmap.

The current practical direction is harness-first: build a chip-design-specific harness that can be used by existing general-purpose coding agents such as OpenCode, Claude Code, Codex, Cursor, or Aider.

## Repository Structure

```text
requirements/
  original-requirement.md

research/
  README.md
  01-landscape-survey.md
  02-product-vision.md
  03-system-architecture.md
  04-mvp-roadmap.md
  05-risks-and-open-questions.md

brainstorm/
  01-harness-hermes-loop-goal.md
  02-open-agent-base-for-chip-design.md
  03-deep-opportunity-map.md

harness/
  README.md
  00-overview.md
  01-why-harness-first.md
  04-goal-runner.md
  05-loop-engineering.md
  06-hermes-style-skill-memory.md
  10-mvp-rtl-goal-runner.md
  adapters/
  workflows/
  schemas/
  templates/
  skills/
```

## Current Scope

This repository is currently focused on documentation and planning. Implementation should start only after the workflow boundaries, tool interfaces, and verification strategy are clear.

The recommended first milestone is not "natural language to production chip". The recommended first milestone is:

```text
small natural language spec
  -> generated Verilog RTL
  -> generated testbench
  -> Verilator / cocotb simulation
  -> automatic debug loop
  -> Yosys synthesis
  -> area / timing summary
```

After that is stable, the platform can add OpenROAD/OpenLane-based physical design.
