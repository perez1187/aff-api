from rest_framework import generics,permissions,filters

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import NicknameSerializer
from .models import Nickname
from .filters import NincknameFilter



class NicknameListsAPIView(generics.ListAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]
    serializer_class = NicknameSerializer
    queryset = Nickname.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter,filters.SearchFilter]    
    filterset_class = NincknameFilter
