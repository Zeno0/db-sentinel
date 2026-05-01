from django.urls import path
from .views import slow_queries
from .views import run_collector

urlpatterns = [
    path('slow-queries/', slow_queries),
    path('run-collector/', run_collector),
]
