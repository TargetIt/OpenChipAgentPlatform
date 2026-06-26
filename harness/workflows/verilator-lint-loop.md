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

Verilator lint exits successfully, or remaining warnings are documented and accepted by a human review gate.

