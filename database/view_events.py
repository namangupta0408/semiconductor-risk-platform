import sqlite3

conn = sqlite3.connect(
    "data/semiconductor_risk.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    article_id,
    company,
    country,
    event_type,
    severity
FROM events
LIMIT 20
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()