from django.urls import path, include

from backend_config import settings

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),

]
