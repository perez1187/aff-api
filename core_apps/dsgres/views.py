'''
    article:
        https://baronchibuike.medium.com/how-to-read-csv-file-and-save-the-content-to-the-database-in-django-rest-256c254ef722
'''

from django.shortcuts import render
from rest_framework import generics
import io, csv, pandas as pd
from rest_framework.response import Response
from rest_framework import status

from .models import Results
from .serializers import FileUploadSerializer, SaveFileSerializer

class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = Results(
                       club=row["CLUB"],
                       nickname=row["NICKNAME"],
                       agents=row["AGENTS"],
                       profit_loss=row["PROFIT/LOSS"],
                       rake=row["RAKE"],
                       deal=row[" DEAL"],
                    #    deal=row["DEAL"],
                       rakeback=row["RAKEBACK"],
                       adjustment=row["ADJUSTMENT"],
                       agent_settlement=row["AGENT SETTLEMENT"],
                       date=row["DATE"],
                       )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)




'''
    commont mistakes:
        https://betterprogramming.pub/3-techniques-for-importing-large-csv-files-into-a-django-app-2b6e5e47dba0

    Another option:
'''


# import codecs
# import csv

# from django.core.files.base import ContentFile
# from django.core.files.storage import FileSystemStorage

# from rest_framework import serializers, viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response

# from .models import Results


# fs = FileSystemStorage(location='tmp/')

# # Serializer
# class ResultsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Results
#         fields = "__all__"

# # Viewset
# class ProductViewSet(viewsets.ModelViewSet):
#     """
#     A simple ViewSet for viewing and editing Product.
#     """
#     queryset = Results.objects.all()
#     serializer_class = ResultsSerializer        

#     @action(detail=False, methods=['POST'])
#     def upload_data_with_validation(self, request):
#         """Upload data from CSV, with validation."""
#         file = request.FILES.get("file")

#         reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
#         data = list(reader)

#         serializer = self.serializer_class(data=data, many=True)
#         serializer.is_valid(raise_exception=True)

#         product_list = []
#         for row in serializer.data:
#             product_list.append(
#                 Results(
#                     club=row["CLUB"],
#                     nickname=row["NICKNAME"],
#                     agent=row["PROFIT/LOSS"],
#                     date=row["DATE"],
#                 )
#             )

#         Results.objects.bulk_create(product_list)

#         return Response("Successfully upload the data")