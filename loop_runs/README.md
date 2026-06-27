# Loop Runs

This directory stores concrete Harness/Loop validation runs. Each run should record the goal, execution target, evidence, final status, and product lessons.

Rules:

- A run report must distinguish local front-end checks from backend RTL-to-GDS checks.
- A final pass requires current-run evidence, not stale artifacts from an older delivery directory.
- Missing tools or skipped stages must be represented as non-pass states.
