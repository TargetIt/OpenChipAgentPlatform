# Agent Host Adapters

This directory describes how to use the same OpenChipAgent Harness from different general-purpose agent hosts.

The harness should be runtime-agnostic.

Supported host targets:

- OpenCode;
- Claude Code;
- Codex;
- Cursor;
- Aider.

Each adapter should explain:

- how to load the harness context;
- which files the agent should read first;
- how to run goals;
- how to preserve artifacts;
- what the host-specific limitations are.

All adapters should point agents at `harness/02-run-layout.md` and `harness/03-human-review-gates.md`.
