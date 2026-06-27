# openPwmChipFlow Loop 演练记录

验证对象：`TargetIt/openPwmChipFlow`  
本地路径：`/Users/jiuri/data/targetIt/openPwmChipFlow`  
演练日期：2026-06-27

## 1. 项目适配性

`openPwmChipFlow` 是一个很适合验证 Loop 的项目，因为它覆盖了完整芯片 flow：

```text
requirements
  -> design spec
  -> RTL
  -> simulation
  -> synthesis
  -> PnR
  -> physical verification
  -> GDS delivery
```

它暴露的问题也不是“代码能不能写”，而是“Agent 如何可信地判断一个工程流程是否真的完成”。

## 2. Project Probe 结果

发现的关键文件：

- `phase0_spec/requirements.md`
- `phase0_spec/design_spec.md`
- `phase1_rtl/src/pwm_ctrl.v`
- `phase2_sim/run_sim.sh`
- `phase2_sim/tb/tb_pwm.v`
- `phase3_synthesis/run_synthesis.sh`
- `phase4_pnr/run_pnr.sh`
- `phase5_verification/run_verify.sh`
- `phase6_gds/run_gds.sh`
- `scripts/health_check.sh`

## 3. 实际健康检查

执行：

```bash
bash scripts/health_check.sh
```

结果：

```text
PASS=19 FAIL=0
WARN: iverilog not installed, skipping simulation smoke test
```

Loop 结论：

```text
结构健康检查通过，但仿真验证未执行。
状态应为 needs_tooling 或 partially_checked，而不是 passed。
```

这说明 Loop 必须把 `skipped` 和 `passed` 分开。

## 4. 发现的问题一：工具能力缺失不能被吞掉

`run_all.sh` 在缺少工具时会跳过：

- `iverilog` 缺失时跳过仿真；
- Docker 缺失时跳过综合和 PnR；
- Phase 3/4 未完成时跳过物理验证和 GDS。

但脚本最后仍打印“全流程执行完毕”。

对人类学习项目来说这可以接受，但对 Agent Loop 来说不够严格。

Loop 规则应改为：

```text
required stage skipped
  -> status = blocked / needs_tooling
  -> not passed
```

## 5. 发现的问题二：报告证据冲突

`phase2_sim/test_report.md` 中存在：

```text
单项测试表：多个 ❌ FAIL
总体结果：✅ ALL TESTS PASSED
```

一个简单检查可以发现：

```text
has_fail_marker = true
has_all_passed = true
```

Loop 规则应改为：

```text
report contains both fail marker and all-passed marker
  -> evidence_conflict
  -> needs_review
```

不能只看最终一句 `ALL TESTS PASSED`。

## 6. 发现的问题三：需求和规格不一致

`phase0_spec/requirements.md` 写：

```text
duty 值范围 0-255，对应占空比 0%-100%
```

`phase0_spec/design_spec.md` 写：

```text
duty=255 时占空比为 99.6%，非 100%
```

这不是简单文案问题，而是规格语义问题。

Loop 规则应改为：

```text
requirements conflict with design spec
  -> spec_ambiguity
  -> human review before generating or modifying tests
```

## 7. 发现的问题四：当前 Loop 偏前端验证，不够覆盖端到端 chip flow

原始 Loop 更偏：

```text
spec -> RTL -> testbench -> simulation -> report
```

但 `openPwmChipFlow` 需要：

```text
spec -> RTL -> sim -> synthesis -> PnR -> DRC/LVS -> GDS delivery
```

因此 Loop 必须支持阶段化状态：

- spec；
- RTL；
- simulation；
- synthesis；
- PnR；
- physical verification；
- GDS delivery。

每个阶段都要有：

- required inputs；
- required tools；
- commands；
- artifacts；
- pass/fail/skip/block status；
- evidence consistency check。

## 8. 对 Loop 的修改建议

### 增加 Project Probe Loop

在 Goal Loop 前增加：

```text
repo
  -> detect phases
  -> detect tools
  -> detect scripts
  -> detect existing reports
  -> detect stale/conflicting artifacts
  -> produce project model
```

### 增加 Capability Gate

每个阶段执行前必须判断：

```text
required tool exists?
required input exists?
required config exists?
license/docker/pdk available?
```

缺失时不能写成 pass。

### 增加 Evidence Consistency Check

检查：

- exit code 与报告是否一致；
- 单项结果与总结果是否一致；
- skipped 阶段是否被计入成功；
- 旧报告是否被当成新结果；
- 需求和规格是否矛盾；
- artifact 时间戳是否来自本次 run。

### 增加 Critic Loop

执行 Agent 完成一轮后，由 Evidence Critic 检查：

- 是否真的跑了工具；
- 是否有跳过阶段；
- 是否有证据冲突；
- 是否有规格冲突；
- 是否误把旧 artifact 当成新结果；
- 是否满足 done condition。

### 增加 End-to-End Chip Flow Loop

在 RTL MVP 之外增加完整芯片 flow：

```text
Spec
  -> RTL
  -> Simulation
  -> Synthesis
  -> PnR
  -> Physical Verification
  -> GDS Delivery
```

## 9. 本次演练结论

`openPwmChipFlow` 证明当前 Loop 的方向正确，但还不够严格。

必须新增：

- Project Probe；
- Capability Gate；
- Evidence Consistency Check；
- Stage State Machine；
- Evidence Critic；
- skipped/blocked 状态传播；
- spec conflict detection；
- stale artifact detection。

这些不是锦上添花，而是 Agent 能否被芯片工程师信任的核心。
