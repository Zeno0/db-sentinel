from django.db import connection
from .models import QueryStat

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