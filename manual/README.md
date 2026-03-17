# 📝 manual/main.py 修改说明

**修改时间：** 2026-03-16  
**修改内容：** 添加 `__main__` 启动部分 + 修复 Channel 接口

---

## ✅ 主要修改

### 1. 添加 `__main__` 启动部分

```python
if __name__ == "__main__":
    import asyncio
    
    print("🚀 启动 Cota 天气机器人 (manual 模式)...")
    print(f"📁 配置路径：{config_path}")
    print(f"🔍 绝对路径：{os.path.abspath(config_path)}")
    print("=" * 50)
    
    controller = Controller()
    
    try:
        asyncio.run(controller.agent_loop())
    except KeyboardInterrupt:
        print("\n\n👋 已退出机器人")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 发生错误：{e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
```

### 2. 修复配置路径（使用绝对路径）

```python
# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 配置路径（使用绝对路径）
config_path = os.path.join(script_dir, '..', 'cota', 'bots', 'weather')
```

**原因：** 避免从不同目录运行时路径错误

### 3. Controller 继承 Channel 类

```python
from cota.channels.channel import Channel

class Controller(Channel):
    """命令行控制器，继承 Channel 以实现必要的接口"""
```

**原因：** `agent.processor.handle_message` 需要 channel 对象实现 `send_response` 方法

### 4. 实现 Channel 必要接口

```python
async def send_text_message(self, recipient_id: Text, **kwargs: Any) -> None:
    """发送文本消息到控制台"""
    text = kwargs.get('text', '')
    if text:
        print(f"Bot: {text}")

async def send_image_url(self, recipient_id: Text, **kwargs: Any) -> None:
    """发送图片消息到控制台"""
    image_url = kwargs.get('image_url', '')
    if image_url:
        print(f"Bot: [图片] {image_url}")
    else:
        await self.send_text_message(recipient_id, **kwargs)
```

---

## 🚀 使用方法

### 方法 1：直接运行脚本

```bash
cd /Users/maomin/programs/vscode/cota
source .venv/bin/activate
python manual/main.py
```

### 方法 2：使用绝对路径运行

```bash
source /Users/maomin/programs/vscode/cota/.venv/bin/activate
python /Users/maomin/programs/vscode/cota/manual/main.py
```

---

## 💬 对话示例

```
🚀 启动 Cota 天气机器人 (manual 模式)...
📁 配置路径：/Users/maomin/programs/vscode/cota/manual/../cota/bots/weather
🔍 绝对路径：/Users/maomin/programs/vscode/cota/cota/bots/weather
==================================================
Input message:
你好
Bot: 你好，请问有什么可以帮您？

Input message:
北京天气怎么样
Bot: [查询天气并回复]

Input message:
/stop
👋 已退出机器人
```

---

## 📋 修改对比

### 修改前
```python
config_path = '../cota/bots/weather'  # ❌ 相对路径

class Controller():  # ❌ 未继承 Channel
    pass

# ❌ 没有 __main__ 部分
```

### 修改后
```python
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, '..', 'cota', 'bots', 'weather')  # ✅ 绝对路径

class Controller(Channel):  # ✅ 继承 Channel
    async def send_text_message(self, ...):  # ✅ 实现接口
        pass

if __name__ == "__main__":  # ✅ 添加启动部分
    asyncio.run(controller.agent_loop())
```

---

## 🔧 技术细节

### 为什么需要继承 Channel？

`agent.processor.handle_message` 的签名：
```python
async def handle_message(self, message: Message, channel: Channel)
```

在 `execute_channel_effects` 中会调用：
```python
await channel.send_response(session_id, message)
```

所以 channel 必须实现：
- `send_response()` - 发送响应（基类已实现）
- `send_text_message()` - 发送文本（需要实现）
- `send_image_url()` - 发送图片（需要实现）

### 为什么使用绝对路径？

相对路径 `../cota/bots/weather` 在以下情况会失败：
- 从其他目录运行：`python /path/to/manual/main.py`
- 在 IDE 中运行（工作目录不同）
- 作为模块导入

使用 `os.path.abspath(__file__)` 确保路径始终正确。

---

## ✅ 验证

```bash
# 检查文件
ls -la /Users/maomin/programs/vscode/cota/manual/main.py

# 运行测试
cd /Users/maomin/programs/vscode/cota
source .venv/bin/activate
python manual/main.py
```

---

**修改完成！** 🎉
