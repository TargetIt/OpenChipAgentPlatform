# Hermes-Style Skill Memory

Hermes-style learning is useful because EDA failures repeat.

The harness should eventually convert repeated failures into reusable skills.

## Skill Memory Goal

```text
same failure pattern
  -> recognized faster next time
  -> repaired with a known strategy
  -> measured by success rate
```

## Example Skills

### Inferred Latch

Trigger:

```text
Yosys or Verilator warns that a latch is inferred.
```

Repair principle:

```text
Ensure every combinational output is assigned on every branch.
Add default assignments at the top of always_comb.
```

### Multiple Drivers

Trigger:

```text
Same signal assigned in multiple always blocks or continuous assignments.
```

Repair principle:

```text
Find all writers.
Choose one ownership block.
Convert competing assignments into next-state logic if needed.
```

### Unsupported SystemVerilog Syntax

Trigger:

```text
Yosys rejects a construct that Verilator accepts.
```

Repair principle:

```text
Rewrite into conservative synthesizable Verilog/SystemVerilog subset.
```

## Skill Lifecycle

1. Observe failure.
2. Classify failure.
3. Record effective repair.
4. Convert repair into skill file.
5. Reuse skill on future failures.
6. Track hit rate and success rate.

## Initial Policy

Start with manually curated skill files. Add automatic skill extraction only after the loops and artifacts are stable.

