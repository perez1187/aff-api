from django.db import models
from django.utils.translation import gettext_lazy as _

class Results(models.Model):
    club = models.CharField(verbose_name=_("Club"), max_length=100)
    nickname = models.CharField(verbose_name=_("Nickname"), max_length=100)
    agents = models.CharField(verbose_name=_("Agent"), max_length=100)
    profit_loss = models.DecimalField(verbose_name=_("PROFIT/LOSS"),max_digits=100, decimal_places=50, null=False, blank=False, default=0.0)
    rake = models.DecimalField(verbose_name=_("Rake"),max_digits=100, decimal_places=50, null=False, blank=False, default=0.0)
    deal = models.DecimalField(verbose_name=_("Affiliate Deal"),max_digits=10, decimal_places=5, null=False, blank=False, default=0.0) 
    rakeback = models.DecimalField(verbose_name=_("Affiliate Rakeback"),max_digits=100, decimal_places=50, null=False, blank=False, default=0.0)
    adjustment = models.DecimalField(verbose_name=_("Affiliate Adjustment"),max_digits=100, decimal_places=50, null=False, blank=False, default=0.0)
    agent_settlement = models.DecimalField(verbose_name=_("Agent Settlement"),max_digits=100, decimal_places=50, null=False, blank=False, default=0.0)
    date = models.CharField(verbose_name=_("Date: mon-sund"), max_length=50) 