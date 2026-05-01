from django.urls import path
from .views import slow_queries

urlpatterns = [
    path('slow-queries/', slow_queries),
]