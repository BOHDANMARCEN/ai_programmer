# test_executor.py
import os
import sys
import json
from dotenv import load_dotenv
from core.planner import TaskPlanner
from core.executor import TaskExecutor
from memory.agent_memory import AgentMemory
import openai
import os as os_env

def load_config(config_path="config.json"):
    """Завантажує конфігурацію з файлу."""
    with open(config_path, 'r') as f:
        return json.load(f)

def main():
    # Встановлюємо кодування UTF-8 для консолі Windows
    if sys.platform == "win32":
        os.system("chcp 65001 > nul")
    
    # Завантаження змінних оточення
    load_dotenv()
    
    # Завантаження конфігурації
    config = load_config()
    
    # Ініціалізація LLM клієнта
    llm_config = config["llm"]
    llm_client = openai.OpenAI(
        base_url=llm_config["base_url"],
        api_key=os_env.getenv(llm_config["api_key_env_var"])
    )
    llm_client.model = llm_config["model"]
    
    # Створення планувальника та виконавця
    planner = TaskPlanner(config)
    # Створення пам'яті для виконавця
    memory = AgentMemory(config["memory"]["file_path"])
    executor = TaskExecutor(config, llm_client, memory)
    
    # Тестові завдання
    test_tasks = [
        "Клонуй репозиторій https://github.com/user/repo.git до ./my_folder",
        "Проаналізуй код у app.py",
        "Створи скрипт Python для сортування списку"
    ]
    
    for task in test_tasks:
        print(f"\n[Завдання]: {task}")
        
        # Створення плану
        plan = planner.plan(task)
        print(f"[План]: {json.dumps(plan, ensure_ascii=False, indent=2)}")
        
        # Виконання плану
        print("\n[Виконання]:")
        result = executor.execute(plan)
        # Обробляємо можливі проблеми з кодуванням
        try:
            print(result)
        except UnicodeEncodeError:
            # Якщо виникає помилка кодування, виводимо результат без спеціальних символів
            clean_result = result.encode('ascii', 'ignore').decode('unicode_escape')
            print(clean_result)
        except Exception as e:
            print(f"Помилка виведення: {e}")

if __name__ == "__main__":
    main()