# Skill: Verilator Debug

## Triggers

- Verilator exits with a non-zero code.
- Verilator emits warnings that affect correctness, width, initialization, or synthesizable style.

## Common Classes

- syntax error;
- undeclared signal;
- width mismatch;
- unused signal;
- inferred latch;
- multiple drivers.

## Process

1. Read the first real error, not only the last line.
2. Map error to source location.
3. Classify using `failure.schema.json`.
4. Patch the smallest safe change.
5. Rerun lint.

## Safety

Do not suppress warnings just to pass. Suppression requires human review and a written reason.

## Validation

- Rerun the exact Verilator command after each repair.
- If RTL changed, rerun simulation before declaring the design fixed.
- Record the first failing log path and the passing rerun log path in `metadata/run.json`.
