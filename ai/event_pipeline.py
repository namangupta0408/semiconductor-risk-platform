import sqlite3

from ai.event_extractor import extract_event


conn = sqlite3.connect(
    "data/semiconductor_risk.db"
)

cursor = conn.cursor()


cursor.execute("""

SELECT

id,

title,

description,

article_text

FROM articles

WHERE processed=0

LIMIT 20

""")

articles = cursor.fetchall()

print(
    f"Processing {len(articles)} articles\n"
)

for article in articles:

    article_id = article[0]

    title = article[1]

    description = article[2]

    article_text = article[3]

    document = f"""

TITLE

{title}


DESCRIPTION

{description}


ARTICLE

{article_text}

"""

    try:

        event = extract_event(document)

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

        cursor.execute(

            """

            UPDATE articles

            SET processed=1

            WHERE id=?

            """,

            (article_id,)

        )

        conn.commit()

        print(

            f"Processed {article_id}"

        )

    except Exception as e:

        print(e)

conn.close()

print("\nDone.")