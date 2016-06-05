from django.conf.urls import url, include
from django.contrib import admin

from login import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login/', include('login.urls')),
]
