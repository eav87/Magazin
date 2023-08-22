# Используйте официальный образ Python
FROM python:3.10-slim

# Установите рабочую директорию в контейнере
WORKDIR /app

# Установите зависимости проекта
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте содержимое локальной директории в контейнер
COPY . .

# Запустите приложение
CMD ["gunicorn", "magazin.wsgi:application", "--bind", "0.0.0.0:8000"]
