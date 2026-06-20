import sqlite3
from newspaper import Article

conn = sqlite3.connect(
    "data/semiconductor_risk.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    id,
    url
FROM articles
WHERE article_text IS NULL
   OR article_text = ''
LIMIT 20
""")

rows = cursor.fetchall()

print(f"Downloading {len(rows)} articles...\n")

for article_id, url in rows:

    try:

        article = Article(url)

        article.download()

        article.parse()

        text = article.text

        cursor.execute(
            """
            UPDATE articles
            SET article_text = ?
            WHERE id = ?
            """,
            (
                text,
                article_id
            )
        )

        conn.commit()

        print(f"Downloaded {article_id}")

    except Exception as e:

        print(f"Failed {article_id}")

conn.close()

print("\nFinished.")