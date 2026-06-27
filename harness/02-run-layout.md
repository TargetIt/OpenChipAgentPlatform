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

1. spec completeness check;
2. Verilator lint;
3. cocotb simulation;
4. Yosys synthesis;
5. final report check.

After any RTL patch caused by synthesis, rerun lint and simulation before declaring synthesis fixed.

## Reproducibility Rule

A final report is not enough. A run is complete only when another engineer can use `metadata/run.json` plus the files in the run directory to reproduce the same pass, fail, or blocker.
