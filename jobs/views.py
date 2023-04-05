from django.shortcuts import render
from .serializers import Jobserializer
from .models import Job
from rest_framework import generics
# Create your views here.


class Joblist(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = Jobserializer
