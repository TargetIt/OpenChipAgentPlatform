# Final Report

## Status

Passed.

The `openPwmChipFlow` project was driven through the complete RTL-to-GDS flow on a Linux/container backend. Phase 3 through Phase 6 were not skipped.

## What This Proves

The Harness/Loop approach must model chip work as an evidence-producing system, not as a code-generation session. The useful product behavior is:

```text
goal
  -> project probe
  -> capability gate
  -> local frontend checks
  -> backend execution target
  -> synthesis/PnR/signoff/GDS
  -> evidence consistency check
  -> final report
```

## Product Lessons

1. Local macOS is useful for fast front-end checks, but full backend closure needs Linux/container infrastructure.
2. `needs_backend_execution_target` must be a first-class status.
3. Design configs should not hard-code PDK/tool install paths.
4. PDK version consistency must be checked across OpenLane config, `.magicrc`, logs, and final artifacts.
5. Final reports must cite raw tool evidence: DRC, LVS, antenna, GDS readability, and generated artifact list.
6. Artifact upload and run IDs should be captured because they make a run reviewable by another engineer.

## Remaining Product Work

- Turn these documented rules into an executable Harness runner.
- Add schema-level validation examples for backend artifacts.
- Add automatic stale-artifact detection based on run id and timestamps.
- Add a backend target selector for local, container, remote CI, and cluster execution.
