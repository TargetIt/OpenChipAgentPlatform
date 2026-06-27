# 执行闭环设计

OpenChipAgent Loop 的完整执行链路如下：

```text
项目探测
  -> 用户目标
  -> 结构化规格
  -> 验证计划
  -> 生成验证资产
  -> 执行 EDA 工具
  -> 读取证据
  -> 证据一致性检查
  -> 失败分类
  -> 修复/补充
  -> 回归验证
  -> 出口判定
  -> 报告/沉淀经验
```

## 0. Project Probe Loop：先理解项目和环境

陌生项目不能直接进入生成或修复。必须先建立项目模型：

```text
repo
  -> detect phases
  -> detect RTL/testbench/scripts/configs/reports/artifacts
  -> detect tools and licenses
  -> detect existing stale artifacts
  -> detect known reports and run history
  -> produce project model
```

输出应包括：

- 项目阶段：spec、RTL、sim、synthesis、PnR、physical verification、GDS；
- 每阶段入口脚本；
- 每阶段所需工具；
- 每阶段关键产物；
- 当前可执行能力；
- 已存在报告是否来自当前 run；
- 明确哪些阶段会被 skipped。

`openPwmChipFlow` 演练证明：如果没有 Project Probe，Agent 很容易把“缺工具导致跳过”误判成“流程完成”。

## 1. Goal Loop：把自然语言目标变成可执行目标

输入可能是：

- “帮我验证这个 FIFO”
- “这个 AXI 模块回归失败了，帮我 debug”
- “帮我补齐 coverage”
- “帮我给这个 RTL 生成 testbench”

Agent 第一件事不是写代码，而是把目标结构化：

```text
用户输入
  -> 识别模块、接口、协议、reset、clock、验收标准
  -> 发现缺失信息
  -> 必要时追问
  -> 生成 goal.json / spec.md
```

关键规则：

- 缺少接口、reset、协议、验收标准时，不允许直接开干。
- goal 一旦确定，Agent 不能自己偷偷改目标。
- 后续所有动作都要回到 goal 判断是否完成。

## 2. Plan Loop：生成验证计划

结构化规格之后，Agent 要先规划验证，而不是直接写 testbench。

```text
spec
  -> 提取功能点
  -> 提取 corner cases
  -> 生成 directed tests
  -> 生成 random tests
  -> 生成 assertions
  -> 生成 coverage points
  -> 定义出口标准
```

验证计划要回答：

- 要测什么？
- 怎么测？
- 怎么判断对错？
- 覆盖率目标是什么？
- 哪些场景必须人工确认？

这里的核心是：AI 生成代码之前，先生成验证意图。

## 3. Asset Loop：生成验证资产

然后进入生成阶段：

```text
verification plan
  -> testbench
  -> driver / monitor / scoreboard
  -> reference model
  -> assertions
  -> coverage model
  -> run scripts
```

分阶段支持：

- MVP：cocotb / Python reference model / Verilator。
- 下一阶段：SystemVerilog testbench。
- 再下一阶段：UVM component / sequence / scoreboard / coverage。
- 工业阶段：商业仿真器、coverage database、regression system。

## 4. Execution Loop：跑真实工具

这是 Agent 和普通 Chatbot 的核心区别。

```text
生成资产
  -> 编译
  -> lint
  -> simulation
  -> coverage
  -> regression
  -> formal / assertion check
```

每个命令都要记录：

- command；
- cwd；
- tool version；
- stdout / stderr；
- exit code；
- log path；
- artifact path；
- start / end time。

Agent 不允许只说“应该通过”，必须跑工具。

## 4.5 Capability Gate：跳过不是通过

每个阶段执行前必须判断：

```text
required input exists?
required tool exists?
required license/docker/pdk exists?
required config exists?
```

如果能力缺失：

```text
status = blocked / needs_tooling / skipped
```

不能写成：

```text
status = passed
```

对于芯片工程，`skipped` 是一个正式状态，必须传递到最终报告。

## 5. Evidence Loop：读取证据

工具跑完后，Agent 要读结果：

```text
log
  -> 错误摘要
  -> 第一处真实失败
  -> 失败位置
  -> 失败类型
  -> 关联源代码
  -> 关联 spec / test / waveform / coverage
```

证据包括：

- 编译错误；
- 仿真 log；
- assertion fail；
- waveform；
- coverage hole；
- scoreboard mismatch；
- lint warning；
- synthesis warning。

关键点：Agent 要学会从海量 log 中定位第一根因，而不是只看最后一行。

## 5.5 Evidence Consistency Loop：检查证据是否互相矛盾

工具证据不仅要存在，还要一致。

必须检查：

- exit code 与报告结论是否一致；
- 单项测试结果与总体结果是否一致；
- log 中是否存在 FAIL / ERROR / WARNING；
- 是否有 skipped 阶段被写成完成；
- 旧 artifact 是否被当成本次 run 结果；
- requirement 与 design spec 是否冲突；
- coverage/DRC/LVS/GDS 结论是否有对应原始报告。

典型规则：

```text
report has FAIL marker and ALL PASSED marker
  -> evidence_conflict
  -> needs_review

required stage skipped
  -> not passed
  -> needs_tooling or blocked

requirements conflict with design spec
  -> spec_ambiguity
  -> human review
```

这是从 `openPwmChipFlow` 演练中得到的重要修正。

## 6. Failure Classification Loop：失败分类

失败必须分类，不然无法沉淀。

```text
failure
  -> spec ambiguity
  -> RTL bug
  -> testbench bug
  -> reference model bug
  -> assertion bug
  -> coverage gap
  -> tool config error
  -> environment error
  -> unknown
```

每类失败对应不同动作：

- RTL bug：提出修复建议，通常需要人确认。
- testbench bug：可自动修，但需要回归。
- spec ambiguity：必须追问。
- coverage gap：补 test / coverage point。
- tool config error：修脚本。
- unknown：降级为人工 review。

## 7. Repair Loop：修复或补充

修复不能乱来，要有边界。

```text
classified failure
  -> 判断是否 safe auto repair
  -> 生成最小修改
  -> 记录 patch
  -> 解释为什么改
  -> 重新运行受影响检查
```

必须 human review 的情况：

- 改接口；
- 改 reset 语义；
- 改协议；
- 删除测试；
- 弱化 assertion；
- suppress warning；
- 接受 mismatch；
- 修改验收标准。

这里必须防止 Agent 为了通过而作弊。

## 8. Regression Loop：回归验证

任何修复都必须回归。

```text
patch
  -> rerun failed test
  -> rerun related tests
  -> rerun smoke regression
  -> update coverage
  -> update report
```

不能只跑刚失败的 case。至少要有：

- failed test rerun；
- related tests rerun；
- smoke regression；
- coverage delta。

## 9. Exit Loop：出口判定

最后要判断是否完成。

```text
done?
  -> spec complete
  -> tests pass
  -> coverage acceptable
  -> no critical warning
  -> all failures resolved or reviewed
  -> report generated
```

输出状态建议分五类：

- `passed`
- `failed`
- `blocked`
- `needs_review`
- `in_progress`
- `skipped`
- `needs_tooling`

企业客户不接受“模糊完成”，所以状态必须明确。

## 9.5 Evidence Critic Loop：独立检查 Done Condition

执行 Agent 完成一轮后，需要一个 Evidence Critic 检查：

- goal 是否被满足；
- required stage 是否真的执行；
- skipped 是否被误报为 pass；
- report 是否存在内部矛盾；
- spec 是否存在上游冲突；
- 修复后是否 rerun；
- artifact 是否来自本次 run；
- human review gate 是否被绕过。

这可以是独立 Agent，也可以是同一 Agent 的独立模式，但它必须使用不同的检查清单。

## 10. Learning Loop：经验沉淀

每次 run 结束后，沉淀经验：

```text
run result
  -> failure taxonomy
  -> repair action
  -> reusable skill
  -> project memory
  -> benchmark case
```

示例：

- “Yosys 不支持某种 SystemVerilog 写法，替换成保守写法。”
- “AXI ready/valid 死锁常见于 valid 依赖 ready。”
- “coverage hole 来自 reset during transaction。”
- “scoreboard mismatch 先检查 reference model latency。”

这些经验会逐渐变成产品壁垒。
