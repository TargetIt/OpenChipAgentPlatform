# Codex Adapter

Codex can use OpenChipAgent Harness as a repository-local instruction set.

## Recommended Load Order

1. Read the goal.
2. Read `harness/04-goal-runner.md`.
3. Read the workflow for the stage.
4. Read relevant skills.
5. Run tools and preserve artifacts.

## Operating Rules

Codex should:

- prefer `rg` for searching;
- use existing project scripts where possible;
- avoid destructive git operations;
- never weaken completion checks to make a goal pass;
- record failures instead of hiding them;
- produce a concise final report.

