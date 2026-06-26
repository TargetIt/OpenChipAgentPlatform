# Yosys Synthesis Loop

## Purpose

Use Yosys to check whether RTL is synthesizable and to produce an initial synthesis report.

## Loop

```text
run Yosys
  -> parse synthesis errors/warnings
  -> classify
  -> patch RTL if safe
  -> rerun lint, simulation, and synthesis
```

## Common Failure Classes

- non-synthesizable construct;
- inferred latch;
- multiple drivers;
- unsupported SystemVerilog syntax;
- combinational loop;
- width mismatch;
- unconnected port;
- unsized constant risk.

## Done Condition

Yosys synthesis passes and the final report includes key warnings, cell counts, and remaining risks.

