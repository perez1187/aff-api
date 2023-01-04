from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model


User = get_user_model()

class Nickname(models.Model):
    
    player = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("user"), related_name="nickname2", default=5   # this has to be change on production
    )
    nickname = models.CharField(verbose_name=_("Nickname"), max_length=100)
    club = models.CharField(verbose_name=_("Club"), max_length=100)
    player_rb = models.DecimalField(verbose_name=_("Player Rakeback"),max_digits=10, decimal_places=3, null=False, blank=False, default=0.0)
    player_adjustment = models.DecimalField(verbose_name=_("Player Adjustment"),max_digits=10, decimal_places=2, null=False, blank=False, default=0.0)

    def __str__(self):
        return f"{self.player.username}"

    class Meta:
        unique_together = ["nickname", "club"]


# nickname and club unique together

'''
w dsg res nie ddoajmey playera bo po chuj, tylko sprawdzamy czy istnieje nick+ club, jesli nie, to tworzymy nowy jako niezarejestrowany
albo dodjamey z dodatkowym polem confirm, jesli nick zarejestrowany, true, jesli niezarejstrowany false 
i wtedy w dwoch miejscach trzeba dodac
zarejestrowac w nicknames, i recznie zmienic drgres
'''

# czyli w dsgres dodamy nickname/player foreign key do nickanme

'''
```
from rest_framework import serializers

from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    rated_by = serializers.SerializerMethodField(read_only=True)
    article = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        fields = ["id", "article", "rated_by", "value"]

    def get_rated_by(self, obj):
        return obj.rated_by.username

    def get_article(self, obj):
        return obj.article.title
```
lets go to models, and because articles and rated_by are foreign keys to other models we target model atribiutes of this field

so here obj is Rating models
that is why we can use username. So obj (Rating) rated by (feilds) username (because rated by is foreign key to User)

'''