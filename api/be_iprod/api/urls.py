from django.urls import path

from api.views import *
urlpatterns = [
    path('', index, name=""),
    path('get-user/<str:pk>/', user_detail, name="get-user"),
    path('post-user/', user_create, name="post-user"),
    path('get-all-users/', user_list, name="get-all-users"),

    path('get-creation/<str:pk>/', creation_detail, name="get-creation"),
    path('post-creation/', creation_create, name="post-creation"),
    path('get-all-creations/', creation_list, name="get-all-creations"),
    path('edit-creation/<str:pk>/', creation_edit, name="edit-creation"),
    path('delete-creation/<str:pk>/', creation_delete, name="edit-creation"),


]
