from django.db import models
from django.utils.translation import gettext_lazy as _

from django.contrib.auth import get_user_model
from core_apps.nickname.models import Nickname 

User = get_user_model()

class Settlement(models.Model):
    class CurrencyType(models.TextChoices):
        USD = "USD", _("USD")
        EUR = "EUR", _("EUR")
        PLN = "PLN", _("PLN")
        BRL = "BRL", _("BRL")
        ILS = "ILS", _("ILS")

    player = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("user"), default=2   # this has to be change on production
    )
    nickname = models.ForeignKey(
        Nickname, on_delete=models.CASCADE, verbose_name=_("nickname"), blank=True, null=True,help_text = "optional"
    )
    club = models.CharField(verbose_name=_("Club"), max_length=100, blank=True, null=True,help_text = "optional")
    date = models.CharField(verbose_name=_("Date"), max_length=100, help_text = "transaction date dd/mm/yy")
    transactionValue = models.DecimalField(verbose_name=_("Transaction Value"),max_digits=14, decimal_places=2, null=False, blank=False, default=0.00,help_text = "transaction value (original currency)")
    currency = models.CharField(
        verbose_name=_("Currency"),
        max_length=50,
        choices=CurrencyType.choices,
        default=CurrencyType.USD,
        help_text = "orginal currency"
    )
    transactionUSD = models.DecimalField(verbose_name=_("Transaction in USD"),max_digits=14, decimal_places=2, null=False, blank=False, default=0.00,help_text = "transaction in USD")
    exchangeRate = models.DecimalField(verbose_name=_("Exchange Rate"),max_digits=14, decimal_places=2, null=False, blank=False, default=1.00,help_text = "exchange rate to the USD, leave 1.00 if orginal value in USD")
    description = models.CharField(verbose_name=_("Description"), max_length=1000, blank=True, null=True,help_text = "optional")
