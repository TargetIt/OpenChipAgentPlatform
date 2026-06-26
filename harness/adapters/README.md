# Agent Host Adapters

This directory describes how to use the same OpenChipAgent Harness from different general-purpose agent hosts.

The harness should be runtime-agnostic.

Supported host targets:

- OpenCode;
- Claude Code;
- Codex;
- later Cursor and Aider.

Each adapter should explain:

- how to load the harness context;
- which files the agent should read first;
- how to run goals;
- how to preserve artifacts;
- what the host-specific limitations are.

