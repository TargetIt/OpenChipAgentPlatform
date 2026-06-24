# Proposed System Architecture

## 1. High-Level Architecture

```text
Frontend
  - Web UI
  - CLI
  - VSCode extension

Agent Orchestrator
  - workflow graph
  - state machine
  - retry policy
  - artifact manager
  - context manager
  - tool permission layer

Specialized Agents
  - SpecAgent
  - RTLAgent
  - TestbenchAgent
  - VerificationAgent
  - DebugAgent
  - SynthesisAgent
  - PhysicalDesignAgent
  - ReportAgent

Tool Runners
  - Verilator
  - Icarus Verilog
  - cocotb
  - Yosys
  - OpenROAD
  - OpenLane
  - Magic
  - KLayout
  - Netgen

Artifact Store
  - spec.md
  - design.sv / design.v
  - testbench files
  - simulation logs
  - waveform files
  - synthesis reports
  - timing reports
  - DEF/GDS files
  - run manifest
  - final review report
```

## 2. Agent Responsibilities

### SpecAgent

Turns a natural language request into a structured design specification.

Outputs:

- module name;
- ports;
- clock/reset behavior;
- latency requirements;
- valid/ready protocol if needed;
- expected behavior;
- corner cases;
- acceptance tests.

### RTLAgent

Generates or edits RTL according to the structured spec.

Outputs:

- Verilog/SystemVerilog source;
- design notes;
- known assumptions.

### TestbenchAgent

Generates tests from the spec.

Outputs:

- directed tests;
- randomized tests if appropriate;
- cocotb or Verilog testbench;
- expected reference model.

### VerificationAgent

Runs syntax, lint, and simulation checks.

Tools:

- Verilator;
- Icarus Verilog;
- cocotb;
- optional formal tools later.

Outputs:

- pass/fail result;
- parsed errors;
- failing waveform references;
- failure summary.

### DebugAgent

Uses tool output to repair RTL or tests.

Inputs:

- failing spec item;
- compiler error;
- simulation mismatch;
- waveform summary;
- previous patch history.

Outputs:

- patch proposal;
- explanation;
- rerun request.

### SynthesisAgent

Runs Yosys and parses reports.

Outputs:

- synthesis pass/fail;
- cell count;
- area estimate;
- critical warnings;
- unsupported constructs;
- netlist artifact.

### PhysicalDesignAgent

Runs OpenROAD/OpenLane after RTL and synthesis are stable.

Outputs:

- floorplan status;
- placement/routing status;
- timing summary;
- congestion summary;
- final DEF/GDS if successful.

### ReportAgent

Summarizes the entire run.

Outputs:

- final status;
- what passed;
- what failed;
- generated artifacts;
- design risks;
- next recommended actions.

## 3. Workflow State Machine

```text
NEW_REQUEST
  -> SPEC_DRAFTED
  -> RTL_GENERATED
  -> TESTBENCH_GENERATED
  -> SIMULATION_RUNNING
  -> SIMULATION_FAILED -> DEBUG_PATCHED -> SIMULATION_RUNNING
  -> SIMULATION_PASSED
  -> SYNTHESIS_RUNNING
  -> SYNTHESIS_FAILED -> DEBUG_PATCHED -> SIMULATION_RUNNING
  -> SYNTHESIS_PASSED
  -> PHYSICAL_FLOW_RUNNING
  -> PHYSICAL_FLOW_FAILED -> REPORT_ONLY or DEBUG_PATCHED
  -> PHYSICAL_FLOW_PASSED
  -> FINAL_REPORT
```

## 4. Artifact Model

Each run should create a directory like:

```text
runs/2026-06-24-001/
  manifest.json
  spec/
    original_prompt.md
    structured_spec.md
  rtl/
    design.sv
    patches/
  tb/
    tb.py
    reference_model.py
  sim/
    verilator.log
    cocotb.log
    wave.fst
  synth/
    yosys.ys
    yosys.log
    netlist.v
    area.rpt
  pnr/
    openroad.log
    timing.rpt
    final.def
    final.gds
  report/
    final_report.md
```

## 5. Integration Strategy

The platform should integrate existing tools through stable command wrappers instead of directly coupling to internal APIs at the beginning.

Recommended first wrapper interface:

```json
{
  "tool": "verilator",
  "command": ["verilator", "--lint-only", "design.sv"],
  "cwd": "runs/2026-06-24-001",
  "inputs": ["rtl/design.sv"],
  "outputs": ["sim/verilator.log"],
  "status": "pass|fail",
  "parsed_errors": []
}
```

This creates a clean boundary between agents and tools.

## 6. Design Principle

Agents should not be trusted because they sound confident. They should be trusted only when:

- generated files are saved;
- commands are reproducible;
- tests pass;
- reports are parsed;
- failures are visible;
- every repair has a diff.

