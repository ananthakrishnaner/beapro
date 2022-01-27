from django.shortcuts import render,redirect
from accounts.models import Account
from django.urls import reverse
from urllib.parse import urlencode
from django.http import HttpResponse
from django.conf import settings
from itertools import chain
from .models import PrivateChatRoom,RoomChatMessages
# Create your views here.

DEBUG = False


def private_chat_room_view(request, *args,**kwargs):
	user = request.user

	if not user.is_authenticated:
		return redirect('index')

	context = {}

	# 1. Find all the rooms this user is a part of 
	rooms1 = PrivateChatRoom.objects.filter(user1=user, is_active=True)
	rooms2 = PrivateChatRoom.objects.filter(user2=user, is_active=True)

	rooms = list(chain(rooms1, rooms2))

	"""
	m_and_f:
		[{"message": "hey", "friend": "Mitch"}, {"message": "You there?", "friend": "Blake"},]
	Where message = The most recent message
	"""
	m_and_f = [] 
	for room in rooms:
		# Figure out which user is the "other user" (aka friend)
		if room.user1 == user:
			friend = room.user2
		else:
			friend = room.user1
		m_and_f.append({
			'message': "", # blank msg for now (since we have no messages)
			'friend': friend
		})
	context['m_and_f'] = m_and_f
	context['debug'] = DEBUG
	context['debug_mode'] = settings.DEBUG

	return render(request,'chat/room.html',context)