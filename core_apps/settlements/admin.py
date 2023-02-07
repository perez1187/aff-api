from django.contrib import admin

from . import models

class SettlementAdmin(admin.ModelAdmin):
    list_display = ["player","date", "transactionValue","currency","transactionUSD","exchangeRate","description"]
    list_display_links = ["player"]
    list_filter = ["player"]

admin.site.register(models.Settlement, SettlementAdmin)