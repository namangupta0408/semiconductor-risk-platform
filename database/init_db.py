import sqlite3

conn = sqlite3.connect(
    "data/semiconductor_risk.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS articles (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    search_term TEXT,

    title TEXT,

    description TEXT,

    url TEXT UNIQUE,

    source TEXT,

    published TEXT,

    article_text TEXT,

    processed INTEGER DEFAULT 0

)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    article_id INTEGER,

    company TEXT,

    country TEXT,

    event_type TEXT,

    severity TEXT,

    summary TEXT,

    FOREIGN KEY(article_id)
    REFERENCES articles(id)

)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS risk_scores (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    event_id INTEGER,

    risk_score INTEGER,

    risk_level TEXT,

    FOREIGN KEY(event_id)
    REFERENCES events(id)

)
""")

conn.commit()

conn.close()

print("Database initialized successfully")