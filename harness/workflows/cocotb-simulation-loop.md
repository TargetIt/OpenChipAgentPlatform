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

## Default Command

```bash
make -C tb MODULE=<module> TOPLEVEL=<module> \
  > logs/cocotb.stdout.log \
  2> logs/cocotb.stderr.log
```

Record simulator, random seed, waveform path, and test selection in `metadata/run.json`.

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

All required tests pass, deterministic seed reproduction is recorded, and the final report lists coverage limitations.

## Minimum Test Expectations

For the RTL MVP, the testbench should include:

- reset behavior;
- one normal transaction;
- boundary conditions;
- backpressure or stall behavior when the protocol has flow control;
- at least one randomized sequence with recorded seed.
