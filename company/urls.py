from django.urls import path, include
from company import views

urlpatterns = [

    path('add/', views.add_company, name='add_company'),


]
