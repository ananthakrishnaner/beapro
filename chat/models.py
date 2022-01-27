from django.db import models
from accounts.models import Account


# Create your models here.
class PrivateChatRoom(models.Model):

	user1 = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="user1")
	user2 = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="user2")
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return f"A Chat Between {user1} and {user2}."


	@property
	def group_name(self):
		return f"PrivateChatRoom-{self.id}"


class RoomChatMessagesManager(models.Manager):
	def by_room(self,room):
		qs = RoomChatMessages.objects.filter(room=room).order_by("-timestamp")
		return qs


class RoomChatMessages(models.Model):
	user = models.ForeignKey(Account,on_delete=models.CASCADE)
	room = models.ForeignKey(PrivateChatRoom,on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)
	content = models.TextField(unique =False,blank=True)

	objects = RoomChatMessagesManager()

	def __str__(self):
		return self.content
	