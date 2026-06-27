# Structured Spec: `fifo_sync`

## Module

- Name: `fifo_sync`
- Purpose: store data words in first-in-first-out order between a push side and a pop side.
- Non-goals: asynchronous clocks, CDC handling, AXI compatibility, production timing closure.

## Parameters

| Name | Default | Meaning |
| --- | --- | --- |
| `WIDTH` | 8 | Data width |
| `DEPTH` | 4 | Number of entries |

## Ports

| Name | Direction | Width | Required | Description |
| --- | --- | --- | --- | --- |
| `clk` | input | 1 | yes | Rising-edge clock |
| `rst` | input | 1 | yes | Synchronous active-high reset |
| `push_valid` | input | 1 | yes | Producer has a word to write |
| `push_ready` | output | 1 | yes | FIFO can accept a word |
| `push_data` | input | `WIDTH` | yes | Word to write |
| `pop_valid` | output | 1 | yes | FIFO has a word available |
| `pop_ready` | input | 1 | yes | Consumer accepts the current word |
| `pop_data` | output | `WIDTH` | yes | Oldest available word |
| `full` | output | 1 | yes | FIFO occupancy equals `DEPTH` |
| `empty` | output | 1 | yes | FIFO occupancy is zero |

## Clock and Reset

- Clock name: `clk`
- Clock edge: rising
- Reset name: `rst`
- Reset polarity: active high
- Reset style: synchronous
- Reset guarantees: after reset, occupancy is zero, `empty=1`, `full=0`, `push_ready=1`, `pop_valid=0`.

## Functional Behavior

1. A push occurs on a rising clock edge when `push_valid && push_ready`.
2. A pop occurs on a rising clock edge when `pop_valid && pop_ready`.
3. Pushed words are returned in the same order.
4. `push_ready` is low when the FIFO is full.
5. `pop_valid` is low when the FIFO is empty.
6. Simultaneous push and pop are allowed when the FIFO is neither reset-blocked nor structurally invalid.
7. `pop_data` shows the oldest stored word whenever `pop_valid` is high.

## Protocol Rules

- The producer may hold `push_valid` high until `push_ready` accepts the word.
- The consumer may hold `pop_ready` low to apply backpressure.
- Push while full is not accepted because `push_ready=0`.
- Pop while empty is not accepted because `pop_valid=0`.

## Latency and Throughput

- Minimum latency: a pushed word is observable after the write edge when it becomes the oldest entry.
- Maximum latency: bounded by consumer backpressure and older entries.
- Steady-state throughput: one push and one pop per cycle when neither side stalls.

## Corner Cases

- Reset during activity clears the FIFO.
- Fill exactly to `DEPTH`.
- Drain exactly to empty.
- Back-to-back pushes.
- Back-to-back pops.
- Simultaneous push and pop.

## Acceptance Tests

| Test ID | Scenario | Expected Result | Required |
| --- | --- | --- | --- |
| reset | Assert reset | FIFO becomes empty and ready for push | yes |
| single-word | Push one word then pop it | Same word appears on pop side | yes |
| fill-drain | Push `DEPTH` words and drain | Ordering preserved, full/empty flags correct | yes |
| backpressure | Hold `pop_ready=0` | Data remains stable while stalled | yes |
| randomized | Random push/pop sequence | Model queue matches RTL output | yes |

## Assumptions

- `DEPTH` is at least 2.
- `DEPTH` is a power of two for this example implementation.
- `push_data` is stable when `push_valid && !push_ready`.

## Open Questions

None.
