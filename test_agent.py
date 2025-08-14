# test_agent.py
import os
import sys
import json
from dotenv import load_dotenv
from core.agent import AIAgent

def load_config(config_path="config.json"):
    """Завантажує конфігурацію з файлу."""
    with open(config_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    # Встановлюємо кодування UTF-8 для консолі Windows
    if sys.platform == "win32":
        os.system("chcp 65001 > nul")
    
    # Завантаження змінних оточення
    load_dotenv()
    
    # Завантаження конфігурації
    config = load_config()
    
    # Створення агента
    agent = AIAgent(config)
    
    # Тестові завдання
    test_tasks = [
        "Проаналізуй код у app.py",
        "Створи скрипт Python для сортування списку"
    ]
    
    for task in test_tasks:
        print(f"\n[Завдання]: {task}")
        
        # Виконання завдання
        print("\n[Відповідь агента]:")
        result = agent.run(task)
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