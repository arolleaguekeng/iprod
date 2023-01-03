from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User,Creation
from .serializers import UserSerializer 


class PostUser(APIView):
    serializer_class = UserSerializer


# region POST methods
@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

# POST creation in server
@api_view(['POST'])
def creationCreate(request):
    serializer = CreationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
# endregion


# Get one user By Id.
@api_view(['GET'])
def userDetail(request, pk):
    tasks = User.objects.get(id=pk)
    serializer = UserSerializer(tasks, many=False)
    return Response(serializer.data)

# Get one creation By Id.
@api_view(['GET'])
def creationDetail(request, pk):
    tasks = Creation.objects.get(id=pk)
    serializer = CreationSerializer(tasks, many=False)
    return Response(serializer.data)


# Get All users from server.
@api_view(['GET'])
def userList(request):
    tasks = User.objects.all().order_by('-id')
    serializer = UserSerializer(tasks, many=True)
    return Response(serializer.data)

# Get All Creations from server.
@api_view(['GET'])
def creationList(request):
    tasks = Creation.objects.all().order_by('-id')
    serializer = CreationSerializer(tasks, many=True)
    return Response(serializer.data)


# Create your views here.
