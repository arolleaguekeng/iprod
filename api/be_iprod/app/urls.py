from django.urls import path
from app.views import *

urlpatterns = [

    path('get-creation/<str:pk>/', get_creation_by_id, name="get-creation"),
    path('get-all-creations/', get_all_creations, name="gett-all-creations"),
    

]