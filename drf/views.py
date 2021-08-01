from django.db import models
from django.shortcuts import render
from rest_framework import generics

from .models import Projects
from .serializer import ProjectsSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
# from rest_framework.permissions import AllowAny

# Create your views here.
class ProjectsListView(generics.ListCreateAPIView):    
    serializer_class = ProjectsSerializer
    queryset = Projects.objects.all()
    permission_classes = [IsAuthenticated] # permission class changed

class ProjectsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectsSerializer
    queryset = Projects.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)