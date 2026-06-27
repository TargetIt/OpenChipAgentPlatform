# Goal

## Identity

- ID:
- Title:
- Run directory:

## Design Intent

Describe the module in one paragraph. Include what the module does, what it must not do, and the intended operating context.

## Target

- Module name:
- Language:
- Top RTL file:

## Interface Requirements

| Signal | Direction | Width | Meaning |
| --- | --- | --- | --- |
| clk | input | 1 | Clock |
| rst | input | 1 | Reset |

## Timing and Protocol

- Clock:
- Reset:
- Latency:
- Handshake:
- Throughput:

## Acceptance Checks

- [ ] Structured spec has no unresolved questions.
- [ ] RTL exists and matches the declared interface.
- [ ] Verilator lint passes.
- [ ] Simulation passes required directed and randomized tests.
- [ ] Yosys synthesis passes.
- [ ] Final report lists artifacts, commands, failures, fixes, and risks.

## Retry Budget

- Maximum repair attempts per repeated failure class:
- Stop condition after budget is exhausted:

## Human Review Gates

List any goal-specific gates beyond `harness/03-human-review-gates.md`.
