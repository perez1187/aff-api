# from django.shortcuts import render
# from rest_framework import generics
# import io, csv, pandas as pd
# from rest_framework.response import Response
# from rest_framework import status, generics, filters, permissions

# from .models import User


# class ResultsListsAPIView(generics.ListAPIView):
#     permission_classes = [
#         permissions.IsAdminUser,
#     ]
    
#     serializer_class = ResultSerializer
#     queryset = User.objects.all()
