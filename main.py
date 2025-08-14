# main.py
import os
import json
import argparse
from dotenv import load_dotenv
from core.agent import AIAgent

def load_config(config_path=\"config.json\"):
    \"\"\"Завантажує конфігурацію з файлу.\"\"\"
    with open(config_path, 'r') as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description=\"AI Programmer - автономний ШІ-програміст\")
    parser.add_argument('--config', type=str, default=\"config.json\", help='Шлях до файлу конфігурації')
    args = parser.parse_args()

    # Завантаження змінних оточення
    load_dotenv()
    
    # Завантаження конфігурації
    config = load_config(args.config)

    # Створення агента
    print(\" Запуск AI Programmer...\")
    agent = AIAgent(config)

    print(\" Введіть 'exit' для виходу або 'help' для перегляду команд.\")
    try:
        while True:
            user_input = input(\"\n‍ Введіть завдання: \").strip()
            if not user_input:
                continue
            if user_input.lower() in ['exit', 'quit']:
                break
            if user_input.lower() == 'help':
                print('''
Доступні команди:
- Клонуй репозиторій https://github.com/user/repo.git   до ./my_folder
- Проаналізуй код у app.py
- Створи скрипт Python для сортування списку
- Знайди інформацію про Flask
- exit - вихід
                ''')
                continue

            # Запуск агента
            response = agent.run(user_input)
            print(f\"\n Відповідь агента:\n{response}\")

    except KeyboardInterrupt:
        print(\"\n Вихід (Ctrl-C).\")
    finally:
        agent.close()
        print(\"\n До побачення! Ваші сесії збережено.\")

if __name__ == \"__main__\":
    main()