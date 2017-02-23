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

#for testing jwt 
def index_api(request):
    
    messages = ChatMessage.objects.filter(user=request.user).order_by('timestamp')

    # Render that in the index template
    return render(request, "api-index/index.html", {
        "messages": messages,
    })

#list messages of specific user
class UserMessagesListAPIView(ListAPIView):
	#permission_classes = [AllowAny]#default=AllowAny
	permission_classes = [IsAuthenticated]
	serializer_class = UserMessagesSerializer
	#you can use query params like this abc.com/?limit=8&offset=0 
	#means get 8 messages starting from the first message
	pagination_class = LimitOffsetPagination
	def get_queryset(self,*args,**kwargs):
		#if no query pparams used then all messages will return
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

