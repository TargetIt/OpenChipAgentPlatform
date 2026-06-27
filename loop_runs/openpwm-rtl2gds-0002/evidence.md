# Evidence

## Repository

```text
repo: TargetIt/openPwmChipFlow
branch: main
successful commit: 2e6f479 Remove hard-coded OpenLane PDK path
workflow: RTL to GDS
run id: 28294071129
job id: 83830873514
artifact: openpwm-rtl2gds-28294071129
artifact id: 7925921115
artifact size: 18,731,201 bytes
uploaded files: 454
```

## Execution Target

```text
frontend target: local macOS arm64
backend target: GitHub Actions ubuntu-24.04 + efabless/openlane:latest container
PDK: sky130A
PDK version: 0fe599b2afb6708d281543108caf8310912f54af
```

## Successful Stages

| Stage | Status | Evidence |
| --- | --- | --- |
| Simulation | passed | RTL simulation step passed in run `28294071129` |
| Synthesis | passed | Phase 3 synthesis report generated from `RUN_2026.06.27_15.52.49` |
| PnR | passed | Phase 4 PnR report generated from `RUN_2026.06.27_15.52.49` |
| Magic DRC | passed | 0 violations |
| KLayout DRC | passed | 0 violations |
| LVS | passed | no mismatches |
| Antenna | passed | 0 violations |
| GDS | passed | `pwm_ctrl.gds` produced and readable by KLayout Python |

## Delivered Backend Artifacts

```text
pwm_ctrl.gds    416K
pwm_ctrl.lef    8.0K
pwm_ctrl.lib    12K
pwm_ctrl.def    88K
gate netlist    24K
pwm_ctrl.spice  20K
SDF files       10
SPEF corners    3
```

## Failure Repaired During The Run

The previous backend run failed at Magic GDS stream-out:

```text
Could not find file .../c6d73.../sky130A/libs.tech/magic/sky130A.tech
error copying .../pwm_ctrl.magic.gds: no such file or directory
```

Root cause:

```text
openlane/pwm_ctrl/config.tcl hard-coded an old PDK_ROOT.
```

Repair:

- remove hard-coded `PDK_ROOT` from OpenLane Tcl configs;
- pass `PDK_ROOT` from CI/container environment;
- add CI checks for the expected Magic tech file;
- add CI guard against the stale PDK hash in active OpenLane configs.
