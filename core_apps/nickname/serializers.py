from rest_framework import serializers

from .models import Nickname

class NicknameSerializer(serializers.ModelSerializer):

    # player_info = serializers.SerializerMethodField(read_only=True)
    player= serializers.ReadOnlyField(source="player.username")


    # def get_player_info(self, obj):
    #     return {
    #         "username": obj.player.username,
    #         # "fullname": obj.author.get_full_name,
    #         # "about_me": obj.author.profile.about_me,
    #         # "profile_photo": obj.author.profile.profile_photo.url,
    #         # "email": obj.author.email,
    #         # "twitter_handle": obj.author.profile.twitter_handle,
    #     }

    class Meta:
        model = Nickname
        fields = "__all__"