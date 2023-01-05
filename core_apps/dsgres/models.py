from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model

from core_apps.nickname.models import Nickname

User = get_user_model()

class Results(models.Model):
    club = models.CharField(verbose_name=_("Club"), max_length=100)
    player = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("user"), related_name="nickname3", default=2   # this has to be change on production
    )
    
    player_nickname = models.ForeignKey(Nickname,on_delete=models.CASCADE, verbose_name=_("Player Nickname"), related_name="nickname2", blank=True, null=True)
    nickname = models.CharField(verbose_name=_("Nickname"), max_length=100)
    agents = models.CharField(verbose_name=_("Agent"), max_length=100)
    profit_loss = models.DecimalField(verbose_name=_("PROFIT/LOSS"),max_digits=15, decimal_places=2, null=False, blank=False, default=0.0)
    rake = models.DecimalField(verbose_name=_("Rake"),max_digits=15, decimal_places=2, null=False, blank=False, default=0.0)
    deal = models.DecimalField(verbose_name=_("Affiliate Deal"),max_digits=10, decimal_places=2, null=False, blank=False, default=0.0) 
    rakeback = models.DecimalField(verbose_name=_("Affiliate Rakeback"),max_digits=15, decimal_places=2, null=False, blank=False, default=0.0)
    adjustment = models.DecimalField(verbose_name=_("Affiliate Adjustment"),max_digits=15, decimal_places=2, null=False, blank=False, default=0.0)
    agent_settlement = models.DecimalField(verbose_name=_("Agent Settlement"),max_digits=15, decimal_places=2, null=False, blank=False, default=0.0)
    date = models.CharField(verbose_name=_("Date: mon-sund"), max_length=50) 