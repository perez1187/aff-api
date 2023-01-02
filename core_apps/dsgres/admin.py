from django.contrib import admin

from . import models


class ResultsAdmin(admin.ModelAdmin):
    list_display = ["club", "nickname", "agents", "profit_loss", "rake","deal","rakeback","adjustment","agent_settlement","date"]
    list_display_links = ["nickname"]


admin.site.register(models.Results, ResultsAdmin)
