FROM python:3.10-slim

# установка netcat
RUN apt-get update && apt-get install -y netcat-openbsd

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# копирование исходного кода проекта
COPY . .

# добавление и установка прав на выполнение скрипта entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# установка точки входа
ENTRYPOINT ["/app/entrypoint.sh"]
