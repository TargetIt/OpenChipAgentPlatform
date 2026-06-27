# OpenChipAgent Harness

This directory turns the brainstormed OpenChipAgentPlatform idea into a practical harness that can be used by existing general-purpose coding agents.

The first goal is not to build a new agent runtime. The first goal is to make OpenCode, Claude Code, Codex, Cursor, Aider, or similar coding agents behave like chip-design agents by giving them:

- clear goals;
- strict workflows;
- EDA tool loops;
- artifact rules;
- failure taxonomy;
- review gates;
- reusable chip-design skills.

## Why Harness First

General coding agents are already good at reading repositories, editing files, running commands, and iterating on failures. Rebuilding that runtime first would delay the actual chip-design learning.

The missing layer is a chip-design-specific harness:

```text
general coding agent
  + OpenChipAgent Harness
  + Verilator / cocotb / Yosys / OpenROAD / OpenLane feedback
  = goal-driven chip design workflow
```

## First-Stage Structure

```text
harness/
  00-overview.md
  01-why-harness-first.md
  02-run-layout.md
  03-human-review-gates.md
  04-goal-runner.md
  05-loop-engineering.md
  06-hermes-style-skill-memory.md
  10-mvp-rtl-goal-runner.md
  adapters/
  examples/
  policies/
  workflows/
  schemas/
  templates/
  skills/
```

## First Supported Goal

```text
Given a natural language spec, generate synthesizable RTL.
Done when:
- spec.md is complete
- RTL exists
- testbench exists
- Verilator lint passes
- cocotb or equivalent simulation passes
- Yosys synthesis passes
- final report summarizes artifacts, fixes, and risks
```

## Design Principle

The agent should not stop when it has written code. It should stop only when the goal's objective engineering checks pass, or when it has a clearly classified blocker requiring human review.

## Minimum Runnable Contract

Every harness run should create a reproducible run directory:

```text
runs/<goal_id>/<run_id>/
  goal.json
  spec/spec.md
  rtl/
  tb/
  scripts/
  logs/
  metadata/run.json
  reports/final.md
```

The run is not complete until `metadata/run.json` records the exact commands, checks, artifacts, failures, repair attempts, and final status.

## First Example

The first concrete example lives under:

```text
harness/examples/fifo-sync/
```

It demonstrates how a natural-language FIFO goal becomes a structured spec, RTL file, cocotb testbench, Verilator command, Yosys script, run metadata, and final report.
