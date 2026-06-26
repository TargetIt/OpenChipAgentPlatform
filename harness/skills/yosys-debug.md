# Skill: Yosys Debug

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

