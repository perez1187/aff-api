from rest_framework import serializers

from .models import Results

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    
class SaveFileSerializer(serializers.Serializer):
    
    class Meta:
        model = Results
        fields = "__all__"


class ResultSerializer(serializers.ModelSerializer):
    
    player_nickname = serializers.ReadOnlyField(source="player_nickname.player.username")

    class Meta:
        model = Results
        fields = "__all__"

# get player results
# # later add restriction (only 'owner' or admin)        