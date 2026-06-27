# Cursor Adapter

Cursor can use OpenChipAgent Harness as repository-local context for interactive chip-design edits.

## Recommended Context

Load these files into the session before asking Cursor to run a goal:

1. `harness/README.md`
2. `harness/02-run-layout.md`
3. `harness/03-human-review-gates.md`
4. `harness/04-goal-runner.md`
5. the relevant workflow under `harness/workflows/`
6. the relevant skills under `harness/skills/`

## Usage Pattern

```text
Use OpenChipAgent Harness.
Create a run directory following harness/02-run-layout.md.
Do not stop until required checks pass or a blocker is classified.
Record commands, artifacts, failures, repairs, and final report.
```

## Limitations

Cursor is strongest when the user supervises edits inside an IDE. For long-running automated loops, preserve command output under `logs/` and keep `metadata/run.json` current so another agent can resume.
