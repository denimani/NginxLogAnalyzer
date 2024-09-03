from django.db import models

NULLABLE = {'null': True, 'blank': True}

class LogEntry(models.Model):
    time = models.DateTimeField(verbose_name='Время запроса')
    remote_ip = models.CharField(max_length=255, verbose_name='IP адрес')
    remote_user = models.CharField(max_length=255, verbose_name='Имя пользователя', **NULLABLE)
    url = models.CharField(max_length=255, verbose_name='URL')
    http_method = models.CharField(max_length=255, verbose_name='HTTP метод')
    response = models.IntegerField(verbose_name='Код ответа HTTP')
    bytes = models.IntegerField(verbose_name='Размер ответа в байтах')
    referrer = models.CharField(max_length=255, verbose_name='Реферер', **NULLABLE)
    agent = models.CharField(max_length=255, verbose_name='User-Agent', **NULLABLE)

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'

    def __str__(self):
        return f"{self.remote_ip} - {self.http_method} - {self.url}"