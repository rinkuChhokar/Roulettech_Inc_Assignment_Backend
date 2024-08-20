from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name="default"),
    path('search-course', views.search_course, name="search_course"),
    
]