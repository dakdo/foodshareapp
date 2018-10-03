from rest_framework import generics

from . import models
from . import serializers

class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class UserProfileListView(generics.ListCreateAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer

class DetailUserProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer