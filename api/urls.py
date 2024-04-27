from django.contrib import admin
from django.urls import path,include
from .views import EndpointList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('library.urls')),
    path('', EndpointList.as_view(), name='endpoint-list'),
]
