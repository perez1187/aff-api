import django_filters as filters

from core_apps.nickname.models import Nickname

class NincknameFilter(filters.FilterSet):
    player = filters.CharFilter (field_name="player__username",lookup_expr="iexact")

    class Meta:
        model = Nickname
        fields = ["player"]