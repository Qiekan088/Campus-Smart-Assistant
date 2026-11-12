# 校园事务问答与咨询工单系统

本目录是四名实际成员的开发初始化包，采用V0、V1、V2三版实现和V3测试版。当前只建立Skill、文档及任务模板，没有启动开发或验收。

## 开始使用

把整个目录作为四人共享的项目基础，每人使用自己的工作副本。先读[项目背景与共同约定](docs/项目背景与共同约定.md)、[分阶段实现与测试计划](docs/分阶段实现与测试计划.md)，再让自己的AI读取对应Skill：

| 成员 | Skill | 技术主责 |
|---|---|---|
| A | [.agents/skills/campus-qa-a-frontend/SKILL.md](.agents/skills/campus-qa-a-frontend/SKILL.md) | 前端工程 |
| B | [.agents/skills/campus-qa-b-backend/SKILL.md](.agents/skills/campus-qa-b-backend/SKILL.md) | 业务后端与数据库 |
| C | [.agents/skills/campus-qa-c-retrieval/SKILL.md](.agents/skills/campus-qa-c-retrieval/SKILL.md) | 文档处理、Worker与检索 |
| D | [.agents/skills/campus-qa-d-answer/SKILL.md](.agents/skills/campus-qa-d-answer/SKILL.md) | 在线问答与模型集成 |

通用初始化提示：

> 我负责成员A（按实际替换为B/C/D）。请读取本项目AGENTS.md、对应角色SKILL.md及其必读文件。先说明当前阶段、我的交付范围、依赖和需要协商的问句；不要越过阶段门槛。当前任务以我提供的任务卡为准。

支持项目级Skill发现的工具可在打开本目录后使用相应Skill；其他AI工具直接读取文件即可。无需把四份Skill同时放入同一个成员会话。复制Skill时须连同整个项目中的公共文档一起带走，不能只复制一个SKILL.md。

## 当前基线索引

| 资产 | 入口 | 当前状态 |
|---|---|---|
| 范围与协作 | [共同约定](docs/项目背景与共同约定.md) | 用户已确定四人技术分工、3+1迭代、全员阶段门槛、局域网范围 |
| 需求 | [需求规格说明书](docs/需求规格说明书.md) | 开发用初始工作稿，待四人复核 |
| 架构 | [架构讨论稿](docs/软件架构设计方案_讨论稿.md) | 讨论基础；基线版待Q/ADR评审后形成 |
| 决策 | [Q与ADR](docs/架构确认与决策记录.md) | 保留开放问题，不预填确认 |
| 接口 | [接口与关键设计](docs/接口与关键设计说明书.md) | 列责任和待确认内容，尚未冻结具体协议 |
| 版本与任务 | [阶段计划](docs/分阶段实现与测试计划.md)、[任务模板](docs/记录模板.md) | 当前V0准备；无实际成员阶段签署 |
| 验收 | [阶段验收记录](docs/阶段验收记录.md) | V0—V3均未验收，下一阶段未放行 |
| 证据 | [证据索引](evidence/证据索引.md) | 尚无本轮实施证据 |
| 课程依据 | [教师操作指引](references/架构设计后确认与分阶段实现操作指引.md) | 原文留存 |

本轮服务器、公网、域名、云资源和部署运维不安排。先完成局域网联调和可重复启动说明。历史原型及八个DSH模拟会话不属于本轮四名同学已经完成的工作。
