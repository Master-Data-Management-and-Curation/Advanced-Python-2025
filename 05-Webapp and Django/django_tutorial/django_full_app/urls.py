from django.urls import path
from . import views

urlpatterns = [
    path('', views.researcher_view, name='researcher_view'),
]