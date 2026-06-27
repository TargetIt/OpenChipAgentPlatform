# OpenChipAgent Loop

这个目录记录 OpenChipAgentPlatform 的 Loop 设计。

Loop 的目的不是让 AI 一上来自动设计完整芯片，而是把 AI Agent 放进真实芯片工程流程里，让它围绕目标持续执行、调用工具、读取证据、修复问题、回归验证，并把经验沉淀下来。

## 一句话定义

```text
Loop 是 Harness 驱动的 AI 芯片工程任务执行机制。
```

换句话说：

```text
Harness 管规则。
Loop 管执行。
EDA 工具提供证据。
Human Review 控制风险。
Skill Memory 沉淀经验。
```

## 当前定位

短期目标：

```text
AI + Harness + EDA 工具 = 可控、可复现、可审计的芯片验证 Agent
```

长期目标：

```text
验证 Agent
  -> RTL 辅助设计 Agent
  -> IP 级设计验证 Agent
  -> 子系统级芯片工程 Agent
  -> 更完整的 AI-native EDA 平台
```

## 文档结构

- `loop-purpose.md`: Loop 的目的、边界和与 Harness 的关系。
- `execution-loop.md`: 从用户目标到报告输出的完整执行闭环。
- `mvp-loop.md`: 第一阶段 MVP 应该怎么落地。
- `first-principles.md`: 从第一性原理推导 Loop 应该具备什么。
- `agent-loop-patterns.md`: ReAct、Reflexion、SWE-agent、OpenHands、EDA agentic AI 的可借鉴模式。
- `openPwmChipFlow-case-study.md`: 使用 `TargetIt/openPwmChipFlow` 对 Loop 做的一次演练和缺陷回收。

## 核心原则

1. 先定义目标，再执行任务。
2. 先生成验证意图，再生成验证代码。
3. 所有结论必须有工具证据。
4. Agent 不能自己修改验收标准。
5. 失败必须分类。
6. 修复必须回归。
7. 风险动作必须进入 human review。
8. 每次 run 都要沉淀经验。

## 当前修正后的最小控制环

```text
Sense
  读取目标、仓库、工具能力、现有产物、历史日志

Model
  建立当前任务状态、设计意图、验证意图、约束和风险模型

Plan
  选择下一步最小可验证动作

Act
  调用工具、生成资产、修改文件或请求人工判断

Observe
  读取 exit code、日志、报告、波形、覆盖率、文件 diff

Judge
  判定通过、失败、跳过、阻塞、需人工 review，并检查证据一致性

Learn
  把 failure、repair、环境约束、项目知识沉淀到 run record / skill memory
```

线性的 `Goal -> Plan -> Asset -> Execute -> Report` 只是外层叙事。真正工程实现应当是上述状态机反复运行。
