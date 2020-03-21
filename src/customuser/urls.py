from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

api_patterns = [
    url(r'^api/v1/', include('users.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
] + api_patterns
