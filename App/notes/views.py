from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import NoteSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    parser_classes = [MultiPartParser, FormParser]

    serializer = NoteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

