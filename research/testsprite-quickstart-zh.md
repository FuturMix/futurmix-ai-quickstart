# TestSprite MCP Server 中文快速入门指南

> 本文档是 TestSprite 官方快速入门文档的中文翻译，涵盖简介、安装和首次测试三部分。
> 原文地址：https://docs.testsprite.com/mcp/getting-started/

---

## 第一部分：简介

### TestSprite MCP Server 是什么？

TestSprite 是最简单的 AI 软件测试代理，支持全自动测试。我们的无代码 AI 可以在 **10-20 分钟**内完成测试周期，让你无需手动 QA 即可放心发布。

TestSprite MCP Server 是一个模型上下文协议（Model Context Protocol）集成工具，让你的 IDE AI 助手能够直接在编辑器中管理整个 TestSprite 工作流。

> MCP 是一个用于连接 AI 应用程序和外部系统的开源标准。了解更多：https://modelcontextprotocol.io/

### 快速导航

1. **概览** — 了解 TestSprite MCP Server 的功能
2. **安装 MCP Server** — 在两分钟内完成安装
3. **运行首次 MCP 测试** — 10 分钟内完成你的第一次自动化测试
4. **测试工作流** — 理解完整的测试流程
5. **管理 API 密钥** — 创建和管理你的 TestSprite API 密钥
6. **加入社区** — 在 Discord 与其他用户交流：https://discord.com/invite/QQB9tJ973e

### 核心功能

- **全自动测试** — AI 自主完成从代码分析到测试报告的全流程
- **无代码方式** — 无需编写测试脚本，自然语言即可驱动
- **MCP 集成** — 直接在 IDE 中操作，无需切换工具

### 支持的技术栈

**前端：** React、Vue、Angular、Svelte、Next.js、Vite、原生 JavaScript/TypeScript

**后端：** Node.js、Python、Java、Go、Express.js、FastAPI、Spring Boot、REST APIs、GraphQL

### 测试覆盖范围

- **前端**：业务流程端到端测试（用户旅程、表单、认证流程）
- **后端**：API 和集成测试（功能工作流、Schema 验证、安全测试）

---

## 第二部分：安装

在两分钟内完成 TestSprite MCP Server 的安装配置。

### 前置条件

安装 TestSprite MCP Server 之前，请确保你已具备：

1. **兼容的 IDE** — 支持 Trae、Cursor、Claude Code、Windsurf、VS Code、GitHub Copilot
2. **TestSprite 账户** — 免费注册即可
3. **Node.js >= 22** — 下载地址：https://nodejs.org（运行 MCP 服务器所需）

> **如何检查 Node.js 版本？**
> 在终端运行 `node --version` 查看当前版本。

### 获取 API 密钥

首先，你需要一个 TestSprite API 密钥：

1. 登录 TestSprite 控制面板
2. 进入 **Settings**（设置）> **API Keys**（API 密钥）
3. 点击 **"New API Key"**（新建 API 密钥）
4. **复制**你的 API 密钥（安装时需要使用）

### IDE 安装指南

#### Trae

1. 获取你的 API 密钥
2. 在 Trae 中，进入 `AI Sidebar > AI Management`
3. 选择 `MCP > Add > Add from Marketplace`
4. 搜索 **TestSprite** 并添加到 MCP 列表
5. **输入你的 API 密钥**，点击 **Confirm**（确认）
6. 选择 **Builder with MCP** 开始测试

#### Cursor

> **重要提示：** Cursor 默认的"Run in Sandbox"模式会限制 TestSprite 的功能。请参见下方"Cursor 沙盒模式配置"进行设置。

##### 一键安装

1. 获取你的 API 密钥
2. 点击一键安装链接
3. 在 Cursor 中**输入你的 API 密钥**
4. 开始测试

##### 手动安装

1. 打开 Cursor 设置（`Command+Shift+J`）
2. 进入 **Tools & Integration**（工具与集成）
3. 点击 **Add custom MCP**（添加自定义 MCP）
4. **添加**以下配置：

```json
{
  "mcpServers": {
    "TestSprite": {
      "command": "npx",
      "args": ["@testsprite/testsprite-mcp@latest"],
      "env": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

5. 检查 TestSprite MCP 服务器图标旁是否出现绿色圆点，确认工具已成功加载。

##### Cursor 沙盒模式配置

Cursor 最近更新后默认以"Run in Sandbox"模式运行 MCP 工具，此模式会限制 MCP 工具功能，导致 TestSprite 测试流程无法正常调用。

解决方法：
1. 进入 `Cursor` → `Settings` → `Cursor Settings`
2. 找到 `Chat` → `Auto-Run` → `Auto-Run Mode`，将设置更改为 **"Ask Everytime"**（每次询问）或 **"Run Everything"**（运行所有）

#### Claude Code

1. 在终端中**进入项目目录**：
   ```bash
   cd /path/to/your/project
   ```

2. **粘贴安装命令到终端**：
   ```bash
   claude mcp add TestSprite --env API_KEY=your_api_key -- npx @testsprite/testsprite-mcp@latest
   ```

3. 将 `your_api_key` 替换为你的实际 TestSprite API 密钥

4. **运行**安装命令

5. **验证安装**，在项目目录中运行：
   ```bash
   claude mcp list
   ```

   你应该能看到：
   ```
   TestSprite: npx @testsprite/testsprite-mcp@latest - Connected
   ```

> **注意：** 通过此方式安装的 MCP 服务器仅对**当前项目目录**下的 Claude Code 生效。如果在其他项目目录使用 Claude Code，需要重新添加 MCP 服务器。如需全局安装，请参考 Claude Code MCP 文档。

#### VS Code

1. **打开**命令面板（`Command+Shift+P`）
2. **运行** `MCP: Add Server` 命令
3. **选择** Command (stdio) 安装类型
4. **输入** `npx @testsprite/testsprite-mcp@latest` 作为运行命令
5. **输入** `TestSprite` 作为 MCP 服务器标识名称
6. **选择** MCP 服务器配置的作用范围
7. **添加** `env` 配置：

```json
{
  "servers": {
    "testsprite": {
      "command": "npx",
      "args": ["-y", "@testsprite/testsprite-mcp@latest"],
      "env": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

8. 安装完成后，在配置的 `mcp.json` 文件中点击 TestSprite MCP 条目上方的 `start` 按钮。如果服务器启动无错误且所有工具均已加载，则安装成功。

#### 其他 IDE

将以下配置添加到你的 MCP 设置中：

```json
{
  "mcpServers": {
    "TestSprite": {
      "command": "npx",
      "args": ["@testsprite/testsprite-mcp@latest"],
      "env": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

### 安装验证

**成功标志：**
- AI 助手能够看到 **TestSprite MCP 工具**
- 没有出现 **"command not found"** 错误
- 可以开始测试你的项目

**快速测试：** 尝试在 IDE 中输入以下提示：

```
Help me test this project with TestSprite.
```

你的 AI 助手应该会提供使用 TestSprite MCP 工具的选项。

### 卸载

移除 TestSprite MCP Server：

1. 从 IDE 的 MCP 设置中**删除配置**
2. **重启 IDE**

---

## 第三部分：运行首次 MCP 测试

> 在 10 分钟内体验 TestSprite MCP Server 的自动化测试魔力。

完成本指南后，你将：
- 运行第一个**自动化测试套件**
- 看到 AI 生成全面的测试计划
- 观看测试在云端执行
- 收到详细的测试报告
- 应用**自动 Bug 修复**

> **提示：** 开始之前，请确保已安装 TestSprite MCP Server 并**打开你的 IDE**。

### 步骤 1：准备项目

**启动你的应用** — 确保应用在本地正常运行：

```bash
# 前端应用（示例）
npm run dev          # 通常运行在 3000、5173 或 8080 端口

# 后端应用（示例）
node index.js        # 通常运行在 8000、3001 或 4000 端口
```

项目结构示例：

```text
my-project/
├── frontend/          # React、Vue、Angular 等
│   ├── src/
│   ├── package.json
│   └── ...
├── backend/           # Node.js、Python 等
│   ├── app.py
│   ├── requirements.txt
│   └── ...
├── README.md
└── package.json
```

### 步骤 2：魔法命令

打开 **IDE 聊天窗口**，按以下步骤操作：

1. **打开** IDE 中的新聊天窗口
2. **输入**魔法命令：

```text
Can you test this project with TestSprite?
```

3. 如需测试特定子项目，可将项目文件夹拖放到聊天窗口中
4. 按 `Shift+Enter` 发送

就这样！你的 AI 助手将接管整个过程，引导你完成测试流程。

### 步骤 3：配置（必需）

> **注意：** 测试配置页面将在浏览器中打开。在此完成设置以继续测试。

需要配置以下内容：

#### 1. 测试类型

**模式：**
- **Frontend（前端）** — 选择此项来测试 UI 和用户流程（如按钮、表单、导航）
- **Backend（后端）** — 选择此项来测试 API、服务或服务器逻辑

**范围：**
- **Codebase（整个代码库）** — 对整个项目运行测试。首次运行或需要全面测试时使用
- **Code Diff（代码变更）** — 仅对最近的变更运行测试（未提交的 Git 变更）。快速验证新代码时使用

#### 2. 测试账户凭证

如果你的应用需要登录：

**前端：**
```
用户名：test@example.com
密码：your-test-password
```

**后端认证类型：**

| 认证类型 | 说明 |
| :--- | :--- |
| Basic | 使用用户名和密码 |
| Bearer | 基于安全令牌的认证 |
| API-key | 使用唯一的 API 密钥访问 |
| None | 无需认证 |

#### 3. 应用 URL

```text
前端：http://localhost:5173
后端：http://localhost:4000
```

#### 4. 产品需求文档（PRD）

上传现有的 PRD（必需）。即使是草稿或低质量的 PRD 也可以。TestSprite AI 会根据你的上传生成标准化的 PRD。

### 步骤 4：自动化工作流

AI 助手将自动处理**整个测试过程**，从理解项目到运行实际测试的每一步都会自动完成，无需手动操作。

### 步骤 5：查看测试结果

测试完成后，项目中会生成以下文件：

```text
testsprite_tests/
├── tmp/
│   ├── prd_files/                 # 上传的 PRD 文件
│   ├── config.json               # 测试配置
│   ├── code_summary.json         # 代码分析
│   ├── report_prompt.json        # AI 分析数据
│   └── test_results.json         # 详细测试结果
├── standard_prd.json             # 标准化 PRD
├── TestSprite_MCP_Test_Report.md # 人类可读的报告
├── TestSprite_MCP_Test_Report.html # HTML 报告
├── TC001_Login_Success_with_Valid_Credentials.py
├── TC002_Login_Failure_with_Invalid_Credentials.py
└── ...                           # 其他测试文件
```

**理解测试结果** — 测试报告展示整体覆盖率、通过率、失败测试的详细分析，以及测试类别（功能、UI/UX、安全、性能）。

### 步骤 6：自动 Bug 修复

**请求修复** — 查看测试结果后，只需说：

```text
Please fix the codebase based on TestSprite testing results.
```

AI 将：
- 分析失败的测试
- 定位问题代码
- 自动应用修复
- 重新运行测试验证修复结果
- 反复迭代直到问题解决

### 测试输出示例

**生成的测试计划：**

```json
{
  "testCases": [
    {
      "id": "TC001",
      "title": "User Authentication Login",
      "description": "Test user login with valid credentials",
      "category": "Functional",
      "priority": "High",
      "steps": [
        "Navigate to login page",
        "Enter valid username and password",
        "Click login button",
        "Verify successful login"
      ]
    }
  ]
}
```

**测试报告摘要：**

```json
{
  "summary": {
    "totalTests": 18,
    "passed": 12,
    "failed": 6,
    "passRate": "67%",
    "coverage": "85%"
  },
  "failures": [
    {
      "testId": "TC005",
      "title": "Admin Panel Access",
      "error": "Button not found: #admin-delete-btn",
      "recommendation": "Add missing delete button in admin panel"
    }
  ]
}
```

### 成功秘诀

- **确保应用正在运行** — 前端和后端应在标准端口上可访问
- **项目结构** — 包含 README 和有描述性的文件夹名称
- **测试凭证** — 准备使用非生产数据的测试账户
- **检查生成的文件** — 验证生成的 PRD 和测试计划的准确性

### 下一步

🎉 **恭喜！** 你已成功运行了第一次 TestSprite MCP Server 自动化测试。

- **完整测试工作流** — 了解完整流程
- **查看示例** — 查看真实场景用例
- **加入 Discord** — 获取帮助并分享经验：https://discord.com/invite/GXWFjCe4an
- **GitHub 贡献** — 贡献代码和报告问题：https://github.com/wangy44624/docs

---

> 本翻译由 FuturMix 团队完成，基于 TestSprite 官方英文文档。如有疑问或翻译建议，欢迎反馈。
