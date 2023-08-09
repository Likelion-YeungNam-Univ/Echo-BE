from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from .models import Profile

from django.shortcuts import redirect

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key}, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'pk'


class KakaoView(APIView):
    def get(self, request):
        kakao_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"
        redirect_uri = "http://10.58.2.143:8000/users/kakao/callback"
        client_id = "ad3ae8475404821e34a7910b1aeff53d"

        redirect_url = f"{kakao_api}&client_id={client_id}&redirect_uri={redirect_uri}"
        return Response({"redirect_url": redirect_url}, status=status.HTTP_200_OK)

class kakaoCallBackView(APIView):
    def get(self, request):
        data = {
            "grant_type" : "authorization_code",
            "client_id" : "ad3ae8475404821e34a7910b1aeff53d",
            "redirection_uri" : "http://10.58.2.143:8000/users/kakao",
            "code" : request.GET.get("code")
        }

        kakao_token_api = "https:kauth.kakao.com/oauth/token"
        response = requests.post(kakao_token_api, data=data)
        access_token = response.json().get("access_token")
        
        kakao_user_api = "https://kapi.kakao.com/v2/user/me"
        header = {"Authorization":f"Bearer ${access_token}"}
        user_infomation = requests.get(kakao_user_api, headers=header).json()
        
        return Response({"access_token": access_token})
    
    
                                                            
