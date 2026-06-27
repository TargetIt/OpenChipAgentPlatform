# Run Layout

The harness becomes useful only when every agent produces the same shape of evidence. A run directory is the unit of reproducibility.

## Canonical Layout

```text
runs/<goal_id>/<run_id>/
  goal.json
  spec/spec.md
  rtl/
  tb/
  scripts/
  logs/
  artifacts/
    frontend/
    backend/
  metadata/run.json
  reports/final.md
```

## Directory Roles

- `goal.json`: machine-readable goal using `schemas/goal.schema.json`.
- `spec/spec.md`: human-readable structured specification.
- `rtl/`: generated or modified RTL.
- `tb/`: simulation tests, reference models, and Makefiles.
- `scripts/`: tool scripts such as Yosys `.ys` files.
- `logs/`: raw stdout/stderr and tool reports.
- `artifacts/frontend/`: lint, simulation, waveform, coverage, and synthesis-check outputs.
- `artifacts/backend/`: synthesis, PnR, DRC/LVS, GDS, LEF, LIB, DEF, SPICE, SDF, and SPEF outputs.
- `metadata/run.json`: machine-readable run record using `schemas/run.schema.json`.
- `reports/final.md`: concise human final report.

## Command Recording

Each command must record:

- stage;
- tool;
- command line;
- working directory;
- start and end time;
- exit code;
- stdout log path;
- stderr log path;
- whether the command result is required for success.
- execution target, such as local shell, container, remote CI, or cluster.
- key environment inputs, such as PDK version, container image, and license/tool paths.

## Artifact Recording

Each artifact must record:

- path;
- type;
- producing stage;
- producing command id;
- whether it is required;
- optional checksum when available.

## Check Ordering

For the first RTL MVP, use this order:

1. project probe and capability check;
2. spec completeness and consistency check;
3. Verilator lint;
4. cocotb simulation;
5. Yosys synthesis;
6. evidence consistency check;
7. final report check.

After any RTL patch caused by synthesis, rerun lint and simulation before declaring synthesis fixed.

## Stage Status Rule

Every required stage must record one explicit status:

- `passed`;
- `failed`;
- `skipped`;
- `blocked`;
- `needs_tooling`;
- `needs_review`;
- `not_run`.
- `needs_backend_execution_target`.

`skipped`, `blocked`, and `needs_tooling` are not success states. A final report must not claim `passed` if any required stage is skipped or blocked.

`needs_backend_execution_target` is also not a success state. It means the local agent can continue front-end work, but the requested backend flow needs a Linux/container/cluster target with OpenROAD, Magic, Netgen, KLayout, and the selected PDK.

## Evidence Consistency Rule

Before a run can pass, the harness must check:

- command exit code vs. report conclusion;
- per-test results vs. summary result;
- presence of FAIL/ERROR markers in logs;
- skipped stages vs. final status;
- stale artifacts vs. current run id;
- requirement/spec contradictions;
- whether every final claim links to an artifact or log.
- PDK/tool path contamination in design configs;
- PDK version consistency across config, `.magicrc`, logs, and final artifacts.

## Reproducibility Rule

A final report is not enough. A run is complete only when another engineer can use `metadata/run.json` plus the files in the run directory to reproduce the same pass, fail, or blocker.
