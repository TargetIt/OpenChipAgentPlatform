# Schemas

Schemas define durable structures for goal-driven chip design runs.

## Core Schemas

- `goal.schema.json`: the input objective and acceptance checks.
- `run.schema.json`: the full reproducibility record for one run.
- `command.schema.json`: one tool invocation with logs and exit status.
- `artifact.schema.json`: one produced file or report.
- `failure.schema.json`: one classified failure with evidence.
- `repair-action.schema.json`: one attempted repair and its validation.
- `skill.schema.json`: reusable failure-diagnosis and repair knowledge.

## Policy

Schemas should stay strict enough that two different agents produce comparable run records. Add fields deliberately; do not hide important data in free-form text when a structured field is useful.
