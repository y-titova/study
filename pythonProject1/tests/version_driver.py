from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()
print("Путь к драйверу:", driver_path)

# Получаем версию ChromeDriver
import subprocess

result = subprocess.run([driver_path, "--version"], capture_output=True, text=True)
print("Версия ChromeDriver:", result.stdout.strip())