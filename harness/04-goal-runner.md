# Goal Runner

A goal runner defines what the agent is trying to finish and how completion is checked.

For chip design, goals must be objective. A goal should include:

- design intent;
- interface requirements;
- timing/reset assumptions;
- target tools;
- completion checks;
- max retries;
- human review gates.

The machine-readable goal should follow `schemas/goal.schema.json`. The run output should follow `schemas/run.schema.json`.

## Example Goal

```text
Goal:
Generate a synthesizable synchronous FIFO.

Parameters:
- width = 32
- depth = 16
- interface = ready/valid
- reset = synchronous active-high

Done when:
- spec.md is complete
- rtl/fifo.sv exists
- tb/test_fifo.py exists
- Verilator lint passes
- cocotb simulation passes
- Yosys synthesis passes
- report/final.md explains artifacts, failures, fixes, and remaining risks
```

## Stop Conditions

The agent may stop only when one of these is true:

1. All done checks pass.
2. The goal is blocked by missing user information.
3. The retry budget is exhausted and failures are clearly classified.
4. A human approval gate is reached.

## Required Run Evidence

Each goal run must preserve:

- `goal.json`;
- structured spec;
- generated or modified RTL;
- testbench and reference model;
- raw tool logs;
- command records;
- failure classifications;
- repair actions;
- final report.

## Bad Goal

```text
Make a FIFO.
```

This is too vague.

## Good Goal

```text
Generate a synchronous ready/valid FIFO with width=32 and depth=16.
The design must pass Verilator lint, cocotb tests for reset/full/empty/backpressure, and Yosys synthesis.
```
