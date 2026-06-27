# Aider Adapter

Aider can use OpenChipAgent Harness as a text-first editing workflow for small RTL tasks.

## Recommended Context

Start by adding or referencing:

1. `harness/README.md`
2. `harness/02-run-layout.md`
3. `harness/03-human-review-gates.md`
4. `harness/workflows/rtl-goal-runner.md`
5. required templates and skills

## Usage Pattern

```text
Follow OpenChipAgent Harness.
Create or update only the files needed for the current run.
After each repair, rerun the invalidated checks and update metadata/run.json.
```

## Limitations

Aider is well suited for focused patch loops. It should avoid broad refactors unless the current failure evidence requires them.
