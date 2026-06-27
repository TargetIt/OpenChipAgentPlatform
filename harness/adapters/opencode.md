# OpenCode Adapter

OpenCode can be used as a host runtime for OpenChipAgent Harness.

## Load Order

An OpenCode session should read:

1. `harness/README.md`
2. `harness/02-run-layout.md`
3. `harness/03-human-review-gates.md`
4. `harness/04-goal-runner.md`
5. `harness/05-loop-engineering.md`
6. the relevant workflow under `harness/workflows/`
7. the relevant skills under `harness/skills/`

## Usage Pattern

```text
Use OpenChipAgent Harness.
Goal: generate a synchronous FIFO with width=32, depth=16.
Done when Verilator lint passes, cocotb simulation passes, and Yosys synthesis passes.
```

## Expected Behavior

The agent should:

- create a run directory;
- write a structured spec;
- generate RTL and testbench;
- run tools;
- classify failures;
- patch and rerun;
- write final report.

It should also keep `metadata/run.json` current enough for another agent to resume the run.
