"""
Przechowuje wszytskie odnośniki endpointów dla konkretnych aplikacji.
Ścieżka authx/ pobiera wszystkie endpointy dla aplikacji authx.
"""

from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('authx/', include('authx.urls')),
]
