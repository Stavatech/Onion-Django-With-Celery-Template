from django.urls import path
from . import views

urlpatterns = [
    path(r'ping', views.ShallowPing.as_view()),
]