# Brainstorm: Harness, Hermes, Loop Engineering, and Goal-Driven Chip Agents

## 1. Background

The user asked whether recent ideas such as Harness Engineering, Hermes Agent, Loop Engineering, and Claude-style `/goal` workflows can be combined with the chip-design agents and open-source EDA tools surveyed earlier.

The short answer is yes.

The stronger conclusion is:

> OpenChipAgentPlatform should not be just a collection of chip design agents. It should be a goal-driven chip design harness that runs verifiable EDA loops and accumulates reusable chip-design skills over time.

## 2. Concepts Being Combined

### 2.1 Harness Engineering

Harness Engineering is the practice of designing the environment that makes agents reliable.

For chip design, the harness includes:

- repository structure;
- tool versions;
- Docker images;
- PDK setup;
- permissions;
- run manifests;
- logs;
- report parsers;
- design rules;
- verification gates;
- retry policies;
- artifact storage.

The harness is what turns an LLM from "a model that writes text" into "an engineering worker that operates inside a controlled chip design workflow".

### 2.2 Hermes-Style Learning

Hermes Agent is interesting because it emphasizes:

- persistent memory;
- learning from experience;
- generating skills from repeated tasks;
- improving skills during use;
- remembering user preferences and past work.

For chip design, this maps naturally to EDA failure patterns:

- Verilator syntax errors;
- inferred latch warnings;
- multiple-driver issues;
- reset bugs;
- mismatched valid/ready protocols;
- unsupported SystemVerilog constructs in Yosys;
- OpenROAD timing failures;
- routing congestion;
- DRC/LVS issues.

The platform can convert repeated failures into reusable skills.

### 2.3 Loop Engineering

Loop Engineering is the move from one-shot prompting to designing autonomous feedback loops.

For chip design, the core loop is:

```text
generate
  -> run tool
  -> parse result
  -> diagnose
  -> patch
  -> rerun
```

This is especially suitable for EDA because EDA tools already provide objective feedback:

- compiler errors;
- lint warnings;
- simulation mismatches;
- assertion failures;
- synthesis reports;
- timing violations;
- routing failures;
- DRC/LVS reports.

### 2.4 Goal-Driven Agent Workflows

Claude-style `/goal` workflows are useful because they define a completion condition.

For chip design, useful goals are naturally verifiable:

```text
/goal Verilator lint is clean and all cocotb tests pass

/goal The generated FIFO RTL passes simulation and synthesizes with Yosys

/goal OpenLane completes and produces final.gds with no setup timing violations

/goal Analyze the timing report and propose the smallest RTL or constraint change
```

The key idea is that the agent should not stop because it has produced text. It should stop because the engineering condition is satisfied.

## 3. Product Thesis

The product thesis is:

```text
Chip Design Agent = Model + Harness + Loops + Goals + Skills + EDA Tools
```

The model alone is not enough.

The platform becomes powerful when:

1. the harness controls the environment;
2. loops keep running until objective checks pass;
3. goals define when work is done;
4. skill memory captures repeated EDA fixes;
5. open-source EDA tools provide objective feedback.

## 4. Possible Product Forms

### 4.1 OpenChipAgent Goal Runner

A goal-driven chip design runner.

Example:

```text
/goal Generate an async FIFO. Verilator lint must be clean, cocotb tests must pass, and Yosys synthesis must succeed.
```

Workflow:

```text
structured spec
  -> RTL generation
  -> testbench generation
  -> Verilator lint
  -> cocotb simulation
  -> debug loop
  -> Yosys synthesis
  -> final report
```

This is the most realistic first product.

### 4.2 RTL Repair Loop Agent

A focused product for RTL debugging.

Inputs:

- failing RTL;
- testbench;
- compiler log;
- simulation log;
- waveform summary.

Loop:

```text
parse failure
  -> identify likely bug
  -> patch RTL or testbench
  -> rerun
  -> stop only when tests pass
```

This product can be useful even before full RTL-to-GDS integration.

### 4.3 OpenROAD / OpenLane Flow Copilot

A backend-flow copilot for open-source physical design.

Goal examples:

```text
/goal Run OpenLane to final GDS and summarize all failing stages.

/goal Fix the current OpenROAD flow until placement and routing complete.

/goal Explain the top 10 timing violations and propose repair strategies.
```

Core capability:

- detect which stage failed;
- parse logs;
- explain the root cause;
- modify config or constraints;
- rerun the flow;
- preserve all artifacts.

### 4.4 Chip Harness Studio

A platform for building reliable chip design agent environments.

Responsibilities:

- create a standard project structure;
- pin tool versions;
- manage Docker images;
- manage PDK profiles;
- define run manifests;
- expose log parsers;
- define permission policies;
- store artifacts;
- enforce review gates.

This is the infrastructure layer that makes higher-level agents reliable.

### 4.5 Self-Learning EDA Agent

A Hermes-inspired agent that learns from repeated chip design failures.

Examples:

```text
Failure: "Latch inferred"
Skill learned: ensure combinational always blocks assign every output in every branch.

Failure: "Multiple drivers"
Skill learned: search all always blocks and continuous assignments for the same net.

Failure: "Unsupported SystemVerilog syntax in Yosys"
Skill learned: rewrite construct into conservative Verilog subset.

Failure: "OpenROAD setup violation"
Skill learned: classify whether the likely fix is constraint, buffering, retiming, or RTL pipeline change.
```

The long-term moat is the accumulation of chip-design-specific repair skills.

## 5. Recommended Product Architecture

```text
OpenChipAgentPlatform
├── Goal Runner
│   └── long-running objectives with verifiable completion conditions
├── Harness Manager
│   └── tools, PDKs, directories, permissions, logs, artifacts
├── Loop Engine
│   └── generate -> run -> parse -> diagnose -> patch -> rerun
├── Skill Memory
│   └── EDA repair patterns learned from prior runs
├── Tool Adapters
│   └── Verilator / Icarus / cocotb / Yosys / OpenROAD / OpenLane
├── Report Intelligence
│   └── simulation, synthesis, timing, area, power, routing reports
└── Human Review Layer
    └── approvals, diffs, rollback, stage gates
```

## 6. Why This Is Stronger Than a Normal Chip Chatbot

A normal chip chatbot can answer questions and generate code.

OpenChipAgentPlatform should do more:

```text
write RTL
  -> run objective tools
  -> detect failure
  -> repair
  -> rerun
  -> save evidence
  -> summarize
  -> learn from the run
```

Comparison:

| Capability | Chatbot | Goal-Driven Chip Agent Harness |
|---|---|---|
| Answers questions | Yes | Yes |
| Generates RTL | Maybe | Yes |
| Runs tools | Usually no | Yes |
| Parses EDA logs | Weak | Core feature |
| Repairs from feedback | Weak | Core loop |
| Verifiable stop condition | No | Yes |
| Saves artifacts | No | Yes |
| Learns reusable EDA skills | No | Planned |
| Supports RTL-to-GDS flow | No | Planned |

## 7. Recommended First Product

The first product should be:

```text
OpenChipAgent Goal Runner
```

First supported goal:

```text
/goal Given a natural language spec, generate a synthesizable RTL module.
      Verilator lint must be clean.
      cocotb tests must pass.
      Yosys synthesis must pass.
      Produce a final report with artifacts.
```

This first goal is narrow enough to build, but valuable enough to prove the platform.

## 8. Later Product Expansion

After the verified RTL loop is stable:

1. Add OpenROAD/OpenLane physical design goals.
2. Add timing report diagnosis.
3. Add PPA optimization loops.
4. Add benchmark mode with RTLLM / VerilogEval / TuRTLe.
5. Add skill memory for repeated EDA errors.
6. Add web UI for workflow visualization.
7. Add VSCode extension for engineer-in-the-loop workflows.

## 9. Key Design Principle

The platform should be designed around evidence.

Every meaningful agent action should produce:

- a file;
- a command;
- a log;
- a diff;
- a report;
- or a measurable pass/fail result.

The system should not ask users to trust the agent's confidence. It should show the engineering evidence.

