import json
import sqlite3

conn = sqlite3.connect(
    "data/semiconductor_risk.db"
)

cursor = conn.cursor()

with open(
    "data/risk_report.json",
    "r"
) as f:

    events = json.load(f)

for event in events:

    cursor.execute(
        """
        INSERT INTO events
        (
            company,
            country,
            event_type,
            severity,
            summary,
            risk_score,
            risk_level
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            event.get("company", "Unknown"),
            event.get("country", "Unknown"),
            event.get("event_type", "Unknown"),
            event.get("severity", "Medium"),
            event.get("summary", ""),
            event.get("risk_score", 0),
            event.get("risk_level", "Low")
        )
    )

conn.commit()

conn.close()

print(
    f"Loaded {len(events)} events"
)