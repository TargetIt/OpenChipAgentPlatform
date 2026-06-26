# Why Harness First

The current opportunity is not to build another generic coding agent. Open-source and commercial coding agents already provide strong runtime capabilities:

- file editing;
- shell execution;
- repository navigation;
- tool calling;
- planning;
- long-running task execution.

The chip-design opportunity is to add a domain-specific harness that makes those agents reliable inside EDA workflows.

## Advantages

### Faster Validation

A harness can be used immediately with existing agents. This lets us test whether chip-specific workflows, schemas, templates, and skills improve real RTL outcomes.

### Lower Runtime Risk

Building a full agent runtime first would require solving:

- model providers;
- terminal UI;
- permissioning;
- workspace isolation;
- context management;
- editor integration;
- multi-agent orchestration.

Those are important later, but they are not the core chip-design moat.

### Portable Moat

If the harness works, it can move across runtimes:

```text
OpenCode today
Claude Code tomorrow
Codex later
Cursor / Aider as alternative hosts
```

### Domain Focus

The hard domain problems are:

- RTL correctness;
- testbench quality;
- lint/simulation/synthesis loops;
- EDA log diagnosis;
- artifact tracking;
- skill memory.

Harness-first keeps effort focused on these.

## Decision

The first implementation track should be:

```text
build the chip-design harness
use existing agents as hosts
avoid building a new runtime until the harness proves value
```

