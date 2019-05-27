from django.contrib.auth.models import User
from rest_framework.response import Response
from login.serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, login


class UserRegistrationView(CreateAPIView):

    model = User
    serializer_class = UserRegistrationSerializer


class UserLoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        if username and password:
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return Response({'success': "login success"})
        else:
            return Response({'Fail': 'wrong credentials'})
