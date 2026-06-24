# Risks and Open Questions

## 1. Technical Risks

### RTL Correctness

LLMs can produce RTL that compiles but is functionally wrong. This is the most important risk.

Mitigation:

- generate tests from structured specs;
- use reference models;
- run simulation;
- run regressions;
- add formal checks later.

### Testbench Weakness

If the same LLM writes both RTL and testbench, both can share the same misunderstanding.

Mitigation:

- separate TestbenchAgent from RTLAgent;
- use independent reference models;
- include randomized tests;
- include benchmark tests from RTLLM and VerilogEval.

### SystemVerilog Support

Open-source SystemVerilog support is improving but still uneven.

Mitigation:

- start with synthesizable Verilog or conservative SystemVerilog;
- use Verilator lint;
- consider Synlig/Surelog/UHDM for more advanced frontend support.

### Toolchain Installation

Open-source EDA tools can be hard to install.

Mitigation:

- provide Docker images;
- pin tool versions;
- record command manifests;
- use OSS CAD Suite where appropriate.

### Physical Design Complexity

OpenROAD/OpenLane failures can come from constraints, floorplan, routing congestion, PDK setup, timing constraints, or RTL structure.

Mitigation:

- add physical design only after simulation/synthesis MVP is stable;
- start with known-good designs;
- parse reports stage by stage.

## 2. Product Risks

### Overpromising

"Natural language to chip" is attractive but dangerous. Users may assume production readiness.

Mitigation:

- position first versions as educational, research, and small-IP automation;
- clearly report confidence and verification coverage;
- avoid claiming full signoff.

### Black-Box Behavior

If users cannot see commands, files, logs, and diffs, they cannot trust the system.

Mitigation:

- save all artifacts;
- show all patches;
- produce final run reports;
- make every command reproducible.

### Agent Sprawl

Integrating many agents can become messy if responsibilities overlap.

Mitigation:

- define agent contracts;
- use workflow state machines;
- keep tool runners deterministic;
- make agents propose changes, not silently mutate everything.

## 3. Open Questions

1. What is the first benchmark suite?
   - RTLLM, VerilogEval, custom tasks, or a curated mix?

2. Which HDL subset should Phase 1 support?
   - Verilog-2005 only?
   - Conservative SystemVerilog?

3. What is the first user interface?
   - CLI, web UI, or VSCode extension?

4. Which model provider should be supported first?
   - OpenAI-compatible API?
   - Local model?
   - Both through a provider abstraction?

5. How should agent memory work?
   - Per-run only?
   - Project-level design memory?
   - Reusable IP memory?

6. How much autonomy is acceptable?
   - Fully automatic retry?
   - User approval before every patch?
   - Policy depends on stage?

7. How should waveform evidence be summarized?
   - Text-only?
   - Automatic signal trace extraction?
   - Browser waveform viewer integration?

8. How should PDKs be managed?
   - Bundled Docker images?
   - User-supplied PDK?
   - Multiple PDK profiles?

## 4. Practical Recommendation

Start small and make the evidence loop excellent.

The platform should first become very good at:

```text
spec -> RTL -> tests -> simulation -> failure explanation -> repair -> pass
```

That loop is the foundation. Without it, later synthesis and physical design automation will be unreliable.

