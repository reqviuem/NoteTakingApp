import os
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import NoteSerializer

MODELS_DIR = settings.MEDIA_ROOT


@api_view(["POST"])
def save(request, *args, **kwargs):
    method = request.method
    parser_classes = [MultiPartParser, FormParser]
    serializer = NoteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_list(request, *args, **kwargs):
    try:
        files = os.listdir(MODELS_DIR)
        model_files = [f for f in files]
        return Response({"models": model_files})
    except FileNotFoundError:
        return Response(
            status=status.HTTP_404_NOT_FOUND
        )
