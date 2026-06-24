# Landscape Survey: Open-Source Agents and Tools for Chip Design

This document summarizes the initial research around tools similar to ChipAgent / ChipAgents and the broader open-source chip design ecosystem.

## 1. Similar Agent / LLM Projects

These projects are closest to the "AI agent for chip design" direction.

| Project | Type | What It Does | Notes |
|---|---|---|---|
| [ChatEDA](https://github.com/wuhy68/ChatEDA) | LLM-powered EDA agent | Uses an LLM controller to decompose EDA tasks, generate scripts, and execute EDA flows from RTL toward GDS | Research-oriented, but very close to the agent orchestration idea |
| [AutoChip](https://github.com/shailja-thakur/AutoChip) | LLM Verilog generation and repair | Generates Verilog from a prompt and testbench, then feeds compilation/simulation errors back into the LLM for repair | Good reference for RTL debug loops |
| [digital-chip-design-agents](https://github.com/chuanseng-ng/digital-chip-design-agents) | Full-stack HDL design agents / skills | Provides agent skills for RTL flow, timing analysis, UVM generation, and related chip design tasks | Very relevant as an engineering-oriented agent integration reference |
| [RTL-Coder](https://github.com/hkust-zhiyao/RTL-Coder) | RTL generation model | Open LLM solution for RTL code generation | More model-focused than workflow-focused |
| [HaVen](https://github.com/Intelligent-Computing-Research-Group/HaVen) | Verilog generation evaluation / model research | Targets hallucination-mitigated Verilog generation and benchmark evaluation | Useful for model-side research |

## 2. Benchmarks and Evaluation Suites

These are important because an agent that "looks correct" but fails functionally is not useful for hardware design.

| Project | Purpose | Why It Matters |
|---|---|---|
| [RTLLM](https://github.com/hkust-zhiyao/RTLLM) | Natural-language-to-RTL benchmark | Provides design descriptions and testbenches for evaluating RTL generation |
| [VerilogEval](https://github.com/NVlabs/verilog-eval) | Verilog generation evaluation harness | Useful for measuring syntax and functional correctness of generated Verilog |
| [TuRTLe](https://github.com/HPAI-BSC/TuRTLe) | Unified RTL LLM evaluation framework | Integrates multiple benchmarks and evaluates syntax, function, synthesis, PPA, and line completion |
| [LLM4IC](https://github.com/DfX-NYUAD/LLM4IC) | Resource list | Tracks LLMs and future chip design resources |
| [Awesome-LLM4EDA](https://github.com/Thinklab-SJTU/Awesome-LLM4EDA) | Resource list | Tracks LLM-for-EDA papers and projects |
| [awesome-ai4eda](https://github.com/Thinklab-SJTU/awesome-ai4eda) | Resource list | Broader AI-for-EDA resource list |

## 3. Open-Source Digital EDA Tools

These tools form the practical backbone of an open chip design workflow.

| Stage | Tools | Role |
|---|---|---|
| RTL lint / simulation | [Verilator](https://github.com/verilator/verilator), Icarus Verilog | Compile, lint, simulate RTL |
| Python verification | [cocotb](https://www.cocotb.org/), [cocotb GitHub](https://github.com/cocotb/cocotb) | Write Verilog/VHDL testbenches in Python |
| RTL synthesis | [Yosys](https://github.com/YosysHQ/yosys) | Synthesize RTL into gate-level netlists |
| SystemVerilog frontend | [Synlig](https://github.com/chipsalliance/synlig), Surelog/UHDM | Improve SystemVerilog parsing and elaboration support |
| RTL-to-GDS application | [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) | Placement, routing, timing, physical design implementation |
| RTL-to-GDS flow | [OpenROAD-flow-scripts](https://github.com/The-OpenROAD-Project/OpenROAD-flow-scripts) | Scripted autonomous RTL-to-GDS flow |
| Integrated flow | [OpenLane](https://github.com/The-OpenROAD-Project/OpenLane) | Automated RTL-to-GDS flow using Yosys, OpenROAD, Magic, Netgen, and related tools |
| Layout / DRC / LVS | [Magic](https://github.com/RTimothyEdwards/magic), [KLayout](https://www.klayout.de/), Netgen | Layout editing/viewing, DRC, LVS, GDS inspection |
| Tool distribution | [OSS CAD Suite](https://github.com/YosysHQ/oss-cad-suite-build) | Bundled distribution of open-source digital design tools |

## 4. Analog / Mixed-Signal and Generator Projects

| Project | Role |
|---|---|
| [OpenFASoC](https://github.com/idea-fasoc/OpenFASOC) | Automated analog / mixed-signal generator flow from user specification to GDSII |
| [OpenFASoC tapeouts](https://github.com/idea-fasoc/openfasoc-tapeouts) | Examples of generated circuits and tapeouts |

OpenFASoC is relevant because it shows a generator-driven approach to chip design. It may be a later-stage integration target after the digital RTL flow is stable.

## 5. Open PDKs and Tapeout Harnesses

| Project | Role |
|---|---|
| [SkyWater SKY130 PDK](https://github.com/google/skywater-pdk) | Open-source 130nm process design kit |
| [IHP Open PDK](https://github.com/IHP-GmbH/IHP-Open-PDK) | Open-source 130nm BiCMOS PDK |
| [open_pdks](https://github.com/RTimothyEdwards/open_pdks) | PDK installer and setup project for open-source EDA tools |
| [Caravel](https://github.com/efabless/caravel) | Efabless/SKY130 SoC harness for user projects |

PDKs are not optional. Without a PDK, there is no meaningful path from RTL or layout to manufacturable GDS.

## 6. Important Takeaways

1. The agent layer is still immature.
   - Existing open-source agent projects are promising but not yet production-grade end-to-end chip designers.

2. The EDA tool layer is real and usable.
   - Verilator, Yosys, OpenROAD, OpenLane, Magic, KLayout, and open PDKs already form a practical ecosystem.

3. The missing piece is orchestration.
   - Users need one platform that can coordinate agents, run tools, parse logs, repair files, preserve artifacts, and explain results.

4. Verification must be central.
   - RTL generation without testbenches, simulation, lint, and synthesis checks is not trustworthy.

5. The first useful product should be conservative.
   - Start with small modules and deterministic flows.
   - Do not promise full autonomous commercial SoC design at the beginning.

