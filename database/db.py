import sqlite3

conn = sqlite3.connect(
    "data/semiconductor_risk.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company TEXT,

    country TEXT,

    event_type TEXT,

    severity TEXT,

    summary TEXT,

    risk_score INTEGER,

    risk_level TEXT

)
""")

conn.commit()

conn.close()

print("Database initialized")