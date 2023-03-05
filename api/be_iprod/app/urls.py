from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [

    path('get-creation/<str:pk>/', get_creation_by_id, name="get-creation"),
    path('get-all-creations/', get_all_creations, name="gett-all-creations"),
    path('get-bibiographie/', get_bibiographie, name="gett-all-creations"),
]
