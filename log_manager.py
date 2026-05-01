import os

class LogAnalyzer:
    def __init__(self, filename):
        """Инициализира обекта с пътя до лог файла."""
        self.filename = filename

    def count_errors(self):
        """Брои срещанията на критични думи в лога."""
        if not os.path.exists(self.filename):
            return "Грешка: Файлът не съществува!"
        
        count = 0
        with open(self.filename, 'r') as file:
            for line in file:
                # Проверяваме за ERROR или CRITICAL или WARNING (Case-sensitive)
                if "ERROR" in line or "CRITICAL" in line or "WARNING" in line:
                    count += 1
        return count

    def get_report(self):
        """Генерира кратък репорт за анализа."""
        user = os.getlogin()
        abs_path = os.path.abspath(self.filename)
        return f"--- Report by {user} ---\nFile: {abs_path}\nStatus: Processed"

# Основна част за изпълнение
if __name__ == "__main__":
    analyzer = LogAnalyzer("app.log")
    print(analyzer.get_report())
    print(f"Намерени критични събития: {analyzer.count_errors()}")
