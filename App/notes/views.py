from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Note
from .serializers import NoteSerializer


@api_view("POST")
def api_view(request, *args, **kwargs):
    parser_classes = [MultiPartParser, FormParser]

    serializer = NoteSerializer(request.data)
    data = serializer.data

    if serializer.is_valid():
        serializer.save()
        return Response(data,status=status.HTTP_201_CREATED)
    return Response(data,status=status.HTTP_201_CREATED)

