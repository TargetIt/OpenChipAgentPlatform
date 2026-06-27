# Example: Synchronous Ready/Valid FIFO

This example shows the intended first-stage harness shape for a small RTL goal.

It is an example run package, not a generated production IP block. The purpose is to demonstrate:

- canonical run layout;
- structured goal and spec;
- RTL artifact;
- cocotb testbench shape;
- Verilator and Yosys command records;
- final report format.

## Run Directory

```text
harness/examples/fifo-sync/runs/0001/
  goal.json
  spec/spec.md
  rtl/fifo_sync.sv
  tb/Makefile
  tb/test_fifo_sync.py
  scripts/synth.ys
  logs/.gitkeep
  metadata/run.json
  reports/final.md
```

## Intended Commands

```bash
cd harness/examples/fifo-sync/runs/0001
verilator --lint-only -Wall rtl/fifo_sync.sv
make -C tb MODULE=test_fifo_sync TOPLEVEL=fifo_sync TOPLEVEL_LANG=verilog VERILOG_SOURCES="$(pwd)/rtl/fifo_sync.sv"
yosys -q -s scripts/synth.ys
```
