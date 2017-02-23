from django.conf.urls import url
from .views import (UserMessagesListAPIView,MessagesListAPIView)

urlpatterns = [
   
	url(r'^messages/$', UserMessagesListAPIView.as_view(),name='list'),
	url(r'^messages/all$', MessagesListAPIView.as_view(),name='list-all'),
]