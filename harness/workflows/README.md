# Workflows

Workflows define how an agent should execute chip design goals.

Each workflow should specify:

- inputs;
- expected artifacts;
- tools to run;
- default command templates;
- failure classes;
- repair strategy;
- done condition.

For the RTL MVP, workflows should preserve evidence according to `harness/02-run-layout.md`.
