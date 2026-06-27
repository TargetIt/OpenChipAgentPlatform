# Loop 的目的

## 不是一上来自动设计完整芯片

OpenChipAgentPlatform 的 Loop 不是让用户说一句话，AI 就直接生成完整芯片。

完整芯片设计涉及：

- 产品需求；
- 架构设计；
- RTL 实现；
- 验证；
- 综合；
- DFT；
- 后端；
- signoff；
- tape-out；
- post-silicon validation。

这些环节复杂度很高，且任何一个错误都可能带来极大成本。短期直接承诺“自动设计芯片”不现实，也不可信。

## 第一目的：把 AI 从聊天工具变成工程执行者

普通 AI 的模式是：

```text
用户提问
  -> AI 回答
```

OpenChipAgent Loop 的模式是：

```text
用户给工程目标
  -> AI 拆解目标
  -> AI 调用工具
  -> AI 读取结果
  -> AI 分类失败
  -> AI 修复或请求人工判断
  -> AI 回归验证
  -> AI 输出可审计报告
```

所以 Loop 的第一目的，是让 AI 不只是“说”，而是在真实工程环境里“做”。

## 第二目的：用 Harness 管住 AI

Harness 不是芯片，也不是 EDA 工具。Harness 是约束 Agent 的工程规则系统。

Harness 规定：

- 目标怎么定义；
- 规格怎么结构化；
- 工具怎么调用；
- 日志怎么保存；
- 失败怎么分类；
- 哪些动作可以自动修；
- 哪些动作必须问人；
- 什么时候算完成；
- 最后怎么生成报告。

没有 Harness，AI 很容易：

- 写一段看起来合理但没有验证过的 RTL；
- 写一个覆盖不充分的 testbench；
- 遇到失败后乱改；
- 为了通过测试弱化测试；
- 跑完几个 case 就宣称完成；
- 没有完整证据链。

有 Harness，AI 必须在工程规则里执行。

## 第三目的：先成为可靠验证 Agent，再扩展到设计 Agent

当前最合理的落点是：

```text
用 Harness 驱动 AI 做芯片验证任务。
```

第一阶段任务包括：

- 读取 spec / RTL；
- 生成验证计划；
- 生成 cocotb / SystemVerilog / UVM 验证资产；
- 运行 lint / simulation / coverage；
- 读取 log / waveform / coverage；
- 分类失败；
- 智能 debug；
- 修 testbench 或建议 RTL 修复；
- 回归验证；
- 输出报告。

验证闭环跑通后，再扩展到：

```text
小模块 RTL 生成
  -> RTL + 验证协同
  -> IP 级设计验证
  -> 子系统级验证
  -> 更完整的芯片设计辅助
```

## 为什么先做验证

验证最适合建立 Loop，因为它具备：

- 明确输入：spec、RTL、testbench、bug、coverage gap；
- 明确工具反馈：仿真、lint、coverage、assertion、log；
- 明确成功标准：测试通过、覆盖率达标、失败解释清楚；
- 明确客户痛点：质量、速度、成本；
- 明确风险控制：不能随便改规格、不能弱化测试。

设计也可以做，但设计更容易出现“看起来对、实际错”的风险。先用验证来约束 AI，可以更快建立确定性。

## 产品化表达

```text
Harness 是 AI Agent 进入芯片工程的操作系统。
Loop 是这个操作系统里的任务执行机制。
EDA 工具是确定性反馈源。
Human Review 是安全阀。
Skill Memory 是长期壁垒。
```
