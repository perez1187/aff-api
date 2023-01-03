from rest_framework import status, generics,permissions

from .serializers import NicknameSerializer
from .models import Nickname



class NicknameListsAPIView(generics.ListAPIView):
    permission_classes = [
        permissions.IsAdminUser,
    ]
    serializer_class = NicknameSerializer
    queryset = Nickname.objects.all()
