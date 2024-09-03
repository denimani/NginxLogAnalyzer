from rest_framework.routers import DefaultRouter

from logparser.apps import LogparserConfig
from logparser.views import LogEntryViewSet

app_name = LogparserConfig.name

router = DefaultRouter()

router.register(r'logs', viewset=LogEntryViewSet, basename='logs')

urlpatterns = [] + router.urls
