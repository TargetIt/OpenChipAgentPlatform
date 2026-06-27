# Human Review Gates

The harness should let agents repair ordinary implementation mistakes, but it must stop before changing the meaning of the task or weakening evidence.

## Must Ask Before

The agent must ask for human review before:

- changing the goal or user-visible design requirements;
- weakening acceptance tests;
- deleting assertions;
- suppressing warnings to make tools pass;
- skipping lint, simulation, or synthesis;
- changing reset, latency, or protocol semantics after spec approval;
- accepting a simulation mismatch as harmless;
- declaring success with missing logs or missing command records;
- using leaked proprietary code or unclear-license code.

## Safe Automatic Repairs

These are usually safe when supported by tool evidence:

- fixing syntax errors;
- adding missing declarations;
- correcting width casts with explicit sizing;
- replacing unsupported syntax with equivalent conservative RTL;
- adding default assignments to remove unintended latches;
- fixing testbench import paths or build paths.

## Unsafe Automatic Repairs

These require review unless the spec explicitly allows them:

- changing visible interface ports;
- changing cycle latency;
- changing ready/valid behavior;
- reducing FIFO depth or data width;
- removing reset behavior;
- removing corner-case tests;
- masking X or Z values without explaining the root cause.

## Report Requirement

Every human review gate must appear in `metadata/run.json` and `reports/final.md` with:

- the reason review was needed;
- the evidence that triggered it;
- the available options;
- the agent's recommended next action.
