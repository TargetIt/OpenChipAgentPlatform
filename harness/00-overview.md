# Harness Overview

OpenChipAgent Harness is a set of rules, workflows, schemas, templates, and skills that make a general-purpose coding agent useful for chip design.

It is intentionally runtime-agnostic. It should be usable from:

- OpenCode;
- Claude Code;
- Codex;
- Cursor;
- Aider;
- future agent runtimes.

## Product Formula

```text
OpenChipAgent Harness
  = goal specification
  + chip design workflow
  + EDA tool feedback
  + failure taxonomy
  + repair loops
  + artifact tracking
  + reusable skills
```

## Non-Goals

The harness does not initially try to:

- replace senior chip engineers;
- guarantee production signoff;
- complete complex SoC integration;
- solve all timing closure;
- automate CDC/RDC/DFT/UVM signoff;
- directly use leaked proprietary code.

## First Useful Capability

The first practical capability is:

```text
Spec -> RTL -> testbench -> lint -> simulation -> synthesis -> report
```

This path has objective tool feedback and a clear done condition.

## Evidence-First Rule

Every agent run should produce evidence:

- files;
- commands;
- logs;
- parsed failures;
- patches;
- rerun results;
- final report.

The platform should not rely on agent confidence. It should rely on reproducible artifacts.

