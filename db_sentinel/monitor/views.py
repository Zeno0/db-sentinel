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

def dashboard(request):
    slow_queries = QueryStat.objects.order_by('-mean_exec_time')[:10]
    frequent_queries = QueryStat.objects.order_by('-calls')[:10]

        # Prepare data for charts
    slow_labels = [q.query[:30] for q in slow_queries]
    slow_values = [q.mean_exec_time for q in slow_queries]

    freq_labels = [q.query[:30] for q in frequent_queries]
    freq_values = [q.calls for q in frequent_queries]

    context = {
        'slow_queries': slow_queries,
        'frequent_queries': frequent_queries,
        'slow_labels': slow_labels,
        'slow_values': slow_values,
        'freq_labels': freq_labels,
        'freq_values': freq_values,
    }

    return render(request, 'monitor/dashboard.html', context)