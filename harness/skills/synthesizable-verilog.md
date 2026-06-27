# Skill: Synthesizable Verilog

## Triggers

- New RTL is being generated.
- Yosys rejects syntax that Verilator accepted.
- A repair could be written in either advanced SystemVerilog or conservative RTL.

## Rule

Generate conservative synthesizable Verilog/SystemVerilog unless the goal explicitly allows advanced constructs.

## Prefer

- `always_ff` for sequential logic;
- `always_comb` for combinational logic;
- explicit reset behavior;
- sized constants;
- single writer per register;
- complete combinational assignments.

## Avoid

- delays;
- initial-only behavior for synthesizable state;
- dynamic arrays;
- unsynthesizable classes;
- ambiguous latches;
- multiple procedural drivers.

## Validation

- Run Verilator lint.
- Run simulation after behavioral edits.
- Run Yosys synthesis before declaring the RTL complete.

## Forbidden Repairs

- Do not remove behavior just because it is hard to synthesize.
- Do not change ports, reset semantics, or latency without a human review gate.
