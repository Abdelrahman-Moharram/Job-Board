from django.urls import path , include
from . import views

app_name = "home"

urlpatterns = [
    path('', views.home,name="index"),
    path('<str:username>', views.user_profile,name="user_profile"),
    path('<str:username>/edit', views.edit_user,name="edit_user"),
]
