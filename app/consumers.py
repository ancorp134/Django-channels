from channels.generic.websocket import WebsocketConsumer

class MyConsumer(WebsocketConsumer):
    groups = ["broadcast"]

    def connect(self):
        # Called on connection.
        # To accept the connection call:
        self.accept()
        # Or accept the connection and specify a chosen subprotocol.
        # A list of subprotocols specified by the connecting client
        # will be available in self.scope['subprotocols']
        self.accept("subprotocol")
        # To reject the connection, call:
        self.close()

    def receive(self, text_data=None, bytes_data=None):
        # Called with either text_data or bytes_data for each frame
        # You can call:
        self.send(text_data="Hello world!")
        # Or, to send a binary frame:
        self.send(bytes_data="Hello world!")
        # Want to force-close the connection? Call:
        self.close()
        # Or add a custom WebSocket error code!
        self.close(code=4123)

    def disconnect(self, close_code):
        pass


# from channels.consumer import SyncConsumer

# from channels.consumer import AsyncConsumer

# class EchoConsumer(AsyncConsumer):

#     async def websocket_connect(self, event):
#         await self.send({
#             "type": "websocket.accept",
#         })

#     async def websocket_receive(self, event):
#         await self.send({
#             "type": "websocket.send",
#             "text": event["text"],
#         })
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
