from channels.generic.websocket import AsyncWebsocketConsumer
from .models import GroupMessage, ChatGroup
from django.contrib.auth.models import User
from channels.db import database_sync_to_async
import sys
import json
import shortuuid
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

class ChatroomConsumer(AsyncWebsocketConsumer):

	user_online: dict[dict] = {}

	async def connect(self):
		self.chatroom_name: str = self.scope['url_route']['kwargs']['chatroom_name']
		self.user: User = self.scope['user']
		self.uuid = shortuuid.uuid()
		await self.accept()

		self.group: ChatGroup = await self.create_group_if_not_exist()

		# keep user_online
		if self.user_online.get(self.chatroom_name) is None:
			self.user_online[self.chatroom_name] = {}
		self.user_online[self.chatroom_name][self.uuid] = self.user.username

		print (f'{RED}{self.user_online}{RESET}', file=sys.stderr)
		await self.channel_layer.group_add(self.chatroom_name, self.channel_name)
		# send message to user has join to group
		event = {
			'type': 'new_connection',
			'user': self.user.username
		}
		await self.channel_layer.group_send(self.chatroom_name, event)
		
		# send existing message to self
		msg = await self.get_messages()
		first_value = {
			'type': 'connect',
			'messages': msg,
			'users': list(set(self.user_online[self.chatroom_name].values()))
		}
		await self.send(text_data=json.dumps(first_value))

		print(f"{GREEN}{self.user} connected on channel {self.chatroom_name}{RESET}", file=sys.stderr)

	async def disconnect(self, close_code):
		del self.user_online[self.chatroom_name][self.uuid]

		# if last connection send message left channel
		if self.user_online[self.chatroom_name].get(self.user.username) is None:
			print(f"{RED}{self.user.username} is last in {self.chatroom_name}{RESET}", file=sys.stderr)
			event = {
				'type': 'disconnection',
				'user': self.user.username
			}
			await self.channel_layer.group_send(self.chatroom_name, event)

		await self.channel_layer.group_discard(self.chatroom_name, self.channel_name)
		print(f"{RED}{self.user.username} disconnected {self.chatroom_name}{RESET}", file=sys.stderr)
	
	async def new_connection(self, event):
		await self.send(text_data=json.dumps(event))

	async def disconnection(self, event):
		await self.send(text_data=json.dumps(event))

	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		# print(f'{GREEN}{text_data_json}{RESET}', file=sys.stderr)	
		await self.message_save(text_data_json['body'])

		event = {
			'type': 'message_handler',
			'body': text_data_json['body'],
			'author': self.user.username
		}
		await self.channel_layer.group_send(self.chatroom_name, event)

	async def message_handler(self, event):
		await self.send(text_data=json.dumps(event))

####################### database #####################################

	@database_sync_to_async
	def message_save(self, body:str):
		GroupMessage.objects.create(
			group=self.group, 
			author=self.user,
			body=body)

	@database_sync_to_async	
	def create_group_if_not_exist(self):
		group = ChatGroup.objects.filter(name=self.chatroom_name).first()
		if group is None:
			group = ChatGroup.objects.create(name=self.chatroom_name)
		return group

	@database_sync_to_async
	def get_messages(self):
		messages = list(GroupMessage.objects.filter(group=self.group)[:10])
		msg = []
		for message in messages:
			msg.append({
				'type': 'message_handler',
				'body': message.body,
				'author': message.author.username
			})
		return msg
	