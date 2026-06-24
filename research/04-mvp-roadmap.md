# MVP Roadmap

## Phase 0: Research and Design

Goal: define product boundary, toolchain assumptions, and benchmark strategy.

Deliverables:

- landscape survey;
- architecture proposal;
- MVP workflow;
- initial tool wrapper design;
- benchmark selection.

## Phase 1: Verified RTL MVP

Goal: natural language to verified small RTL module.

Workflow:

```text
user prompt
  -> structured spec
  -> RTL generation
  -> testbench generation
  -> Verilator lint
  -> cocotb / Icarus simulation
  -> automatic repair loop
  -> final verified RTL report
```

Must-have features:

- project/run directory creation;
- generated RTL file;
- generated testbench file;
- repeatable simulation command;
- parsed simulation errors;
- patch loop with max retry count;
- final report.

Suggested initial tasks:

- counter;
- FIFO;
- arbiter;
- UART transmitter;
- simple AXI-lite register block;
- small ALU;
- pipelined multiplier.

Exit criteria:

- can solve several small modules end-to-end;
- failures are reported clearly;
- all generated artifacts are saved;
- user can rerun the flow locally.

## Phase 2: Synthesis MVP

Goal: verified RTL to synthesized netlist and synthesis report.

Workflow:

```text
verified RTL
  -> Yosys synthesis
  -> netlist
  -> area / cell report
  -> synthesis warning analysis
```

Must-have features:

- Yosys wrapper;
- standard synthesis script template;
- area/cell report parser;
- unsupported construct detection;
- synthesis-aware repair loop.

Exit criteria:

- verified RTL can be synthesized with Yosys;
- report is understandable to non-expert users;
- common synthesis failures can be explained.

## Phase 3: RTL-to-GDS Prototype

Goal: run a known-good small design through OpenROAD/OpenLane.

Workflow:

```text
synthesizable RTL
  -> OpenLane/OpenROAD
  -> floorplan
  -> placement
  -> routing
  -> timing report
  -> DEF/GDS output
```

Must-have features:

- Dockerized OpenLane/OpenROAD environment;
- PDK setup strategy;
- timing report parser;
- failed-stage detection;
- final artifact collection.

Recommended PDK targets:

- SkyWater SKY130 for first experiments;
- IHP SG13G2 later if mixed-signal / RF exploration matters.

Exit criteria:

- at least one simple design reaches final layout;
- timing and area reports are summarized;
- user can inspect generated layout with KLayout.

## Phase 4: Benchmark and Regression

Goal: evaluate agent performance objectively.

Benchmarks:

- RTLLM;
- VerilogEval;
- TuRTLe;
- custom small-IP benchmark suite.

Metrics:

- syntax pass rate;
- simulation pass rate;
- synthesis pass rate;
- average repair iterations;
- token / runtime cost;
- report quality;
- reproducibility.

## Phase 5: Product UX

Goal: make the system usable by non-experts.

Interfaces:

- CLI first;
- web UI second;
- VSCode extension later.

Core UX:

- show workflow graph;
- show current stage;
- show files generated;
- show failures and suggested fixes;
- show final report;
- allow user approval before risky edits.

## Recommended Immediate Next Step

Build Phase 1 only:

```text
SpecAgent + RTLAgent + TestbenchAgent + VerificationAgent + DebugAgent
```

Use Verilator and cocotb first. Do not start with OpenROAD/OpenLane until the simulation repair loop is stable.

