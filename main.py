from pynput import keyboard as pynput_keyboard
from pynput.keyboard import Controller
import pyperclip
import time
import json
import os
import logging

# 配置日志
logging.basicConfig(
    level=logging.DEBUG,
    filename='force_paste.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_config():
    """加载配置文件"""
    default_config = {
        "hotkey": "<ctrl>+<shift>+v",
        "delay": 0.001
    }

    config_path = "config.json"
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            logging.info(f"加载配置: {config}")
            return config
        except Exception as e:
            logging.error(f"加载配置文件失败: {e}")
            print(f"加载配置文件失败: {e}，使用默认配置")
    else:
        with open(config_path, 'w') as f:
            json.dump(default_config, f, indent=4)
        logging.info("创建默认配置文件")
        print("未找到配置文件，已创建默认配置文件")
    return default_config

def simulate_typing(text, delay):
    """模拟键盘输入文本"""
    kb = Controller()
    for char in text:
        try:
            logging.debug(f"输入字符: {char}")
            kb.press(char)
            kb.release(char)
            time.sleep(delay)
        except ValueError:
            logging.warning(f"无法输入字符: {char}")
            print(f"无法输入字符: {char}")
            continue

def main():
    print("强制粘贴程序启动... 按 Ctrl+C 退出")
    logging.info("程序启动")
    config = load_config()
    hotkey = config["hotkey"]
    delay = config["delay"]
    logging.info(f"快捷键: {hotkey}, 延迟: {delay}")

    def on_activate():
        logging.info(f"检测到快捷键 {hotkey}")
        print(f"检测到快捷键 {hotkey}，开始粘贴...")
        try:
            text = pyperclip.paste()
            if not text:
                logging.warning("剪贴板为空")
                print("剪贴板为空！")
                return
        except Exception as e:
            logging.error(f"无法读取剪贴板: {e}")
            print(f"无法读取剪贴板: {e}")
            return

        try:
            simulate_typing(text, delay)
            logging.info("粘贴完成")
            print("粘贴完成！")
        except Exception as e:
            logging.error(f"模拟输入失败: {e}")
            print(f"模拟输入失败: {e}")

    # 测试快捷键解析
    try:
        logging.info(f"注册快捷键: {hotkey}")
        print(f"尝试注册快捷键: {hotkey}")
        with pynput_keyboard.GlobalHotKeys({hotkey: on_activate}) as h:
            h.join()
    except ValueError as e:
        logging.error(f"快捷键格式错误: {e}")
        print(f"快捷键格式错误: {e}")
        print("请确保 config.json 中的 hotkey 格式正确，例如 '<ctrl>+<shift>+v'")
    except Exception as e:
        logging.error(f"注册快捷键失败: {e}")
        print(f"注册快捷键失败: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("程序退出")
        print("\n程序退出")