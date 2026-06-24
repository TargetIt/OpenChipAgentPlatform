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

## Repository Structure

```text
research/
  README.md
  01-landscape-survey.md
  02-product-vision.md
  03-system-architecture.md
  04-mvp-roadmap.md
  05-risks-and-open-questions.md
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

