from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from logparser.models import LogEntry
from logparser.pagination import MyPagination
from logparser.serializers import LogEntrySerializer


class LogEntryViewSet(viewsets.ModelViewSet):
    """
    API эндпоинт для модели LogEntry
    """
    queryset = LogEntry.objects.all() # получаем все записи
    serializer_class = LogEntrySerializer # сериализатор
    pagination_class = MyPagination # пагинация
    filter_backends = [DjangoFilterBackend, SearchFilter] # фильтр
    filterset_fields = ['remote_ip', 'http_method', 'url', 'response'] # поле для фильтрации
    search_fields = ['remote_ip', 'http_method', 'url'] # поле для поиска

