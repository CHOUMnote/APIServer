from django.urls import path
from .views import Test, CreateScore, GetScore

urlpatterns = [
    path('scoretest/', Test.as_view()),
    path('createscore/', CreateScore.as_view()),
    path('getscores/', GetScore.as_view()),
]
