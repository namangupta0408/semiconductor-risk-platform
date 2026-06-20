import sqlite3
import pandas as pd

conn = sqlite3.connect("data/semiconductor_risk.db")

query = """
SELECT

country,

COUNT(*) AS total_events,

ROUND(AVG(risk_score),2) AS average_risk,

MAX(risk_score) AS highest_risk

FROM events

JOIN risk_scores

ON events.id = risk_scores.event_id

WHERE country IS NOT NULL
AND country != ''

GROUP BY country

ORDER BY average_risk DESC
"""

df = pd.read_sql_query(query, conn)

conn.close()

df.to_csv(
    "data/country_risk.csv",
    index=False
)

print(df)

print("\nGenerated country_risk.csv")