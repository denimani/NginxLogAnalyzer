from django.contrib import admin

from logparser.models import LogEntry


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('time', 'remote_ip', 'http_method', 'url', 'response', 'bytes')
    list_filter = ('remote_ip', 'http_method', 'url', 'response')
    search_fields = ('remote_ip', 'http_method', 'url')
