from rest_framework import serializers

from .models import Results

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    
class SaveFileSerializer(serializers.Serializer):
    
    class Meta:
        model = Results
        fields = "__all__"