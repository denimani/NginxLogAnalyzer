import json

from rest_framework import status
from rest_framework.test import APITestCase

from logparser.models import LogEntry


class LogEntryTestCase(APITestCase):

    def setUp(self):
        self.log_entry = LogEntry.objects.create(
                                time='2015-05-17 11:05:32+03',
                                remote_ip='127.0.0.1',
                                http_method='GET',
                                url='http://localhost:8000/',
                                response=200,
                                bytes=0,
                                referrer='-',
                                agent='Debian APT-HTTP/1.3 (1.0.1ubuntu2)',
        )

    def test_create_log_entry(self):
        """
        Тестирование создания записи
        """
        data = {
            'time': '2015-05-17 11:05:32+03',
            'remote_ip': '127.0.0.1',
            'http_method': 'GET',
            'url': 'http://localhost:8000/',
            'response': 200,
            'bytes': 0,
            'referrer': '-',
            'agent': 'Debian APT-HTTP/1.3 (1.0.1ubuntu2)',
        }
        response = self.client.post(
            '/api/logs/',
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_log_entries(self):
        """
        Тестирование получения списка записей
        """
        response = self.client.get(
            '/api/logs/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_log_entry(self):
        """
        Тестирование обновления записи
        """
        data = {
            'time': '2024-05-17 11:05:32+03',
            'remote_ip': '127.0.0.1',
            'http_method': 'GET',
            'url': 'http://localhost:9999/',
            'response': 404,
            'bytes': 0,
            'referrer': '-',
            'agent': 'Debian APT-HTTP/1.3 (1.0.1ubuntu2)',
        }
        response = self.client.put(
            f'/api/logs/{self.log_entry.id}/',
            data=json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_log_entry(self):
        """
        Тестирование удаления записи
        """
        response = self.client.delete(
            f'/api/logs/{self.log_entry.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
