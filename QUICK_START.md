# 🚀 Cota 天气机器人 - 快速启动指南

**更新时间：** 2026-03-16 13:14  
**状态：** ✅ 已安装并测试成功

---

## 📋 快速启动（3 步）

### 1️⃣ 激活虚拟环境

```bash
cd /Users/maomin/programs/vscode/cota
source .venv/bin/activate
```

**或使用脚本：**
```bash
source activate.sh
```

### 2️⃣ 启动天气机器人

```bash
cota shell --config=cota/bots/weather --debug
```

### 3️⃣ 开始对话

```
Input message: 你好
Bot: 你好，请问有什么可以帮您？

Input message: 北京天气怎么样
Bot: [查询天气并回复]
```

---

## ✅ 验证安装

```bash
# 检查 Python 路径
which python
# 应该输出：/Users/maomin/programs/vscode/cota/.venv/bin/python

# 检查 cota 命令
which cota
# 应该输出：/Users/maomin/programs/vscode/cota/.venv/bin/cota

# 检查版本
cota --version
# 应该输出：Cota version: 1.1.1
```

---

## 🎯 常用命令

### 交互式对话
```bash
cota shell --config=cota/bots/weather
```

### 带调试信息
```bash
cota shell --config=cota/bots/weather --debug
```

### 测试 LLM 连接
```bash
python test_llm.py
```

### 运行天气机器人（脚本模式）
```bash
python run_weather_bot.py
```

### 退出虚拟环境
```bash
deactivate
```

---

## 📁 项目结构

```
/Users/maomin/programs/vscode/cota/
├── .venv/              # 虚拟环境（Poetry 创建）
├── cota/
│   └── bots/
│       └── weather/    # 天气机器人配置
│           ├── agent.yml
│           ├── endpoints.yml    # LLM 配置
│           └── policy/
│               └── data.yml     # 对话策略
├── activate.sh         # 激活脚本
├── test_llm.py         # LLM 测试
└── run_weather_bot.py  # 启动脚本
```

---

## 🔧 配置说明

### LLM 配置

**文件：** `cota/bots/weather/endpoints.yml`

```yaml
llms:
  aliyun-codingplan:
    type: openai
    model: qwen3.5-plus
    key: sk-sp-9744b2d2a3834fe1875f74fc43689dbf
    apibase: https://coding.dashscope.aliyuncs.com/v1
```

### 天气 API

**当前：** Mock 接口（测试用）  
**位置：** `cota/bots/weather/agent.yml`

如需真实天气数据，请替换为实际 API（如心知天气、和风天气）。

---

## 💡 对话策略示例

### 打招呼
```
用户：你好
机器人：你好，请问有什么可以帮您？
```

### 查询天气
```
用户：北京天气怎么样
机器人：[调用 Weather API 查询并回复]
```

### 多城市比较
```
用户：成都和重庆天气咋样哪个好
机器人：[依次查询两个城市并比较]
```

---

## ⚠️ 常见问题

### Q1: `cota: command not found`

**解决：**
```bash
# 确保激活了正确的虚拟环境
source .venv/bin/activate

# 验证
which cota
```

### Q2: `poetry env info --path` 无输出

**解决：**
```bash
# 重新配置 Poetry
poetry config virtualenvs.in-project true
poetry install
source .venv/bin/activate
```

### Q3: LLM 连接失败

**检查：**
1. API Key 是否正确
2. 网络连接是否正常
3. 查看 `endpoints.yml` 配置

---

## 📊 测试记录

**时间：** 2026-03-16 13:13  
**测试命令：** `echo "你好" | cota shell --config=cota/bots/weather`

**结果：**
```
✅ Agent loaded
✅ HTTP Request: POST ... "HTTP/1.1 200 OK"
✅ User: 你好
✅ Bot: 你好，请问有什么可以帮您？
```

---

## 🎉 开始使用

```bash
cd /Users/maomin/programs/vscode/cota
source .venv/bin/activate
cota shell --config=cota/bots/weather
```

**祝你使用愉快！** 😊
