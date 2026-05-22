import sqlite3

conn = sqlite3.connect("scam.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user TEXT,
    score REAL,
    result TEXT
)
""")

conn.commit()

def save_report(user, score, result):
    cursor.execute("INSERT INTO reports (user, score, result) VALUES (?, ?, ?)",
                   (user, score, result))
    conn.commit()