from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import QueryStat
from .collector import collect_query_stats
from django.utils.timezone import now, timedelta


def slow_queries(request):
    data = list(QueryStat.objects.filter(mean_exec_time__gt=20)
                .values())
    return JsonResponse(data, safe=False)

def run_collector(request):
    collect_query_stats()
    return JsonResponse({"status": "collector ran"})

def dashboard(request):
    from django.utils.timezone import now, timedelta
    time_filter = request.GET.get('range', '1h')
    if time_filter == '24h':
        since = now() - timedelta(hours=24)
    elif time_filter == '7d':
        since = now() - timedelta(days=7)
    else:
        since = now() - timedelta(hours=1)
    recent_queries = QueryStat.objects.filter(created_at__gte=since)




    slow_queries = QueryStat.objects.order_by('-mean_exec_time')[:10]
    frequent_queries = QueryStat.objects.order_by('-calls')[:10]
     # Define time window
    last_hour = now() - timedelta(hours=1)
    # Filter recent queries
    recent_queries = QueryStat.objects.filter(created_at__gte=last_hour)


        # Prepare data for charts
    slow_labels = [q.query[:30] for q in slow_queries]
    slow_values = [q.mean_exec_time for q in slow_queries]

    freq_labels = [q.query[:30] for q in frequent_queries]
    freq_values = [q.calls for q in frequent_queries]

    recent_data = QueryStat.objects.filter(created_at__gte=since).order_by('created_at')

    time_labels = [q.created_at.strftime("%H:%M") for q in recent_data]
    time_values = [q.mean_exec_time for q in recent_data]

    context = {
        'slow_queries': slow_queries,
        'frequent_queries': frequent_queries,
        'selected_range': time_filter,
        'slow_labels': slow_labels,
        'slow_values': slow_values,
        'freq_labels': freq_labels,
        'freq_values': freq_values,
        'time_labels': time_labels,
'       'time_values': time_values
    }

    return render(request, 'monitor/dashboard.html', context)