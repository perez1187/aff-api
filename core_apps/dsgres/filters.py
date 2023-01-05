import django_filters as filters

from core_apps.dsgres.models import Results

class ResultFilter(filters.FilterSet):
    player_nickname = filters.CharFilter (field_name="player_nickname__player__username",lookup_expr="iexact")
    nickname = filters.CharFilter (field_name="nickname",lookup_expr="iexact")
    date = filters.CharFilter (field_name="date",lookup_expr="iexact")

    class Meta:
        model = Results
        fields = ["player_nickname","nickname","date"]