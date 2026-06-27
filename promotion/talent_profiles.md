# OpenChipAgentPlatform 启动阶段人才画像

版本：2026-06-27

## 总体判断

当前阶段最需要的人不是单纯大模型研究员，而是能把大模型变成可靠工程系统的 Agent 工程人才。

原因：

- 我们短期不需要从零训练基础模型。
- 现有大模型已经具备足够的代码、文档和工具调用基础能力。
- 真正的难点在芯片验证场景：工具链复杂、失败多样、质量要求高、证据链必须完整。
- 产品成败取决于能否让 Agent 在真实 EDA 环境里闭环，而不是生成一次漂亮回答。

## 1. 第一优先级：Agent/Harness 工程负责人

### 使命

把通用大模型和通用代码 Agent 改造成芯片验证 Agent。

### 核心能力

- 熟悉 LLM Agent 的任务规划、工具调用、记忆、反思、重试和状态管理。
- 能设计长任务执行框架：goal -> plan -> execute -> observe -> repair -> verify -> report。
- 能设计 schema、workflow、artifact tracking、failure taxonomy。
- 能做工程落地：CLI、日志采集、队列、权限、隔离、审计、恢复。
- 能处理多工具输出：编译器日志、测试日志、结构化报告、文件 diff。
- 有强代码能力，能把原型做成稳定可维护系统。

### 加分项

- 做过 Claude Code / OpenCode / Codex / Cursor / Aider 相关插件或工作流。
- 做过自动化测试平台、CI/CD、DevOps、observability。
- 做过复杂工具链编排，例如编译器、仿真器、数据平台、云原生任务系统。
- 理解 RAG、向量检索、上下文压缩、长上下文管理。

### 面试重点

- 让候选人设计一个“自动修复失败测试”的 Agent。
- 追问如何防止 Agent 为了通过测试而删除测试。
- 追问如何记录每一步证据，如何让另一个 Agent 接管。
- 追问失败三次后如何判断是 blocker、spec ambiguity 还是 tool config error。

## 2. 第二优先级：芯片验证专家

### 使命

把真实验证流程、质量标准和工程边界固化进 Harness。

### 核心能力

- 熟悉 SystemVerilog/UVM/cocotb 中至少一种验证体系。
- 熟悉 directed/random testing、scoreboard、monitor、driver、reference model。
- 熟悉 coverage closure、assertion、regression、debug。
- 能读懂 RTL、仿真 log、波形、失败栈。
- 能定义什么场景可以自动修，什么场景必须人工 review。
- 能把验证经验转成可执行的 workflow 和 skill。

### 加分项

- 做过复杂 IP 或 SoC 子系统验证。
- 做过 RISC-V、CPU、NPU、接口 IP、总线协议验证。
- 熟悉商业仿真器和回归平台。
- 有验证平台建设经验。

### 面试重点

- 让候选人描述一次复杂 bug debug 过程。
- 追问如何把这个过程变成 Agent 可执行流程。
- 追问 coverage hole 如何定位根因。
- 追问 AI 生成 testbench 最危险的失败模式是什么。

## 3. 第三优先级：EDA 工具链/平台工程师

### 使命

把 Agent 接入真实 EDA 环境。

### 核心能力

- 熟悉 Verilator、Yosys、cocotb、Make、脚本化工具链。
- 能接入商业 EDA CLI、license 环境、regression 系统。
- 能做日志解析、报告解析、产物管理。
- 能建设可复现 run 环境。

### 加分项

- 熟悉 VCS/Xcelium/Questa、Verdi、Jasper/Formal、SpyGlass 等。
- 做过企业内部 EDA 平台或验证自动化平台。
- 熟悉容器化、调度、远程执行、资源隔离。

## 4. 第四优先级：大模型/算法人才

### 使命

在产品闭环成立后，提升模型在 EDA/验证语义上的专用能力。

### 早期需要的能力

- 模型选择和评测。
- prompt/program synthesis 评测。
- RAG、embedding、rerank、上下文压缩。
- 基于 run 数据构建训练/评测集。

### 中后期需要的能力

- EDA/RTL/verification 专用模型微调。
- 私有部署和推理成本优化。
- 多模型路由。
- 基于失败数据的自学习。

### 为什么可以晚一点

在没有真实 run 数据、真实客户反馈、真实 failure taxonomy 之前，训练模型容易变成无目标优化。先让 Harness 跑起来，才能知道模型到底应该学什么。

## 5. 早期最理想的小团队组合

建议 4-6 人起步：

| 角色 | 人数 | 作用 |
| --- | --- | --- |
| Agent/Harness 工程负责人 | 1 | 架构和闭环核心 |
| Agent 工程师 | 1-2 | 工具调用、run 管理、debug loop |
| 验证专家 | 1-2 | 验证流程、质量标准、案例构建 |
| EDA 平台工程师 | 1 | 工具链接入、日志和环境 |
| 大模型工程师 | 0-1 | 早期兼职即可，后续增强 |

## 6. 早期招聘原则

- 优先找能做出东西的人，而不是只会讲模型概念的人。
- 优先找能接受硬件工程严谨性的人。
- 优先找愿意和验证工程师一起抠细节的人。
- 优先找能把失败记录下来并转成系统能力的人。
- 不要找只追求 demo 炫技、不能接受质量约束的人。
