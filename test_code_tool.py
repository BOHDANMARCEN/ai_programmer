# test_code_tool.py
import sys
import os

# Встановлюємо кодування UTF-8 для консолі Windows
if sys.platform == "win32":
    os.system("chcp 65001 > nul")

# Додаємо поточну директорію до шляху пошуку модулів
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("Тестування CodeTool...")

# Спробуємо імпортувати по-різному
try:
    from tools.code_tool import CodeTool
    print("[OK] CodeTool імпортовано успішно")
    print(f"Тип CodeTool: {type(CodeTool)}")
except Exception as e:
    print(f"[Помилка] Помилка імпорту CodeTool: {e}")

try:
    import tools.code_tool
    print("[OK] Модуль tools.code_tool імпортовано успішно")
    print(f"Атрибути модуля: {dir(tools.code_tool)}")
    if hasattr(tools.code_tool, 'CodeTool'):
        print("[OK] Атрибут CodeTool знайдено")
        code_tool = tools.code_tool.CodeTool
        print(f"Тип code_tool: {type(code_tool)}")
    else:
        print("[Помилка] Атрибут CodeTool не знайдено")
except Exception as e:
    print(f"[Помилка] Помилка імпорту модуля tools.code_tool: {e}")

print("Тестування завершено.")