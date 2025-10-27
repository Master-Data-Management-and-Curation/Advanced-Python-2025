from django.urls import path
from . import views

urlpatterns = [
    path('', views.orm_tutorial_view, name='orm_tutorial_view'),
]