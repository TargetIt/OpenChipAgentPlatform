# Promotion Sources

版本：2026-06-27

这些资料用于支撑 `investor_partner_deck_draft.md` 中的公开事实、行业趋势和对标分析。材料中的商业判断是我们的推论，公开来源只用于事实锚点。

## EDA 行业与设计流程

1. Synopsys glossary: What is Electronic Design Automation  
   https://www.synopsys.com/glossary/what-is-electronic-design-automation.html  
   用途：说明 EDA 工具覆盖芯片设计、验证、制造准备等流程，以及 AI 正在提升 EDA 效率和质量。

2. ChipVerify: ASIC/SoC Chip Design Flow  
   https://chipverify.com/verilog/asic-soc-chip-design-flow  
   用途：说明 ASIC 设计流程从 specification/architecture 到 implementation/verification，再到 fabrication/validation。

3. Techlabs Semi: End-to-End ASIC Design Flow Explained  
   https://techlabssemi.com/blogs/end-to-end-asic-design-flow-explained-from-specification-to-tape-out/  
   用途：说明从规格、RTL、验证、物理设计、signoff、tape-out 到 post-silicon validation 的完整流程。

## 验证瓶颈与质量压力

4. Siemens / Wilson Research Group 2024 IC/ASIC Functional Verification Study  
   https://resources.sw.siemens.com/en-US/white-paper-2024-wilson-research-group-ic-asic-functional-verification-trend-report/  
   用途：公开摘要提到 first-silicon success rate 下降到 20 年低点，只有 14% 项目达到首次硅成功。

5. Verification Academy: 2024 Wilson Research Group IC/ASIC Functional Verification Trend Report  
   https://verificationacademy.com/topics/planning-measurement-and-analysis/wrg-industry-data-and-trends/2024-siemens-eda-and-wilson-research-group-ic-asic-functional-verification-trend-report/  
   用途：验证复杂度、SoC、安全/功能安全、异步时钟域等因素推高验证挑战。

6. ChipAgents blog list  
   https://chipagents.ai/blogs  
   用途：公开博客标题中提到 verification consumes 60-70% of chip engineering hours，用作验证瓶颈的公开说法之一。

7. Synopsys VSO.ai  
   https://www.synopsys.com/ai/ai-powered-eda/vso-ai.html  
   用途：Synopsys 对 AI-driven verification 的公开案例，提到减少 functional coverage holes 和提升 IP verification productivity。

## AI Agent + EDA 对标

8. ChipAgents official site  
   https://chipagents.ai/  
   用途：ChipAgents/Alpha Design AI 的官方定位：AI-native EDA，设计和验证 agent。

9. Semiconductor Engineering entity page: ChipAgents  
   https://semiengineering.com/entities/alpha-design-ai-chipagents/  
   用途：概括 ChipAgents 覆盖 spec、RTL、testbench、verification、debug 等任务。

10. PR Newswire: Introducing ChipAgents  
    https://www.prnewswire.com/news-releases/introducing-chipagents-the-worlds-first-ai-agent-for-chip-design-and-verification-302267497.html  
    用途：ChipAgents 对外发布信息，说明其面向硬件工程师和验证团队，强调效率、准确性和 time-to-market。

11. BusinessWire: ChipAgents Raises $74M  
    https://www.businesswire.com/news/home/20260217568914/en/ChipAgents-Raises-%2474M-to-Scale-an-Agentic-AI-Platform-to-Accelerate-Chip-Design  
    用途：ChipAgents 融资和 agentic AI chip design 平台的公开市场信号。

12. Cadence: Agentic AI for Chip Design  
    https://www.cadence.com/en_US/home/ai/ai-for-design.html  
    用途：Cadence 对 agentic AI chip design 的定义，包括目标驱动、工具执行、结果评估、迭代到 verified outcome。

13. Synopsys Chinese blog: AI+EDA 提升芯片验证覆盖率  
    https://www.synopsys.com/zh-cn/blogs/chip-design/ai-verification.html  
    用途：AI 在验证覆盖率收敛中的公开案例和 EDA 厂商叙事。

## 国内对标：智维创芯 / ChatDV

14. 集微网：智维创芯完成数千万级天使轮融资  
    https://www.ijiwei.com/n/1047720  
    用途：智维创芯公司背景、EDA 国创中心孵化、ChatDV、设计-验证-优化全链路 AI 智能工具平台等公开信息。

15. 36氪：实现芯片设计验证自动化，提升开发效率10倍以上  
    https://m.36kr.com/p/3838488706370054  
    用途：智维创芯定位、ChatDV 覆盖测试生成、断言生成、参考模型构建、自动调试，以及效率/周期/成本相关公开表述。

16. 新浪财经转载：智维创芯 ChatDV  
    https://finance.sina.com.cn/stock/t/2026-06-04/doc-iniafvzr2546899.shtml  
    用途：智维创芯融资、产品和商业化落地相关公开报道交叉验证。

## 市场规模参考

17. SemiAnalysis: EDA Market Primer  
    https://newsletter.semianalysis.com/p/eda-market-primer  
    用途：EDA 大三家集中度和 EDA+IP 市场规模的行业分析参考。

18. Persistence Market Research: EDA Market Size  
    https://www.persistencemarketresearch.com/market-research/electronic-design-automation-eda-market.asp  
    用途：EDA 市场规模与 CAGR 预测参考。

19. P&S Intelligence: EDA Market Analysis  
    https://www.psmarketresearch.com/market-analysis/electronic-design-automation-market  
    用途：EDA 市场规模和增长预测交叉参考。

## 使用注意

- 市场规模数字来自第三方市场研究或行业分析，口径差异较大，正式融资材料中应选择一个主口径并注明来源。
- 智维创芯和 ChipAgents 的效率提升数据多来自公司宣传或媒体报道，正式材料中建议写成“公开报道/公司宣称”，不要写成我们已独立验证的事实。
- “AI Agent 时代价值向 EDA/Agent 平台迁移”是我们的投资判断，不是公开事实，应在 PPT 中表述为 thesis。
