from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import HttpResponse

from .models import User,Creation
from .serializers import UserSerializer,CreationSerializer


def index(request):
    return HttpResponse("Hello world")

class PostUser(APIView):
    serializer_class = UserSerializer


# region POST methods
@api_view(['POST'])
def user_create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# POST creation in server
@api_view(['POST'])
def creation_create(request):
    serializer = CreationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
# endregion


# Get one user By Id.
@api_view(['GET'])
def user_detail(request, pk):
    tasks = User.objects.get(id=pk)
    serializer = UserSerializer(tasks, many=False)
    return Response(serializer.data)

# Get one creation By Id.
@api_view(['GET'])
def creation_detail(request, pk):
    tasks = Creation.objects.get(id=pk)
    serializer = CreationSerializer(tasks, many=False)
    return Response(serializer.data)


# Get All users from server.
@api_view(['GET'])
def user_list(request):
    tasks = User.objects.all().order_by('-id')
    serializer = UserSerializer(tasks, many=True)
    return Response(serializer.data)

# Get All Creations from server.
@api_view(['GET'])
def creation_list(request):
    tasks = Creation.objects.all().order_by('-id')
    serializer = CreationSerializer(tasks, many=True)
    return Response(serializer.data)


# region put

@api_view(['PUT'])
def creation_edit(request,pk):
    creation = Creation.objects.get(pk=pk)
    serializer = CreationSerializer(creation, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# end region



@api_view(['DELETE'])
def creation_delete(request,pk):
    creation = Creation.objects.get(pk=pk)
    creation.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

