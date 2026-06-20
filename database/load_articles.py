import sqlite3
import pandas as pd

df = pd.read_csv(
    "data/news_articles.csv"
)

conn = sqlite3.connect(
    "data/semiconductor_risk.db"
)

cursor = conn.cursor()

loaded = 0

for _, row in df.iterrows():

    try:

        cursor.execute(
            """
            INSERT OR IGNORE INTO articles
            (
                search_term,
                title,
                description,
                url,
                source,
                published,
                article_text,
                processed
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                str(row.get("search_term", "")),
                str(row.get("title", "")),
                str(row.get("description", "")),
                str(row.get("url", "")),
                str(row.get("source", "")),
                str(row.get("published", "")),
                "",
                0
            )
        )

        loaded += 1

    except Exception as e:

        print(e)

conn.commit()

conn.close()

print(
    f"\nLoaded {loaded} articles"
)