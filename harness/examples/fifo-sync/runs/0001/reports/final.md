# Final Report

## Goal

- Goal ID: `fifo-sync`
- Run ID: `0001`
- Status: `needs_review`

## Summary

This archived example demonstrates the expected harness artifact shape for a synchronous ready/valid FIFO. It records the intended commands and artifacts, but the commands have not been executed as part of this documentation-only example.

## Artifacts

| Type | Path | Required | Notes |
| --- | --- | --- | --- |
| Goal | `goal.json` | yes | Machine-readable objective |
| Spec | `spec/spec.md` | yes | Complete structured spec |
| RTL | `rtl/fifo_sync.sv` | yes | Example implementation |
| Testbench | `tb/test_fifo_sync.py` | yes | Directed and randomized cocotb tests |
| Script | `scripts/synth.ys` | yes | Yosys synthesis script |
| Metadata | `metadata/run.json` | yes | Reproducibility record |

## Tool Results

| Stage | Command ID | Status | Evidence |
| --- | --- | --- | --- |
| Lint | `cmd-verilator-lint` | not run | Command recorded in `metadata/run.json` |
| Simulation | `cmd-cocotb` | not run | Command recorded in `metadata/run.json` |
| Synthesis | `cmd-yosys` | not run | Command recorded in `metadata/run.json` |

## Failures and Fixes

None recorded. This is an archived example package, not a completed tool run.

## Human Review Gates

The run status is `needs_review` because the example commands are recorded but not executed in this repository update.

## Remaining Risks

- The example RTL has not been proven by local tool execution in this commit.
- The cocotb environment may need simulator-specific setup.
- The FIFO implementation assumes `DEPTH` is a power of two.

## Reproduction

Use the commands recorded in `metadata/run.json` from `harness/examples/fifo-sync/runs/0001`.
