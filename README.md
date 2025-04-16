# Force Paste

一个通过快捷键触发的强制粘贴工具，使用虚拟键盘输入模拟用户输入剪贴板内容。

## 功能

- 通过快捷键（默认 `Ctrl+Shift+V`）触发粘贴。
- 从系统剪贴板读取文本。
- 逐字符模拟键盘输入，绕过粘贴限制。
- 支持自定义快捷键和输入延迟。

## 安装

1. 确保安装 Python 3.8+。
2. 克隆或下载本项目。
3. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```
4. 在需要管理员权限的终端中运行：

   ```bash
   python main.py
   ```

## 配置

编辑 `config.json` 文件：

- `hotkey`：快捷键组合（如 `"ctrl+shift+v"`）。
- `delay`：每个字符输入的延迟（秒，推荐 0.01）。

## 使用

1. 运行 `main.py`。
2. 复制文本到剪贴板。
3. 按快捷键（默认 `Ctrl+Shift+V`）触发粘贴。
4. 程序将逐字符输入剪贴板内容。
5. 按 `Ctrl+C` 退出程序。

## 注意事项

- 需要安装 `keyboard` 和 `pyperclip` 库。
- Windows 和 Linux 下通常需要管理员权限。
- macOS 可能需要额外配置（参考 `keyboard` 库文档）。
- 某些特殊字符可能无法正确模拟输入。

## 依赖

见 `requirements.txt`。

## 许可证

MIT License
