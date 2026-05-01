from django.urls import path
from .views import slow_queries, dashboard
# from .views import run_collector

urlpatterns = [
    path('slow-queries/', slow_queries),
    path('dashboard/', dashboard),
    # path('run-collector/', run_collector),
]
