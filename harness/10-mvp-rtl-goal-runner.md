# MVP: RTL Goal Runner

The first MVP is the RTL Goal Runner.

## Purpose

Given a small digital design goal, the harness guides a general-purpose agent through:

```text
spec -> RTL -> testbench -> lint -> simulation -> synthesis -> report
```

## Supported Design Scope

Initial scope:

- small synchronous digital modules;
- conservative Verilog/SystemVerilog;
- single clock;
- clear reset behavior;
- simple handshakes;
- no complex SoC integration.

Initial examples:

- counter;
- FIFO;
- UART transmitter;
- UART receiver;
- SPI master;
- AXI-lite register block;
- arbiter;
- edge detector;
- toy matrix multiply accelerator.

## Completion Checks

A run is successful when:

- structured spec exists;
- RTL exists;
- testbench exists;
- Verilator lint passes;
- simulation passes;
- Yosys synthesis passes;
- final report exists.

## Success Metric

First milestone:

```text
10 small IP tasks
>= 7 complete automatically
all runs reproducible
all patches recorded
all failures classified
```

## Out of Scope

- full SoC generation;
- UVM;
- CDC/RDC;
- DFT;
- analog/mixed-signal;
- production signoff;
- full timing closure.

