# Structured Spec

## Module

- Name:
- Purpose:
- Non-goals:

## Ports

| Name | Direction | Width | Required | Description |
| --- | --- | --- | --- | --- |

## Clock and Reset

- Clock name:
- Clock edge:
- Reset name:
- Reset polarity:
- Reset style:
- Reset guarantees:

## Functional Behavior

Describe behavior in ordered rules. Each rule should be testable.

1.

## Protocol Rules

Describe valid input/output handshakes, backpressure, stalls, bubbles, and illegal sequences.

## Latency and Throughput

- Minimum latency:
- Maximum latency:
- Steady-state throughput:

## Corner Cases

- Reset during activity:
- Empty/full/boundary state:
- Back-to-back transactions:
- Stalls/backpressure:
- Width or overflow behavior:

## Acceptance Tests

| Test ID | Scenario | Expected Result | Required |
| --- | --- | --- | --- |

## Assumptions

List assumptions that are not directly enforced by ports or tests.

## Open Questions

The agent must stop for clarification if this section is non-empty and the missing answer affects interface, reset, latency, or acceptance checks.
