from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from api.models import *
from rest_framework.response import Response
from api.serializers import *
from django.template.response import TemplateResponse
# Create your views here.

def get_creation_by_id(request,pk):
    creation = Creation.objects.get(pk=pk)
    return render(request, 'index.html',{'creation':creation})



def get_all_creations(request):
    return TemplateResponse(request, 'creations_list.html', {'creations': Creation.objects.all()})
