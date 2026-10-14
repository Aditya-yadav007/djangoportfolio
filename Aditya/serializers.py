from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'category',
            'description',
            'image_url',
            'project_url',
            'sort_order',
        )
        read_only_fields = ('id',)
