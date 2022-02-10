from django.urls import re_path
from django.contrib import admin

from .views import (
    FacebookWebhookView
    )

app_name ='bot_webhooks'
urlpatterns = [
    re_path(r'^c63e313b2235ac8744df7b1f4a2a66100a383c964b0d40a8723a82ba410b/$', FacebookWebhookView.as_view(), name='webhook'),
]