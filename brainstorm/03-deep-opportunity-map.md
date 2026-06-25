# Deep Opportunity Map: OpenChipAgentPlatform

## 1. Why This Opportunity Exists Now

The opportunity exists because three trends are converging.

### 1.1 Open Agent Runtime Is Becoming Commodity Infrastructure

Open-source coding agents such as OpenCode provide a reusable foundation for:

- terminal / IDE based agent operation;
- multi-model routing;
- tool invocation;
- file editing;
- subagent-style task decomposition;
- long-running development tasks.

Hermes-style agents add another important direction:

- persistent memory;
- reusable skills;
- learning loops;
- self-improvement from repeated work.

This means OpenChipAgentPlatform does not need to invent the entire agent runtime from scratch. The better opportunity is to specialize the runtime for chip design.

### 1.2 Open-Source EDA Has Become Usable Enough

Open-source EDA tools provide objective feedback loops:

- Verilator / Icarus for lint and simulation;
- cocotb for Python-based verification;
- Yosys for synthesis;
- OpenROAD / OpenLane for physical implementation;
- Magic / KLayout / Netgen for layout and checking;
- open PDKs such as SKY130 and IHP Open PDK.

The existence of these tools matters because chip design agents need objective feedback. Without tool feedback, the agent is just guessing.

### 1.3 Chip Design Workflow Is Still Fragmented

The user experience is still difficult:

- toolchain installation is painful;
- logs are long and specialized;
- testbench writing is hard;
- synthesis failures are hard to understand;
- OpenLane/OpenROAD failures are hard to diagnose;
- artifacts are scattered;
- beginners do not understand the full RTL-to-GDS path;
- even experienced engineers waste time on repetitive flow triage.

This gap creates room for an agentic harness layer.

## 2. First-Principles View

The core problem is not:

```text
Can an LLM write Verilog?
```

The deeper problem is:

```text
Can the system move a hardware design through objective engineering gates?
```

The useful gates are:

```text
spec is complete
RTL compiles
lint is clean
tests pass
RTL is synthesizable
synthesis report is understood
timing is understood
physical flow status is understood
artifacts are reproducible
```

Therefore, the correct product is not a chatbot. It is a goal-driven engineering loop.

## 3. Product Formula

```text
OpenChipAgentPlatform
  = Open Agent Runtime
  + Chip Design Harness
  + EDA Tool Loops
  + Goal Runner
  + Artifact Graph
  + Failure Taxonomy
  + Repair Actions
  + Skill Memory
```

The model is only one part of the product.

The differentiated product is the harness that turns model output into verified chip design progress.

## 4. Strongest Product Wedge

The strongest first wedge is:

```text
OpenChipAgent RTL Goal Runner
```

Example goal:

```text
/chip-goal Generate a synchronous FIFO:
  - width = 32
  - depth = 16
  - ready/valid interface
  - synchronous reset
  - Verilator lint clean
  - cocotb tests pass
  - Yosys synthesis pass
  - produce final report with artifacts
```

This is stronger than "generate Verilog" because it has verifiable completion conditions.

## 5. MVP Workflow

```text
Natural language spec
  -> Spec clarification
  -> structured spec.md
  -> RTL generation
  -> testbench generation
  -> Verilator lint
  -> cocotb / Icarus / Verilator simulation
  -> failure classification
  -> patch RTL or testbench
  -> rerun
  -> Yosys synthesis
  -> final report
```

## 6. Why Not Start With Natural Language to GDS

Natural language to GDS is exciting, but it is not the correct first product.

Reasons:

- physical design has many variables unrelated to RTL correctness;
- PDK and flow setup can dominate failures;
- timing closure is hard to automate safely;
- generated RTL must first be functionally correct;
- debugging a full physical flow without a stable RTL loop creates too many degrees of freedom.

The first product should make the RTL / verification / synthesis loop excellent.

OpenROAD/OpenLane should be phase two.

## 7. Product Opportunity Map

### 7.1 RTL Repair Loop Agent

Purpose:

```text
Fix RTL and testbench issues from objective tool feedback.
```

Inputs:

- RTL;
- testbench;
- Verilator log;
- cocotb log;
- waveform summary;
- Yosys log.

Outputs:

- root cause;
- patch;
- rerun result;
- final explanation.

Why it matters:

This is the most concrete and easiest-to-verify agent loop.

### 7.2 EDA Log Intelligence

Purpose:

```text
Turn long EDA logs into structured diagnosis and repair actions.
```

Supported logs:

- Verilator;
- Icarus;
- cocotb;
- Yosys;
- OpenROAD;
- OpenLane;
- STA;
- DRC/LVS.

Outputs:

- failed stage;
- severity;
- likely root cause;
- recommended repair;
- whether the repair is safe to automate;
- whether human review is required.

### 7.3 Chip Harness Studio

Purpose:

```text
Make open-source chip design flows reproducible and inspectable.
```

Responsibilities:

- project scaffold;
- Docker / devcontainer;
- tool version lock;
- PDK profile;
- run manifest;
- artifact graph;
- report viewer;
- approval gates.

### 7.4 OpenLane / OpenROAD Flow Copilot

Purpose:

```text
Help users run and understand backend open-source EDA flows.
```

Core capability:

- identify failed stage;
- parse stage-specific logs;
- explain what likely went wrong;
- propose config / constraint / RTL changes;
- rerun selected stages;
- summarize timing / area / congestion.

This is a phase-two product after RTL Goal Runner.

### 7.5 EDA Skill Memory

Purpose:

```text
Convert repeated failures into reusable skills.
```

Examples:

- latch inferred;
- multiple drivers;
- width mismatch;
- blocking/non-blocking misuse;
- reset behavior mismatch;
- unsupported Yosys syntax;
- setup timing violation;
- OpenLane routing congestion.

Skill records should include:

- trigger pattern;
- diagnosis;
- safe repair conditions;
- repair template;
- examples;
- counterexamples;
- success metrics.

### 7.6 Benchmark Platform

Purpose:

```text
Measure whether agents actually improve.
```

Metrics:

- syntax pass rate;
- lint pass rate;
- simulation pass rate;
- synthesis pass rate;
- retries to success;
- token cost;
- runtime;
- area;
- timing slack;
- human intervention count.

Potential benchmarks:

- RTLLM;
- VerilogEval;
- TuRTLe;
- custom small IP suite;
- OpenLane demo suite.

## 8. Customer Segments

### 8.1 Open-Source Hardware Developers

Pain:

- need small IP blocks;
- lack verification infrastructure;
- EDA logs are hard;
- toolchain setup is painful.

Best product:

- RTL Goal Runner;
- RTL Repair Loop;
- Yosys synthesis check;
- GitHub Action integration.

### 8.2 Universities and Learners

Pain:

- chip design learning path is fragmented;
- students do not understand why RTL fails;
- teachers need reproducible teaching flows.

Best product:

- guided lab environment;
- educational reports;
- visual flow graph;
- standard modules like FIFO, UART, ALU, AXI-lite register block.

### 8.3 Chip Startups and Small Teams

Pain:

- limited engineering bandwidth;
- early prototype bring-up is slow;
- logs and scripts consume time;
- need local / private deployment.

Best product:

- local RTL repair and synthesis loop;
- private artifact store;
- report intelligence;
- PPA exploration.

### 8.4 Enterprise CAD / EDA Teams

Pain:

- internal flows are complex;
- knowledge is scattered;
- repeated failures are not converted into reusable automation;
- need permission and audit.

Best product:

- private harness platform;
- internal adapter SDK;
- skill memory;
- team dashboard;
- enterprise audit.

## 9. Competitive Differentiation

General coding agents are strong at:

- editing code;
- reading repositories;
- running software tests;
- generating patches.

Chip design requires more:

```text
RTL compiles != hardware behavior is correct
simulation passes != RTL is synthesizable
synthesizable != timing closes
timing improves != routing succeeds
GDS generated != signoff quality
```

OpenChipAgentPlatform should differentiate on:

- EDA-aware goals;
- verification gates;
- tool adapters;
- log parsers;
- waveform summaries;
- synthesis and timing report understanding;
- PDK and flow profiles;
- artifact graph;
- chip-specific skill memory.

## 10. Moat

The moat should not be the base model.

The moat should be:

```text
EDA adapters
log parsers
failure taxonomy
repair loop library
artifact graph
chip-specific skills
benchmark data
PDK / OpenROAD / OpenLane know-how
community plugin ecosystem
```

This is hard for generic coding agents to prioritize because it is too domain-specific.

## 11. Core Data Structures

The platform should be designed around durable data structures.

### 11.1 goal.json

Records:

- user goal;
- design constraints;
- completion conditions;
- allowed tools;
- max retries;
- human approval rules.

### 11.2 run.json

Records:

- run id;
- timestamp;
- tool versions;
- commands;
- exit codes;
- logs;
- artifacts;
- parsed failures;
- patches;
- retry count;
- final status.

### 11.3 artifact graph

Connects:

- original prompt;
- structured spec;
- RTL files;
- testbench files;
- logs;
- waveforms;
- netlists;
- reports;
- patches;
- final summaries.

### 11.4 failure taxonomy

Examples:

- syntax error;
- lint warning;
- simulation mismatch;
- reference model error;
- testbench timing error;
- reset ambiguity;
- non-synthesizable construct;
- inferred latch;
- multiple drivers;
- width mismatch;
- timing violation;
- routing congestion.

### 11.5 repair action

Records:

- failure type;
- proposed fix;
- touched files;
- safety level;
- need for human approval;
- rerun command.

### 11.6 skill file

Records:

- trigger pattern;
- diagnosis;
- repair recipe;
- examples;
- success rate;
- last updated date.

## 12. Risk Map

### 12.1 Weak Tests

If the testbench is weak, bad RTL can pass.

Mitigation:

- independent reference models;
- randomized tests;
- coverage targets;
- benchmark tasks;
- formal checks later.

### 12.2 Ambiguous Specs

Natural language specs often omit reset, latency, handshake, overflow, and corner cases.

Mitigation:

- SpecAgent must ask clarifying questions;
- goal cannot start until minimum spec fields are filled;
- unknown assumptions must be listed.

### 12.3 Long Logs

EDA logs are too long for naive context stuffing.

Mitigation:

- deterministic parsers first;
- LLM summarization second;
- stage-specific extraction;
- source-location indexing.

### 12.4 Toolchain Drift

OpenROAD, OpenLane, Yosys, cocotb, and PDK versions can change results.

Mitigation:

- Docker images;
- pinned tool versions;
- run manifests;
- compatibility matrix.

### 12.5 Legal and License Risk

Leaked proprietary code must not be used.

Mitigation:

- only use legal open-source dependencies;
- maintain third-party notices;
- require contribution source declarations;
- license scanning in CI.

### 12.6 Overclaiming

"AI designs chips" is too broad and invites distrust.

Mitigation:

- position around verified goals;
- show pass/fail evidence;
- clearly state limitations.

## 13. Suggested Roadmap

### Phase 0: Research OS

- document requirements;
- survey open agent foundations;
- define harness schema;
- define run artifact model;
- choose license strategy.

### Phase 1: RTL Goal Runner

- support 5 to 10 small IP tasks;
- generate spec / RTL / testbench;
- run Verilator and cocotb;
- run Yosys;
- produce final report.

### Phase 2: EDA Log Intelligence

- build log parsers;
- classify common errors;
- add repair templates;
- build error knowledge base.

### Phase 3: OpenLane / OpenROAD Flow Runner

- scaffold OpenLane projects;
- run small designs to GDS;
- parse stage failures;
- summarize timing / area / congestion.

### Phase 4: Skill Memory

- manually curated skills first;
- automatic skill extraction later;
- track skill hit rate and repair success.

### Phase 5: Workbench / Enterprise

- web UI;
- team workspaces;
- private deployment;
- internal tool adapters;
- audit and permissions;
- benchmark dashboard.

## 14. Strong Product Language

Avoid:

```text
Natural language to chip
AI replaces chip engineers
One-click tapeout
```

Prefer:

```text
Goal-driven chip design agent platform
Open-source EDA loop harness
From spec to verified RTL
EDA loops, not just code generation
Reproducible chip design agent runs
```

## 15. Final Judgment

The opportunity is real.

But the winning product must focus on:

- verifiable goals;
- EDA feedback;
- reproducible artifacts;
- repair loops;
- skill accumulation;
- domain-specific workflow.

The correct first product is not a general agent and not a full chip autopilot.

The correct first product is:

```text
OpenChipAgent RTL Goal Runner
```

Once that loop is stable, the platform can expand toward OpenROAD/OpenLane, skill memory, benchmarks, and enterprise workflow integration.

