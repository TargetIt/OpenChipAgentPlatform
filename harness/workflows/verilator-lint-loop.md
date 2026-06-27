# Verilator Lint Loop

## Purpose

Use Verilator to catch syntax, lint, width, reset, and synthesizable-style issues early.

## Loop

```text
run Verilator
  -> parse errors/warnings
  -> classify
  -> patch RTL if safe
  -> rerun
```

## Default Command

```bash
verilator --lint-only -Wall rtl/<module>.sv \
  > logs/verilator-lint.stdout.log \
  2> logs/verilator-lint.stderr.log
```

If the project has include directories or multiple RTL files, add them explicitly and record the final command in `metadata/run.json`.

## Common Failure Classes

- syntax error;
- undeclared signal;
- width mismatch;
- multiple drivers;
- incomplete assignment;
- blocking/non-blocking misuse;
- unused signal;
- unsupported construct.

## Done Condition

Verilator exits successfully with no unreviewed warnings. Suppressed or accepted warnings must be documented as human review gates.
