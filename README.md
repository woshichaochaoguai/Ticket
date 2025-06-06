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

## Getting Started

此项目需要 **Python 3.9+** 和 **Node.js 16+**。以下步骤适用于 Windows、macOS 与各类 Linux 发行版。

1. 进入 `backend` 目录并创建 `.env` 文件填入 Gemini API Key：
   ```bash
   cd backend
   echo GOOGLE_API_KEY=your_api_key_here > .env
   ```
2. 安装后端依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 另开终端进入 `frontend` 并安装前端依赖：
   ```bash
   cd ../frontend
   npm install
   ```
4. 分别启动后端和前端服务：
   ```bash
   # 在 backend 目录下
   flask run --port 5001

   # 在 frontend 目录下
   npm start
   ```

完成后打开浏览器访问 `http://localhost:3000` 即可。

更多关于在 Windows Server 2012 上部署的说明请参阅 [docs/WINDOWS_DEPLOYMENT.md](docs/WINDOWS_DEPLOYMENT.md)。
