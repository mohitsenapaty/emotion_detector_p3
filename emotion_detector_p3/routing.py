'''
from channels.routing import route
from test_app.consumers import ws_connect, ws_message, ws_disconnect

channel_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]
'''
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from test_app.consumers import ChatConsumer
from django.urls import path

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path(r"^chat/$", ChatConsumer),
        ])
    ),
})
