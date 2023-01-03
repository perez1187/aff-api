from rest_framework import status, generics

from .serializers import NicknameSerializer
from .models import Nickname



class NicknameListsAPIView(generics.ListAPIView):
    serializer_class = NicknameSerializer
    queryset = Nickname.objects.all()
