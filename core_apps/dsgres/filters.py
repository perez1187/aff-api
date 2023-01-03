import django_filters as filters

from core_apps.dsgres.models import Results

class ResultFilter(filters.FilterSet):
    player_nickname = filters.CharFilter (field_name="player_nickname__player__username",lookup_expr="iexact")

    class Meta:
        model = Results
        fields = ["player_nickname"]