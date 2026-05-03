# DB Sentinel

A lightweight database monitoring system that tracks PostgreSQL query performance and surfaces insights through a simple dashboard.

---

## 🚀 Overview

DB Sentinel collects query statistics from PostgreSQL using `pg_stat_statements`, stores them for analysis, and visualizes performance trends.

It also includes basic alerting to highlight slow or high-frequency queries.

---

## ⚙️ Features

- 📊 Track slow and frequent queries  
- ⏱️ Time-based filtering (1h / 24h / 7d)  
- 📈 Dashboard with charts (Chart.js)  
- 🔄 Automated data collection (GitHub Actions / command)  
- 🚨 Telegram alerts for performance issues  
- 🧪 Simulated load & activity generation  

---

## 🧠 How it works

1. PostgreSQL tracks queries using `pg_stat_statements`
2. A collector fetches and stores metrics in the database
3. Django serves APIs and dashboard
4. Charts visualize query performance
5. Alerts notify when thresholds are exceeded

---

## 🛠️ Tech Stack

- Django  
- PostgreSQL (Neon)  
- Chart.js  
- GitHub Actions  
- Telegram Bot API  

---

## ▶️ Running the project

### 1. Clone repo

```bash
git clone https://github.com/Zeno0/db-sentinel.git
cd db-sentinel/db_sentinel
```

### 2.Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
# OR
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure environment variables

Create a .env file OR export manually:
```bash
export DB_NAME=neondb
export DB_USER=neondb_owner
export DB_PASSWORD=your_password
export DB_HOST=your_host
export DB_PORT=5432

export TELEGRAM_BOT_TOKEN=your_token
export TELEGRAM_CHAT_ID=your_chat_id
```

### 5. Enable PostgreSQL extension

Run this in your database:
```bash
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```
### 6. Run migrations

Make sure you are inside:
```bash
db_sentinel/
```
Then run:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Start Server
```bash
python manage.py runserver
```
### 8. Open dashboard
```bash
http://127.0.0.1:8000/dashboard/
```
---

## 🔁 Commands

### Generate test activity
```bash
python manage.py generate_activity --count 200
```
### Collect query stats
```bash
python manage.py collect_stats
```
### Simulate real traffic (optional)

From repo root:
```bash
python load_test.py
```
## 📊 Features
- View slow queries
- Track frequent queries
- Time-based filtering (1h / 24h / 7d)
- Execution trend charts
- Telegram alerts
## 🚨 Alerts

Configure Telegram:

- TELEGRAM_BOT_TOKEN
- TELEGRAM_CHAT_ID

Alerts trigger when query thresholds are exceeded.

## 📌 Notes
- Uses pg_stat_statements (must be enabled in PostgreSQL)
- GitHub Actions scheduling is not real-time (best effort)
## 💡 Future Improvements
- Background workers (Celery)