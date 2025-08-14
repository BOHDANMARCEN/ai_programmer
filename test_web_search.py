# test_web_search.py
import os
import sys
import json
from dotenv import load_dotenv
from tools.web_search_tool import WebSearchTool

def main():
    # Встановлюємо кодування UTF-8 для консолі Windows
    if sys.platform == "win32":
        os.system("chcp 65001 > nul")
    
    # Завантаження змінних оточення
    load_dotenv()
    
    # Тестові запити
    test_queries = [
        "Python best practices",
        "Flask tutorial",
        "Django deployment"
    ]
    
    for query in test_queries:
        print(f"\n[Пошук]: {query}")
        
        # Виконання пошуку
        result = WebSearchTool.search(query)
        print(result)

if __name__ == "__main__":
    main()