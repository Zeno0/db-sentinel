import requests
import threading

URL = "https://db-sentinel.onrender.com/slow-queries/"

def hit_api(thread_id):
    for i in range(50):  # 50 calls by each user
        try:
            requests.get(URL, timeout=5)
            print(f"Thread {thread_id} → Request {i} done")
        except Exception as e:
            print(f"Thread {thread_id} error:", e)

threads = []

for i in range(10):  # 10 users
    t = threading.Thread(target=hit_api, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("DONE ✅")