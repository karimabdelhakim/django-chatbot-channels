from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatMessage,BotMsgToAll
from itertools import chain
from operator import attrgetter


@login_required
def index(request):
    
    #user and bot messages sent to the specific user
    chat_msgs_qs = ChatMessage.objects.filter(user=request.user).order_by('timestamp')
    #bot messages sent to all existing users
    bot_msgs_qs = BotMsgToAll.objects.order_by('timestamp')
    #joining the two list querysets into one sorted list queryset.
	#sorted by timestamp, can be sorted by -timestamp if 
	#reverse=True argument is added after key like in the api view
    result_list = sorted(chain(chat_msgs_qs,bot_msgs_qs),key=attrgetter('timestamp'))
    
    return render(request, "index.html", {
        "messages": result_list,
    })
