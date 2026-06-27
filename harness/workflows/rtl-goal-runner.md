# RTL Goal Runner Workflow

## Inputs

- user goal;
- optional existing RTL;
- optional testbench;
- target toolchain.

## Steps

1. Create `goal.json` and the canonical run directory from `harness/02-run-layout.md`.
2. Create `spec/spec.md` from `templates/spec-template.md`.
3. Identify missing requirements. If a required interface, reset, clock, latency, or acceptance-test rule is missing, stop for clarification.
4. Generate RTL under `rtl/`.
5. Generate testbench and reference model under `tb/`.
6. Run Verilator lint and save raw logs under `logs/`.
7. Run cocotb or equivalent simulation and save raw logs, seed, and waveform path when available.
8. Classify failures using `schemas/failure.schema.json`.
9. Patch the smallest safe scope and record the repair action.
10. Rerun every check invalidated by the patch.
11. Run Yosys synthesis only after lint and simulation pass.
12. Write `metadata/run.json` and `reports/final.md`.

## Required Command Templates

The exact project command may vary, but each run should start from these templates unless the repository already has a better script.

```bash
verilator --lint-only -Wall rtl/<module>.sv
make -C tb MODULE=<module> TOPLEVEL=<module>
yosys -q -s scripts/synth.ys
```

If a command is changed, record the reason in `metadata/run.json`.

## Done Condition

- `goal.json` exists and validates against `schemas/goal.schema.json`;
- `spec/spec.md` has no `TODO` fields;
- RTL exists under `rtl/`;
- testbench exists under `tb/`;
- Verilator lint passes;
- simulation passes with recorded seed and coverage limitations;
- Yosys synthesis passes;
- required artifacts are saved;
- `metadata/run.json` records commands, checks, artifacts, failures, and repair attempts;
- `reports/final.md` summarizes status, evidence, fixes, and remaining risks.

## Failure Policy

If a failure repeats for the same reason after the retry budget, stop and report:

- failure class;
- evidence;
- attempted repairs;
- recommended human action.

Do not weaken the spec, tests, or tool checks to get a pass. Use `harness/03-human-review-gates.md` when a repair would change the design intent.
