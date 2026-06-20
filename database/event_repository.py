import sqlite3


DB_PATH = "data/semiconductor_risk.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def get_unprocessed_articles(limit=50):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, title
        FROM articles
        WHERE processed = 0
        LIMIT ?
        """,
        (limit,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows


def save_event(article_id, event):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO events
        (
            article_id,
            company,
            country,
            event_type,
            severity,
            summary
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            article_id,
            event.get("company", "Unknown"),
            event.get("country", "Unknown"),
            event.get("event_type", "Unknown"),
            event.get("severity", "Medium"),
            event.get("summary", "")
        )
    )

    conn.commit()

    conn.close()


def mark_processed(article_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE articles
        SET processed = 1
        WHERE id = ?
        """,
        (article_id,)
    )

    conn.commit()

    conn.close()