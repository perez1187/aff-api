from django.urls import path
from .views import NicknameListsAPIView

urlpatterns = [
    path('all/', NicknameListsAPIView.as_view(), name='upload-file'),
]