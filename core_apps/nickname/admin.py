from django.contrib import admin

from . import models


class NicknameAdmin(admin.ModelAdmin):
    list_display = ["player", "nickname", "club"]
    list_display_links = ["player","nickname"]


admin.site.register(models.Nickname, NicknameAdmin)
