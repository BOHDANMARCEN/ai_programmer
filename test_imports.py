# test_imports.py
import sys
import os

# Встановлюємо кодування UTF-8 для консолі Windows
if sys.platform == "win32":
    os.system("chcp 65001 > nul")

# Додаємо поточну директорію до шляху пошуку модулів
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("Тестування імпортів...")

try:
    from tools.git_tool import GitTool
    print("[OK] GitTool імпортовано успішно")
except Exception as e:
    print(f"[Помилка] Помилка імпорту GitTool: {e}")

try:
    from tools.code_tool import CodeTool
    print("[OK] CodeTool імпортовано успішно")
except Exception as e:
    print(f"[Помилка] Помилка імпорту CodeTool: {e}")

try:
    from tools.web_search_tool import WebSearchTool
    print("[OK] WebSearchTool імпортовано успішно")
except Exception as e:
    print(f"[Помилка] Помилка імпорту WebSearchTool: {e}")

print("Тестування завершено.")