# MVP Loop

第一阶段不要做完整芯片设计，也不要一开始做完整 UVM / SoC 验证。MVP 的目标是证明：

```text
AI Agent 能在 Harness 约束下，完成一个小模块的验证闭环。
```

## MVP 输入

支持输入：

- 一个小 RTL 模块；
- 一段自然语言设计说明；
- 一个简单 bug 描述；
- 一个已有失败 log。

第一批模块建议：

- FIFO；
- arbiter；
- counter；
- ready/valid pipeline；
- simple bus register block；
- edge detector。

## MVP 工具链

优先使用开源工具，降低集成成本：

- Verilator：lint / 编译检查；
- cocotb：Python 测试；
- Python reference model：行为参考；
- Yosys：基础 synthesizable check；
- Makefile / shell scripts：执行入口。

## MVP 执行链路

```text
输入项目 / RTL / spec
  -> project probe
  -> 生成结构化 spec
  -> 生成验证计划
  -> 生成 cocotb testbench
  -> 生成 reference model
  -> capability gate
  -> 运行 Verilator
  -> 运行 simulation
  -> 读取 log
  -> evidence consistency check
  -> 分类失败
  -> 修 testbench 或建议 RTL 修复
  -> 回归
  -> 生成 report
```

## MVP 不做什么

第一阶段不要急着做：

- 完整 UVM 自动生成；
- SoC 级验证；
- 商业 EDA 深度集成；
- coverage closure 全自动；
- 自研大模型；
- 完整后端流程；
- 自动 tape-out。

这些不是不重要，而是应该等小闭环跑通后再扩展。

## MVP 成功标准

一个 MVP run 成功，至少需要：

- 有 `goal.json`；
- 有 `spec.md`；
- 有 project probe 结果；
- 有工具能力检查；
- 有生成的 testbench；
- 有真实工具命令记录；
- 有 log；
- 没有证据冲突；
- 有失败分类；
- 有修复记录；
- 有回归记录；
- 有最终报告。

建议第一阶段目标：

```text
10 个小模块验证任务
  >= 7 个能自动跑完整闭环
  所有失败都有分类
  所有结果都可复现
```

## 产品模块映射

```text
Goal Manager
  -> 接收目标，生成 goal.json

Spec Extractor
  -> 生成 spec.md

Verification Planner
  -> 生成测试计划和出口标准

Asset Generator
  -> 生成 testbench / reference model / scripts

Tool Runner
  -> 运行 Verilator / cocotb / Yosys

Evidence Analyzer
  -> 读取 log / error / mismatch

Failure Classifier
  -> 分类 RTL bug / testbench bug / spec ambiguity / tool config error

Repair Planner
  -> 生成最小修复建议

Human Review Gate
  -> 控制高风险动作

Regression Manager
  -> 重新运行受影响检查

Report Generator
  -> 输出最终报告

Skill Memory
  -> 沉淀 failure 和 repair
```

## MVP 最关键的风险

1. Agent 生成了测试，但测试本身不可靠。
2. Agent 为了通过测试而弱化测试。
3. Agent 无法定位 log 根因。
4. Agent 修了一个 case，破坏其他 case。
5. Agent 没有保留足够证据，工程师无法信任结果。
6. Agent 把 skipped 阶段当成 passed。
7. Agent 把旧报告当成本次 run 结果。
8. Agent 没有发现需求和设计规格冲突。

MVP 必须围绕这些风险设计，而不是只追求 demo 看起来很顺。

## 从 openPwmChipFlow 得到的 MVP 修正

`openPwmChipFlow` 说明，MVP 即使只做小 PWM，也必须处理：

- 环境工具缺失；
- 阶段跳过；
- 报告内部矛盾；
- 需求与规格冲突；
- 端到端 flow 的阶段状态传播。

所以 MVP 的最低要求不是“跑一个 testbench”，而是：

```text
能可靠地区分 passed / failed / skipped / blocked / needs_review。
```

## 第一版产品口号

```text
不是让 AI 随便写验证代码，
而是让 AI 在 Harness 和 EDA 证据约束下完成验证闭环。
```
