# test_planner.py
import os
import sys
import json
from dotenv import load_dotenv
from core.planner import TaskPlanner

# Встановлюємо кодування UTF-8 для консолі Windows
if sys.platform == "win32":
    os.system("chcp 65001 > nul")

def load_config(config_path="config.json"):
    """Завантажує конфігурацію з файлу."""
    with open(config_path, 'r') as f:
        return json.load(f)

def main():
    # Завантаження змінних оточення
    load_dotenv()
    
    # Завантаження конфігурації
    config = load_config()
    
    # Створення планувальника
    planner = TaskPlanner(config)
    
    # Тестові завдання
    test_tasks = [
        "Клонуй репозиторій https://github.com/user/repo.git до ./my_folder",
        "Проаналізуй код у app.py",
        "Створи скрипт Python для сортування списку",
        "Знайди інформацію про Flask",
        "Як створити веб-додаток на Django?"
    ]
    
    for task in test_tasks:
        print(f"\n[Завдання]: {task}")
        plan = planner.plan(task)
        print(f"[План]: {json.dumps(plan, ensure_ascii=False, indent=2)}")

if __name__ == "__main__":
    main()