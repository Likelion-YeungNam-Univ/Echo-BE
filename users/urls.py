from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view()),
    path('/kakao/callback', kakaoCallBackView.as_view()),
    path('kakao/', KakaoView.as_view()),
]