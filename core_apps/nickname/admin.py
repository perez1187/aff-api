from django.contrib import admin

from . import models


class NicknameAdmin(admin.ModelAdmin):
    list_display = ["player", "nickname", "club","player_rb","player_adjustment"]
    list_display_links = ["player","nickname"]
    list_filter = ["player", "nickname"]


admin.site.register(models.Nickname, NicknameAdmin)
