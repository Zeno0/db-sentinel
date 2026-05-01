from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import QueryStat

def slow_queries(request):
    data = list(QueryStat.objects.filter(mean_exec_time__gt=100)
                .values())
    return JsonResponse(data, safe=False)