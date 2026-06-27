# Skill: Yosys Debug

## Triggers

- Yosys rejects RTL.
- Yosys `check` reports structural problems.
- Synthesis passes but reports warnings that may indicate unintended hardware.

## Common Classes

- unsupported SystemVerilog construct;
- inferred latch;
- multiple drivers;
- combinational loop;
- width mismatch;
- unconnected port.

## Process

1. Parse the Yosys failure.
2. Determine whether RTL is unsynthesizable or the script is wrong.
3. Prefer conservative RTL rewrites.
4. Rerun lint and simulation before declaring synthesis fixed.

## Rule

Synthesis fixes must not break simulation behavior.

## Validation

- Rerun Yosys after the repair.
- Rerun Verilator lint and simulation if RTL changed.
- Record cell counts and important warnings in the final report.

## Forbidden Repairs

- Do not remove logic just to eliminate a synthesis warning.
- Do not replace a protocol feature with a simpler behavior unless the goal allows it.
