from django.urls import path

from api.views import PostUser, userDetail, userCreate, userList,creationDetail,creationCreate,creationList

urlpatterns = [
    path('get-user/<str:pk>/', userDetail, name="get-user"),
    path('post-user/', userCreate, name="post-user"),
    path('get-all-users/', userList, name="get-all-users"),

    path('get-creation/<str:pk>/', creationDetail, name="get-creation"),
    path('post-creation/', creationCreate, name="post-creation"),
    path('get-all-creations/', creationList, name="get-all-creations"),
]
