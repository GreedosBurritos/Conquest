from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import User, GamePiece
from mongoengine.errors import NotUniqueError
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from django.shortcuts import render

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        try:
            user = User(
                username=data['username'],
                email=data['email'],
                password=make_password(data['password'])
            )
            user.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        except NotUniqueError:
            return Response({'error': 'Username or email already exists'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        try:
            user = User.objects.get(username=data['username'])
            if check_password(data['password'], user.password):
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class GamePieceListView(APIView):
    def get(self, request):
        pieces = GamePiece.objects.all()
        return Response([
            {'id': str(piece.id), 'name': piece.name, 'movement': piece.movement}
            for piece in pieces
        ])
    def post(self, request):
        data = request.data
        try:
            piece = GamePiece(name=data['name'], movement=data['movement'])
            piece.save()
            return Response({'message': 'Game piece created'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return HttpResponse("<h1>Welcome to the Conquest API</h1><p>Try the <a href='/api/register/'>Register</a>, <a href='/api/login/'>Login</a>, or <a href='/api/gamepieces/'>Game Pieces</a> endpoints.</p>")

def login_page(request):
    return render(request, 'login.html')
