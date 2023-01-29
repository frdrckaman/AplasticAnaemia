from django.conf import settings
from django.contrib import admin
from django.urls import path

admin.site.site_header = settings.APP_NAME

app_name = "nimr_web"

urlpatterns = [
    path('', admin.site.urls),
]