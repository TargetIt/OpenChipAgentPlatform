# Claude Code Adapter

Claude Code can be used as a host runtime for OpenChipAgent Harness.

## Recommended Pattern

Use a goal-oriented prompt and explicitly point Claude Code at the harness files.

```text
Read harness/README.md and harness/10-mvp-rtl-goal-runner.md.
Use the RTL Goal Runner workflow.
Do not stop until the done checks pass or a blocker is clearly reported.
```

## Review Gates

For risky changes, ask the user before:

- changing the goal;
- weakening tests;
- removing assertions;
- skipping synthesis;
- declaring success without tool evidence.

## Artifact Rule

Claude Code should preserve:

- spec;
- RTL;
- testbench;
- commands;
- logs;
- patches;
- report.

