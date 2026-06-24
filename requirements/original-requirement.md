# Original Requirement

## 1. Initial Request

The original request was to research open-source tools similar to ChipAgent / ChipAgents, with a focus on tools for chip design.

The user wanted to understand:

- whether there are open-source projects similar to ChipAgent;
- what open-source agents exist for chip design;
- what open-source EDA tools can support chip design;
- whether these tools can be integrated into a larger agentic platform.

## 2. Research Scope Requested

The requested research scope included two major categories.

### 2.1 AI / Agent Tools for Chip Design

Projects and directions similar to:

- ChatEDA;
- AutoChip;
- digital-chip-design-agents;
- RTL-Coder;
- RTLLM;
- VerilogEval;
- TuRTLe;
- other LLM-for-EDA and AI-for-chip-design resources.

The goal was not only to list tools, but to understand which ones could become building blocks for an integrated chip design agent platform.

### 2.2 Open-Source Chip Design Toolchains

Open-source EDA tools and infrastructure such as:

- Verilator;
- Icarus Verilog;
- cocotb;
- Yosys;
- Synlig / Surelog / UHDM;
- OpenROAD;
- OpenLane;
- Magic;
- KLayout;
- Netgen;
- OpenFASoC;
- SkyWater SKY130 PDK;
- IHP Open PDK;
- Caravel.

These tools are the practical backend needed to move from RTL generation toward synthesis, physical design, layout inspection, and eventually GDS output.

## 3. Product Idea Raised by the User

After the initial research, the user proposed a larger idea:

> Build an integrated Agent that brings these open-source agents and open-source EDA tools together, so that a user can use it out of the box from the frontend to the backend.

In other words, the desired project is not merely a list of tools. It is an integrated platform.

## 4. Desired Platform Concept

The desired platform should integrate the chip design workflow end to end:

```text
natural language specification
  -> requirement clarification
  -> RTL generation
  -> testbench generation
  -> simulation
  -> automated debug
  -> synthesis
  -> place and route
  -> timing / area / power report analysis
  -> final artifacts and review report
```

The platform should behave like an open-source chip design agent orchestrator.

## 5. Core User Expectations

The user expects the platform to:

1. Integrate existing open-source agents and tools instead of reinventing everything.
2. Provide an out-of-the-box user experience.
3. Cover the workflow from the earliest design intent to backend implementation.
4. Keep the process auditable and reproducible.
5. Save generated files, logs, reports, and artifacts.
6. Use tool feedback to drive automatic repair loops.
7. Help users understand failures, reports, and next actions.

## 6. Important Product Direction

The direction is considered valuable if implemented carefully.

The platform should not be positioned as a magical black-box chip designer. It should be positioned as:

> An open-source orchestration layer that connects LLM agents with open EDA tools to create reproducible chip design workflows from specification to verified RTL and, eventually, RTL-to-GDS.

## 7. Recommended First Milestone

The recommended first milestone is conservative:

```text
small natural language spec
  -> generated Verilog RTL
  -> generated testbench
  -> Verilator / cocotb simulation
  -> automatic debug loop
  -> Yosys synthesis
  -> area / timing summary
```

This milestone should be completed before attempting full physical design automation with OpenROAD/OpenLane.

## 8. Repository Creation Requirement

The user requested a GitHub repository named:

```text
OpenChipAgentPlatform
```

The repository should contain the initial research and the platform idea.

The user specifically requested a `research/` directory for the research material.

This `requirements/` directory was later added to preserve the original demand and intent separately from the research analysis.

