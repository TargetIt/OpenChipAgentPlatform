# Skill: Synthesizable Verilog

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

