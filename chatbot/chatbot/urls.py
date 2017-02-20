from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from chat.views import index
from chat.api.views import index_api

urlpatterns = [
    url(r'^$', index),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^admin/', admin.site.urls),

    url(r'^api/$', index_api),
    url(r'^api/accounts/', include("accounts.api.urls",namespace='users-api')),
]
