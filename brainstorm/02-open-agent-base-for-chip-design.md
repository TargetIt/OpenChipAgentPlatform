# Brainstorm: Building a Chip Design Agent on Open Agent Foundations

## 1. Background

The user asked whether recent open-source agent projects and industry events create an opportunity to build a chip-design-specific agent.

The mentioned signals include:

- OpenCode and similar open-source coding agents;
- Hermes Agent becoming open source;
- Claude Code source leakage as an industry signal;
- prior research into chip-design agents and open-source EDA tools.

The important distinction:

> Open-source projects such as OpenCode and Hermes can be used as legal technical foundations. Leaked proprietary code should not be copied, modified, or used as a product dependency.

Claude Code leaks may reveal market direction and product patterns, but they should only be treated as external industry signals, not as a code source.

## 2. Core Question

Can we take open-source agent infrastructure, adapt it, and build a specialized chip design agent platform?

Short answer:

> Yes. The opportunity is real, but the winning product is not a generic coding agent clone. It is a chip-design-specific agent harness and EDA loop platform.

The product should not be:

```text
generic coding agent + chip design prompts
```

It should be:

```text
chip design agent runtime
  = open agent foundation
  + chip design workflow
  + EDA tool adapters
  + goal-driven loops
  + harness constraints
  + RTL / verification / synthesis / backend knowledge
  + reproducible artifact system
```

## 3. Demand-Side Possibility

There is real user demand, but it must be framed correctly.

The market does not yet need a product that claims:

```text
AI automatically designs production SoCs from natural language
```

That would be overpromising.

The real demand is:

```text
Help users automate repetitive, fragmented, log-driven, feedback-driven chip design work.
```

## 4. Potential Customers

### 4.1 Learners and Universities

Pain points:

- Verilog learning is hard;
- toolchain setup is painful;
- EDA errors are difficult to understand;
- RTL-to-GDS flow is fragmented;
- students need guided feedback.

Potential value:

- guided RTL generation;
- automatic simulation;
- clear error explanation;
- report summaries;
- educational flow visualization.

### 4.2 Open-Source Hardware Developers

Pain points:

- writing small IP blocks is repetitive;
- testbench generation takes time;
- Verilator/Yosys/OpenLane errors are tedious;
- open-source flows require manual glue scripts.

Potential value:

- quick module generation;
- automated verification loop;
- synthesis check;
- OpenLane/OpenROAD flow assistance.

### 4.3 Chip Startups and Small Teams

Pain points:

- early architecture exploration is expensive;
- engineers spend time on boilerplate RTL and flow scripts;
- EDA report interpretation is repetitive;
- internal tooling is often underdeveloped.

Potential value:

- early prototype generation;
- regression and synthesis automation;
- timing/area report summarization;
- design-space exploration assistance.

Important boundary:

This should support early-stage work and productivity, not replace signoff or senior chip engineers.

### 4.4 EDA / AI Researchers

Pain points:

- LLM-for-EDA evaluation is fragmented;
- benchmark execution is inconsistent;
- generated RTL quality is hard to compare.

Potential value:

- unified benchmark harness;
- RTLLM / VerilogEval / TuRTLe integration;
- reproducible evaluation reports.

### 4.5 Internal Platform Teams

Pain points:

- companies want internal EDA copilots;
- commercial tools are expensive and closed;
- workflow automation is highly customized.

Potential value:

- open-source starting point;
- pluggable tool adapters;
- internal deployment;
- private model and local EDA support.

## 5. Technical Possibility

The first-stage technical goal is feasible:

```text
natural language spec
  -> RTL
  -> testbench
  -> Verilator lint
  -> cocotb / Icarus simulation
  -> automatic repair
  -> Yosys synthesis
  -> report summary
```

This can be built today from available components:

- OpenCode-style agent runtime;
- Hermes-style memory and skill learning;
- Verilator / Icarus / cocotb feedback;
- Yosys synthesis feedback;
- RTLLM / VerilogEval / TuRTLe for evaluation;
- structured artifacts and run manifests.

Second-stage technical goal:

```text
verified RTL
  -> OpenLane / OpenROAD
  -> floorplan / placement / routing
  -> timing report parsing
  -> failure diagnosis
  -> rerun loop
```

This is feasible but significantly harder.

Third-stage technical goal:

```text
complex SoC
  -> full verification
  -> CDC / RDC / DFT
  -> timing closure
  -> signoff-quality flow
```

This should not be the initial goal.

## 6. Engineering Possibility

The engineering core is the harness.

A useful chip design agent needs a standard project structure:

```text
chip_project/
  spec/
  rtl/
  tb/
  sim/
  synth/
  pnr/
  reports/
  runs/
  skills/
  manifests/
```

Each run should save:

- original prompt;
- structured spec;
- generated RTL;
- generated testbench;
- commands;
- logs;
- waveforms;
- synthesis reports;
- timing reports;
- patches;
- retry count;
- final result.

The loop should be explicit:

```text
run tool
  -> parse result
  -> classify failure
  -> patch
  -> rerun
  -> stop only when goal condition is satisfied
```

## 7. Candidate Product Forms

### 7.1 OpenChipAgent Runtime

A chip-design-specific runtime built on top of open-source agent infrastructure.

Example:

```text
/chip-goal "Generate an async FIFO. Verilator lint must be clean, cocotb tests must pass, and Yosys synthesis must pass."
```

This is not a general coding assistant. It is a chip design workflow runner.

### 7.2 RTL Debug Loop

A focused product for RTL repair.

Loop:

```text
Verilator error
  -> locate source line
  -> explain error
  -> patch RTL
  -> rerun

simulation mismatch
  -> compare expected vs actual
  -> inspect reference model
  -> decide RTL bug or testbench bug
  -> patch
  -> rerun
```

This is likely the best MVP because the feedback signal is clear.

### 7.3 EDA Log Intelligence

A product focused on reading and explaining EDA logs.

Inputs:

- Yosys log;
- Verilator log;
- cocotb log;
- OpenROAD log;
- OpenLane logs;
- timing reports;
- DRC/LVS reports.

Outputs:

- failed stage;
- root cause;
- severity;
- likely fix;
- patch proposal;
- rerun command.

### 7.4 Chip Skill Memory

A Hermes-inspired skill memory for EDA.

Examples:

```text
latch inferred
  -> skill: assign every output in every combinational branch

multiple drivers
  -> skill: identify all always blocks and continuous assignments writing the same net

unsupported Yosys syntax
  -> skill: rewrite into conservative synthesizable Verilog

cocotb mismatch
  -> skill: compare reference model, transaction timing, reset behavior

setup timing violation
  -> skill: classify constraint issue vs pipeline issue vs long combinational path
```

This could become a durable product moat.

### 7.5 Open-Source Chip Design Workbench

A UI-oriented product for education and community adoption.

Features:

- project dashboard;
- workflow graph;
- RTL/testbench/report viewer;
- one-click rerun;
- agent explanations;
- run history;
- artifact browser.

## 8. Competitive Analysis

The product should not compete directly with general coding agents.

General coding agents:

- understand code broadly;
- edit files;
- run tests;
- support many languages;
- optimize for general software engineering.

OpenChipAgentPlatform should specialize in:

- RTL semantics;
- hardware timing;
- simulation and waveform evidence;
- synthesis constraints;
- open-source EDA toolchains;
- physical design reports;
- PDK-aware flows;
- chip design benchmark harnesses.

The competitive wedge:

```text
General coding agents know code.
OpenChipAgent understands chip design loops.
```

## 9. Product Competitiveness

The product can be competitive if it builds depth in areas that generic agents ignore:

1. EDA tool adapters.
2. Log and report parsers.
3. RTL repair loops.
4. Verifiable chip-design goals.
5. PDK and OpenLane/OpenROAD integration.
6. Persistent EDA skill memory.
7. Benchmark-driven evaluation.
8. Reproducible artifact management.

The moat is not the base model.

The moat is:

```text
chip-specific harness + EDA feedback loops + accumulated repair skills
```

## 10. Suggested Build Strategy

### Phase 1: Legal Open Agent Foundation

Use only legal open-source agent infrastructure.

Possible references:

- OpenCode-style coding agent architecture;
- Hermes-style memory and skill learning;
- existing open-source agent runtimes and plugin systems.

Do not use leaked proprietary code.

### Phase 2: Verified RTL Goal Runner

Build the first useful goal:

```text
Given a natural language spec,
generate synthesizable RTL,
generate tests,
pass Verilator lint,
pass cocotb simulation,
pass Yosys synthesis,
produce a report.
```

### Phase 3: EDA Log Parser Library

Build parsers for:

- Verilator;
- Icarus;
- cocotb;
- Yosys;
- OpenLane;
- OpenROAD.

### Phase 4: Skill Memory

Start with explicit skill files.

Later add automatic skill generation from repeated failures.

### Phase 5: Backend Flow Integration

Add OpenLane/OpenROAD goals:

```text
/chip-goal Produce final.gds for this small design using SKY130.
```

## 11. Key Risks

### 11.1 Legal Risk

Using leaked proprietary code would create major risk.

Mitigation:

- use only open-source licensed code;
- document dependencies and licenses;
- treat leaks only as product-signal context.

### 11.2 Technical Overreach

Trying to support full SoC design too early will likely fail.

Mitigation:

- start with small RTL modules;
- add synthesis after simulation is stable;
- add physical design only later.

### 11.3 Weak Verification

If tests are weak, the agent can produce incorrect RTL that appears to pass.

Mitigation:

- use independent reference models;
- add randomized tests;
- use benchmark tasks;
- eventually add formal verification.

### 11.4 Toolchain Fragility

Open-source EDA tools can be difficult to install and configure.

Mitigation:

- Dockerize toolchains;
- pin versions;
- provide standard project templates;
- save manifests.

## 12. Conclusion

There is a real opportunity.

The best product is not:

```text
another Claude Code clone
```

The best product is:

```text
a chip-design-specific agent harness and EDA loop platform
```

It should use open-source agent foundations where legal and useful, but create its own differentiation in the chip-specific workflow:

- RTL generation;
- test generation;
- simulation repair;
- synthesis repair;
- EDA log intelligence;
- OpenROAD/OpenLane integration;
- skill memory;
- reproducible evidence.

This direction has demand-side possibility, technical possibility, engineering feasibility, and product differentiation if scoped carefully.

