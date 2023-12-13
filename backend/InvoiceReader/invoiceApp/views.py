
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UploadedFile
from ml_app.models import Invoice
from ml_app.serializers import InvoiceSerializer

from .serializers import UploadedFileSerializer

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ml_app.views import query_invoice_image



class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = UploadedFileSerializer(data=request.data)
        if file_serializer.is_valid():
            uploaded_file_instance = file_serializer.save()
            print(uploaded_file_instance.file.path)  # Access the file path here
            query_invoice_image(uploaded_file_instance.file.path)  # Use the correct attribute
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def invoice_list(request):
    if request.method == 'GET':   
        queryset = Invoice.objects.all()
        serializer = InvoiceSerializer(queryset, many=True, context={'requst':request})
        print(serializer.data)
        return Response(serializer.data)
    