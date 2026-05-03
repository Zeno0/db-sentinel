from django.db import connection
from .models import QueryStat
from .alerts import send_telegram_alert

def analyze_query(query, mean_exec_time, calls):
    print("Mean time:", mean_exec_time)
    if mean_exec_time >=3:
         send_telegram_alert(
            f"🚨 Slow Query Detected!\n\nQuery: {query[:100]}\nTime: {mean_exec_time} ms"
        )
    if calls > 1500:
        send_telegram_alert(
            f"🔥 High Frequency Query!\n\nQuery: {query[:100]}\nCalls: {calls}"
        )

def collect_query_stats():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT query, calls, total_exec_time, mean_exec_time
            from pg_stat_statements
            ORDER BY total_exec_time DESC
            LIMIT 10;
    """)
        rows = cursor.fetchall()
        for row in rows:
            QueryStat.objects.create(
                query=row[0],
                calls=row[1],
                total_exec_time=row[2],
                mean_exec_time=row[3]
            )
            print("Calling analyze_query")
            analyze_query(row[0], row[3], row[1]) 
