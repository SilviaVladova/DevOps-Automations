#!/usr/bin/env python3
import subprocess

def get_disk_usage():
    # Изпълнява системната команда 'df -h /' за проверка на дисковото пространство
    result = subprocess.run(['df', '-h', '/'], capture_output=True, text=True)
    
    # Обработка на изхода (парсване на текста)
    lines = result.stdout.split('\n')
    usage_line = lines[1]
    percent = usage_line.split()[4]
    
    return percent

if __name__ == "__main__":
    print(f"Текущо натоварване на диска: {get_disk_usage()}")
