from django.db import models
from django.shortcuts import render
from rest_framework import generics

from .models import Projects
from .serializer import ProjectsSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class ProjectsListView(generics.ListCreateAPIView):    
    serializer_class = ProjectsSerializer
    queryset = Projects.objects.all()

class ProjectsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectsSerializer
    queryset = Projects.objects.all()
    permission_classes = (IsAuthorOrReadOnly,)