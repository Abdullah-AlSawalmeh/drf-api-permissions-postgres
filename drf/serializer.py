from rest_framework import serializers

from .models import Projects

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'body', 'author')
        model = Projects