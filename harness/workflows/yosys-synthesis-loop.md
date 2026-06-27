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

## Default Script

```tcl
read_verilog -sv rtl/<module>.sv
hierarchy -check -top <module>
proc
opt
check
stat
```

Save this as `scripts/synth.ys` and run:

```bash
yosys -q -s scripts/synth.ys \
  > logs/yosys.stdout.log \
  2> logs/yosys.stderr.log
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

Yosys synthesis passes, `check` reports no critical structural issue, and the final report includes key warnings, cell counts, and remaining risks.
