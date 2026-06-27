# 优秀 Agent Loop 模式调研

本文件总结可借鉴的公开 Agent loop 模式，并抽象成 OpenChipAgent 可以采用的设计原则。

## 1. ReAct：Reason + Act + Observation

来源：ReAct paper / Google Research。

核心思想：

```text
reason
  -> act
  -> observe
  -> update reasoning
  -> next act
```

可借鉴点：

- 不能让模型只做静态推理，必须让它和环境交互。
- action 的结果会反过来修正 plan。
- 对芯片验证来说，EDA 工具就是环境，log/report/waveform 就是 observation。

落到 OpenChipAgent：

```text
分析当前验证目标
  -> 调用 lint/sim/coverage/PNR 工具
  -> 读取工具反馈
  -> 更新失败分类和下一步动作
```

## 2. Reflexion：Generation + Evaluation + Feedback + Memory

来源：Reflexion paper / OpenReview。

核心思想：

```text
generate
  -> evaluate
  -> verbal feedback
  -> episodic memory
  -> retry with memory
```

可借鉴点：

- 失败后的反思不一定要训练模型，可以沉淀为文本记忆。
- 记忆必须来自反馈，而不是模型自嗨。
- 每次失败都应该形成下一次可用的修复原则。

落到 OpenChipAgent：

```text
失败 log
  -> failure classification
  -> repair summary
  -> skill memory
  -> future run reuse
```

## 3. SWE-agent / Agent-Computer Interface

来源：SWE-agent paper。

核心思想：

Agent 不是普通用户，它需要专门设计过的计算机接口。好的 interface 会显著影响 Agent 能力。

可借鉴点：

- 工具接口不是简单 shell，而是面向 Agent 的可操作环境。
- 文件浏览、编辑、测试、错误定位都需要明确协议。
- interface 设计本身就是产品壁垒。

落到 OpenChipAgent：

```text
EDA-Agent Interface
  -> normalized command schema
  -> normalized log schema
  -> artifact registry
  -> failure taxonomy
  -> safe repair policy
```

## 4. OpenHands Iterative Refinement：Worker + Critic

来源：OpenHands iterative refinement docs。

核心思想：

```text
worker performs task
  -> critic evaluates quality
  -> if below threshold, worker retries with feedback
```

可借鉴点：

- 复杂任务不能只靠单个执行 Agent。
- 需要独立 reviewer / critic 角色检查产物质量。
- reviewer 不是重复执行，而是检查是否满足目标和证据。

落到 OpenChipAgent：

```text
Verification Agent
  -> generates tests / runs tools / repairs

Evidence Critic
  -> checks report consistency, skipped stages, coverage holes, spec conflict

Human Review Gate
  -> handles high-risk decisions
```

## 5. Cadence / Synopsys / ChipAgents 的 EDA Agentic AI 启发

公开资料显示，EDA 厂商和芯片 Agent 公司都强调几个方向：

- 多步骤 workflow；
- 多 Agent 协作；
- 与真实 EDA 工具紧密集成；
- human-in-the-loop；
- 结果必须由仿真、验证、签核等工具约束；
- 覆盖 RTL、验证、debug、testbench、coverage 等任务。

对 OpenChipAgent 的启发：

- 不要做脱离工具的聊天型 Agent。
- 不要只做单点代码生成。
- 应该围绕真实 EDA 反馈建立闭环。
- 质量、安全、证据链比“生成速度”更重要。

## 6. 对 OpenChipAgent Loop 的合成设计

综合以上模式，OpenChipAgent Loop 应该采用：

```text
ReAct 的工具交互
  + Reflexion 的失败记忆
  + SWE-agent 的专用工具接口
  + OpenHands 的 critic/refinement
  + EDA agentic AI 的 signoff-oriented evidence grounding
```

最终形态：

```text
Project Probe
  -> Goal State Machine
  -> Plan/Act/Observe
  -> Evidence Critic
  -> Repair/Review
  -> Regression
  -> Skill Memory
```

## Sources

- ReAct: https://arxiv.org/abs/2210.03629
- Google Research ReAct blog: https://research.google/blog/react-synergizing-reasoning-and-acting-in-language-models/
- Reflexion: https://openreview.net/forum?id=vAElhFcKW6
- SWE-agent: https://arxiv.org/abs/2405.15793
- OpenHands iterative refinement: https://docs.openhands.dev/sdk/guides/iterative-refinement
- Cadence Agentic AI: https://www.cadence.com/en_US/home/ai/ai-for-design.html
- Synopsys Agentic AI: https://www.synopsys.com/ai/agentic-ai.html
- ChipAgents verification bottlenecks: https://chipagents.ai/blogs/breaking-verification-bottlenecks
