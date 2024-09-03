import json
import os
from datetime import datetime

from django.core.management import BaseCommand

from config import settings
from logparser.models import LogEntry


class Command(BaseCommand):
    help = 'Парсинг Nginx логов и сохранение их в базу данных'

    def add_arguments(self, parser):
        parser.add_argument('log_file', type=str)

    def handle(self, *args, **kwargs):
        # получаем имя файла из аргументов
        log_file = kwargs['log_file']

        # путь к файлу с логами
        file_path = os.path.join(settings.BASE_DIR, log_file)

        try:
            # открываем файл и читаем построчно параллельно сохраняем в БД
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    log_entry = json.loads(line)
                    log = LogEntry(
                        time=datetime.strptime(log_entry['time'], "%d/%b/%Y:%H:%M:%S %z"),
                        remote_ip=log_entry['remote_ip'],
                        remote_user=log_entry['remote_user'],
                        http_method=log_entry['request'].split(' ')[0],
                        url=log_entry['request'].split(' ')[1],
                        response=log_entry['response'],
                        bytes=log_entry['bytes'],
                        referrer=log_entry['referrer'],
                        agent=log_entry['agent'],
                    )
                    log.save()

        # если файл не существует - выводим ошибку
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('Файл не найден'))

        # если невалидные данные - выводим ошибку
        except json.JSONDecodeError as e:
            self.stdout.write(self.style.ERROR(f'Ошибка - {e}'))
