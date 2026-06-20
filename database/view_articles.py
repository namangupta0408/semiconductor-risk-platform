import sqlite3

conn = sqlite3.connect(
    "data/semiconductor_risk.db"
)

cursor = conn.cursor()

cursor.execute(
    """
    SELECT id,
           search_term,
           title
    FROM articles
    LIMIT 20
    """
)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()