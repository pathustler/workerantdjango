from django.shortcuts import render
from .serializers import Userserializer
from rest_framework import generics
from .models import User
# Create your views here.


class Userslist(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer