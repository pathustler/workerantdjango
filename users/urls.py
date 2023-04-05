from django.urls import path
from . import views

urlpatterns = [
     path('',views.Userslist.as_view())
]
