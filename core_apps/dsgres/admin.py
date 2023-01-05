from django.contrib import admin

from . import models


class ResultsAdmin(admin.ModelAdmin):
    list_display = ["club","player","player_nickname", "nickname", "agents", "profit_loss", "rake","deal","rakeback","adjustment","agent_settlement","date"]
    list_display_links = ["player","player_nickname","nickname"]
    list_filter = ["player", "nickname","date"]


admin.site.register(models.Results, ResultsAdmin)
