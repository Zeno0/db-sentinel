from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import QueryStat
from .collector import collect_query_stats


def slow_queries(request):
    data = list(QueryStat.objects.filter(mean_exec_time__gt=0)
                .values())
    return JsonResponse(data, safe=False)

def run_collector(request):
    collect_query_stats()
    return JsonResponse({"status": "collector ran"})