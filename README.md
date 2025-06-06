# 海外NAS技术支持AI助手

本仓库提供了一个完整的前后端示例，用于构建AI辅助的工单处理工具。项目基于React和Flask实现，依赖Google Gemini Pro API进行文本摘要、分析与回复生成。

## 目录结构

```
backend/               后端代码
  app.py               Flask 服务入口
  gemini_client.py     与 Gemini API 交互
  knowledge_base.py    本地知识库检索
  utils.py             文件解析工具
  requirements.txt     Python 依赖
  knowledge_files/     示例知识库文件
frontend/              前端代码（React）
  public/index.html    页面入口
  src/                 React 组件与样式
```

更多关于在 Windows Server 2012 上部署的说明请参阅 [docs/WINDOWS_DEPLOYMENT.md](docs/WINDOWS_DEPLOYMENT.md)。
