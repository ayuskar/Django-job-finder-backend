from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from .models import Profile
from jobs.serializers import JobSerializer, ProfileSerializer, JobApplicationSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework import filters 


@api_view(['POST'])
@permission_classes([AllowAny])  #Allowing access for postman
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=400)
    user = User.objects.create_user(username=username, password=password)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})

@api_view(['GET', 'POST'])
def manageprofile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        profile.name = request.data.get('name', profile.name)
        profile.skills = request.data.get('skills', profile.skills)
        profile.experience = request.data.get('experience', profile.experience)
        profile.save()
        return Response({'message': 'Profile updated!'})
    return Response({
        'name': profile.name,
        'skills': profile.skills,
        'experience': profile.experience
    })