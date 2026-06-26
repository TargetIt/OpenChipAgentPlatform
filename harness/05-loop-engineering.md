# Loop Engineering

The harness is built around loops.

The basic loop is:

```text
generate
  -> run tool
  -> parse result
  -> classify failure
  -> patch
  -> rerun
```

## Spec Loop

```text
user prompt
  -> extract ports, clocks, reset, protocol, latency, corner cases
  -> generate spec.md
  -> ask clarifying questions if required fields are missing
```

## RTL Loop

```text
spec.md
  -> generate RTL
  -> run lint
  -> classify syntax/lint failures
  -> patch RTL
  -> rerun lint
```

## Verification Loop

```text
spec.md + RTL
  -> generate reference model
  -> generate tests
  -> run simulation
  -> classify mismatch
  -> patch RTL, testbench, or spec
  -> rerun
```

## Synthesis Loop

```text
verified RTL
  -> run Yosys
  -> parse unsupported syntax / latch / multi-driver / width mismatch
  -> patch RTL
  -> rerun lint + simulation + synthesis
```

## Backend Loop

```text
synthesizable RTL
  -> run OpenLane/OpenROAD
  -> identify failed stage
  -> parse timing / congestion / routing / DRC failures
  -> propose config, constraint, or RTL change
  -> rerun selected stage
```

Backend loops are phase-two. The first stable loop should be RTL + verification + synthesis.

