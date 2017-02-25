from django.shortcuts import render
from chat.models import ChatMessage
from .serializers import UserMessagesSerializer
from rest_framework.generics import (ListAPIView, RetrieveAPIView,
	UpdateAPIView,DestroyAPIView,CreateAPIView,RetrieveUpdateAPIView)
from rest_framework.filters import ( SearchFilter, OrderingFilter)
from rest_framework.permissions import (AllowAny,IsAuthenticated,
	IsAdminUser,IsAuthenticatedOrReadOnly)
#from .permissions import IsOwnerOrReadOnly,IsOwner
from rest_framework.pagination import (LimitOffsetPagination)
from .pagination import MessagesPageNumberPagination
from rest_framework.decorators import api_view


#for testing chating with jwt authentication 
def index_api(request):#add /?token=token to the url and then chat
    return render(request, "api-index/index.html")


#list messages of specific user
class UserMessagesListAPIView(ListAPIView):
	#permission_classes = [AllowAny]#default=AllowAny
	permission_classes = [IsAuthenticated]
	serializer_class = UserMessagesSerializer
	#you can use query params like this abc.com/?limit=8&offset=0 
	#means get 8 messages starting from the first message
	pagination_class = LimitOffsetPagination
	def get_queryset(self,*args,**kwargs):
		#if no query params used then all messages will return
		queryset_list = ChatMessage.objects.filter(user=self.request.user).order_by('-timestamp')
		
		return queryset_list

#list all messages
class MessagesListAPIView(ListAPIView):
	queryset = ChatMessage.objects.all()
	#permission_classes = [AllowAny]#default=AllowAny
	permission_classes = [IsAdminUser] #only admin can.
	serializer_class = UserMessagesSerializer
	filter_backends = [SearchFilter,OrderingFilter]
	search_fields = ['user__email','user__username','user__last_name','owner','timestamp']
	pagination_class = MessagesPageNumberPagination

