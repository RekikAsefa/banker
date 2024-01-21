from django.urls import path
from .views import create_business_customer, create_swift_application, success , login , landing, chat_view , poll_messages_api , send_message_api ,initiate_chat

urlpatterns = [
    path('',landing,name='landing'),
    path('login/',login,name='login'),
    path('register/', create_business_customer, name='create_business_customer'),
    path('create-swift-application/', create_swift_application, name='create_swift_application'),
    path('status/', success, name='success'),
    path('chat/<int:chat_session_id>/', chat_view, name='chat_view'),
    path('chat/api/messages/<int:chat_session_id>/', poll_messages_api, name='poll_messages_api'),
    path('chat/api/send/<int:chat_session_id>/', send_message_api, name='send_message_api'),
    path('chat/initiate/', initiate_chat, name='initiate_chat'),
]