# from django.contrib.auth.models import User
# from rest_framework import generics, status
# from rest_framework.response import Response

# from django.shortcuts import redirect

from rest_framework import status
from django.contrib.auth import authenticate, get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import UserSerializer, LoginUserSerializer

User = get_user_model()
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes_by_action = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [AllowAny],
        'update': [IsAuthenticated],
        'destroy': [IsAuthenticated],
    }
    def get_serializer(self, *args, **kwargs):
        if self.action == 'login':
            serializer_class = LoginUserSerializer
        else :
            serializer_class = UserSerializer
        return serializer_class(*args, **kwargs)


    def create(self, request, *args, **kwargs):
        reg_serializer = self.get_serializer(data = request.data) # json -> python
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            res = self.get_serializer(instance = new_user)
            
            return Response({"user": res}, status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=["post"], url_name='login')
    def login(self, request):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        nickname = serializer.validated_data.get("nickname")
        password = serializer.validated_data.get("password")

        if not nickname or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(nickname=nickname, password=password)

        if user:
            token = TokenObtainPairSerializer.get_token(user)
            return Response({
                "access" : str(token.access_token),
                "refresh" : str(token),
                }, status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
