"""
ASGI config for WebStoreHouse project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
# from WebStoreHouse import routing  # Импортируйте routing из вашего приложения


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebStoreHouse.settings')

application = get_asgi_application()


# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             routing.websocket_urlpatterns  # Используйте маршруты WebSocket
#         )
#     ),
# })
