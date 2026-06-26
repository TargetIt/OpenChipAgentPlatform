# RTL Goal Runner Workflow

## Inputs

- user goal;
- optional existing RTL;
- optional testbench;
- target toolchain.

## Steps

1. Create structured spec.
2. Identify missing requirements.
3. Generate RTL.
4. Generate testbench.
5. Run lint.
6. Run simulation.
7. Classify failures.
8. Patch and rerun.
9. Run synthesis.
10. Write final report.

## Done Condition

- lint passes;
- simulation passes;
- synthesis passes;
- artifacts are saved;
- report is written.

## Failure Policy

If a failure repeats for the same reason after the retry budget, stop and report:

- failure class;
- evidence;
- attempted repairs;
- recommended human action.

