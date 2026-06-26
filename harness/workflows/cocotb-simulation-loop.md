# cocotb Simulation Loop

## Purpose

Use cocotb or equivalent simulation to verify behavior against the structured spec.

## Loop

```text
generate tests
  -> run simulation
  -> compare expected vs actual
  -> classify mismatch
  -> patch RTL, testbench, or spec
  -> rerun
```

## Mismatch Classification

- RTL bug;
- testbench bug;
- reference model bug;
- spec ambiguity;
- reset timing issue;
- handshake protocol violation;
- latency mismatch;
- corner case missing.

## Done Condition

All required tests pass and the final report lists test coverage limitations.

