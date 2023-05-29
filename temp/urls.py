from django.urls import path
from .views import Test, CreateMSG, GetMessages, SyncMessage

urlpatterns = [
    path('test/', Test.as_view()),
    
    path('create_msg/', CreateMSG.as_view()),
    path('messages/', GetMessages.as_view()),
    path('syncmessage/', SyncMessage.as_view()),
]
