from channels.consumer import SyncConsumer

from channels.consumer import AsyncConsumer

class EchoConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event["text"],
        })
# from channels.generic.websocket import WebsocketConsumer
# from asgiref.sync import async_to_sync
# import json

# class MyConsumer(WebsocketConsumer):


#     def connect(self):
#         self.room_name = "test_consumer"
#         self.room_group_name = "test_consumer_group"
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_name , self.room_group_name
#         )
#         self.accept()
#         self.send(text_data= json.dumps({ 'status' : 'connected' }))
        
        

#     def receive(self, text_data=None, bytes_data=None):
#         pass

#     def disconnect(self, close_code):
#         pass
