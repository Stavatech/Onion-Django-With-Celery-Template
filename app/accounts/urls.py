from django.urls import path
from . import views

urlpatterns = [
    path(r'<str:id>', views.AccountDetail.as_view()),
]