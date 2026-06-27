# 从第一性原理推导 Loop

## 1. 芯片工程的本质

芯片工程不是文本生成任务，而是高成本、强约束、强证据的工程收敛任务。

它有几个基本事实：

- 错误越晚发现，成本越高。
- 设计意图必须被精确表达。
- 每一步结果都必须能被工具或工程证据验证。
- 不能为了通过局部检查而破坏上游规格或下游签核。
- 没有可复现证据的“完成”不可信。

所以 OpenChipAgent 的 Loop 不能从“模型怎么回答”出发，而要从“工程系统怎么收敛”出发。

## 2. 第一性原理问题

任何一个 Loop 都必须回答七个问题：

1. 当前目标是什么？
2. 当前世界状态是什么？
3. 当前缺少什么信息？
4. 下一步最小可验证动作是什么？
5. 动作完成后得到什么证据？
6. 证据是否一致、充分、可复现？
7. 这次经验是否能沉淀到下一次？

如果一个 Agent loop 不能回答这些问题，它就只是自动化脚本加聊天界面。

## 3. 芯片验证 Agent 的最小状态机

```text
unknown
  -> probed
  -> specified
  -> planned
  -> assets_ready
  -> tool_run
  -> evidence_checked
  -> repaired_or_reviewed
  -> regression_checked
  -> passed / failed / blocked / needs_review
```

状态必须明确，不允许把 `skipped` 当成 `passed`。

## 4. 三种证据

### 工具证据

- exit code；
- log；
- waveform；
- coverage；
- DRC/LVS/STA/report；
- generated artifacts。

### 规格证据

- requirement；
- design spec；
- interface；
- timing/reset/protocol；
- acceptance criteria。

### 操作证据

- command；
- cwd；
- tool version；
- patch；
- rerun record；
- human review decision。

## 5. 三类一致性检查

### 需求一致性

例如需求写 `duty=255` 对应 100%，规格写 `duty=255` 只有 255/256。Loop 必须发现这是 spec ambiguity，而不是直接继续。

### 报告一致性

例如单项测试表显示 FAIL，但总体结果写 ALL TESTS PASSED。Loop 必须判定为 evidence conflict，而不是只看最终一句 PASS。

### 阶段一致性

例如仿真、综合、PnR 因缺工具被跳过，但总脚本打印“全流程完成”。Loop 必须把阶段状态记录为 skipped / blocked，而不是 passed。

## 6. 最小动作原则

每一次 loop 迭代只做一个最小可验证动作：

- 先探测项目结构，不直接改代码。
- 先跑健康检查，不直接跑全量流程。
- 先定位第一根因，不盲目修复多个文件。
- 先补充验证意图，不直接生成大量 testbench。
- 先 rerun 受影响检查，再扩大到 full regression。

这个原则可以降低 Agent 误修和误判。

## 7. Human Review 的本质

Human review 不是产品缺陷，而是安全阀。

必须进入 review 的情况：

- 规格冲突；
- 验收标准改变；
- 接受 warning；
- 跳过必须阶段；
- 删除测试；
- 弱化 assertion；
- 修改接口、reset、协议、时序；
- 工具证据冲突。

## 8. 结论

从第一性原理看，OpenChipAgent Loop 应该是：

```text
以目标为锚点，
以状态机为骨架，
以工具证据为反馈，
以一致性检查为质量门，
以 human review 为安全阀，
以 skill memory 为长期学习机制。
```
