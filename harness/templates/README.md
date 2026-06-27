# Templates

Templates are copied into real runs and then filled by the agent.

## Required Templates

- `goal-template.md`: human-readable goal definition.
- `spec-template.md`: structured module specification.
- `final-report-template.md`: final evidence report.

## Template Rule

Templates should be specific enough that a general coding agent fills them consistently. Avoid vague `TODO` placeholders in completed runs; unresolved fields should move to an explicit `Open Questions` or `Human Review Gates` section.
