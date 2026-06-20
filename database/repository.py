import sqlite3

DB = "data/semiconductor_risk.db"


class Repository:

    def __init__(self):

        self.conn = sqlite3.connect(DB)

        self.cursor = self.conn.cursor()

    def get_articles(self, limit=50):

        self.cursor.execute(
            """
            SELECT id,title
            FROM articles
            WHERE processed=0
            LIMIT ?
            """,
            (limit,)
        )

        return self.cursor.fetchall()

    def save_event(self, article_id, event):

        self.cursor.execute(
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
            VALUES
            (?,?,?,?,?,?)
            """,
            (
                article_id,
                event.get("company","Unknown"),
                event.get("country","Unknown"),
                event.get("event_type","Unknown"),
                event.get("severity","Medium"),
                event.get("summary","")
            )
        )

        self.conn.commit()

    def mark_processed(self, article_id):

        self.cursor.execute(
            """
            UPDATE articles
            SET processed=1
            WHERE id=?
            """,
            (article_id,)
        )

        self.conn.commit()

    def close(self):

        self.conn.close()