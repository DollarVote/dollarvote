from django.urls import path

from . import views

urlpatterns = [
    path('get_company/', views.index, name='index'),
]