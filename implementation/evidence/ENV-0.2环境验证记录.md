# ENV-0.2环境验证记录

日期2026-11-12；本机Docker Desktop Linux引擎29.1.3，linux/amd64。此记录为实际工具执行结果，不是四人阶段签署。

| 检查 | 实际结果 |
|---|---|
| docker info | 服务端29.1.3可达，先前500/虚拟化不可用状态本轮已消失 |
| 三个基础镜像pull | Node/Python/MySQL均成功，digest已写Dockerfile/Compose |
| Linux pip-compile | Python3.12容器生成全部依赖及hash，requirements.txt存在 |
| docker compose build | frontend/backend成功；后端--require-hashes安装通过 |
| 前端npm ci | 版本断言通过，审计0项漏洞 |
| docker compose up -d --wait | 前后端healthy |
| frontend npm run build | vue-tsc及Vite编译成功 |
| backend pip check | No broken requirements found |
| 容器版本 | Node v24.14.1，npm11.11.0，Python3.12.12 |
| 宿主端口/代理 | 5173页面HTTP200，8000及5173代理health均status=ok |
| MySQL基础设施 | database profile healthy；campus_app建立临时探针，重启前后COUNT(*)均1，已删除探针表 |
| 离线镜像检查 | network none下前端node执行、后端核心依赖import通过 |
| Compose静态校验 | 默认及database配置均通过 |

MySQL本次使用本机随机口令，保存于忽略的.env，未写入证据。服务保留运行，mysql_data保留。基础环境可用于本机开发，但业务登录、问答、Worker、迁移、令牌有效期执行尚未实现。健康能力environment_only不冒充qa_mock。浏览器视觉、热更新及跨平台尚未实测；后端未做全面漏洞扫描。前端npm审计不能替代完整安全评估。

Git未提交、未推送；文件哈希见ENV-0.2-files.sha256，提供本次本地快照依据。不能以未提交推断文件未创建，也不能把此快照当成员签署。

## 新成员路径复核修订

本轮补镜像下载与离线命令、Windows+Linux/amd64已验证范围、共享目录/端口/引擎前提、顶层文件挂载和pytest exit5解释。移除无效WATCHFILES_FORCE_POLLING；临时Python路由源码修改后HTTP请求成功，日志StatReload确认重载，原文件已恢复。前端浏览器HMR和另一成员干净机器仍未实测，不以源码静态可见冒充浏览器验证。未执行任何远端操作。
