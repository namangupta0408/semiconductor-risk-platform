import sqlite3

SEVERITY_SCORES = {
    "Low": 25,
    "Medium": 50,
    "High": 75,
    "Critical": 100
}

EVENT_WEIGHTS = {
    "Earthquake": 20,
    "Flood": 15,
    "Fire": 15,
    "Factory Shutdown": 20,
    "Trade Restriction": 25,
    "Sanction": 25,
    "Geopolitical Conflict": 30,
    "Labor Strike": 10,
    "Power Outage": 10,
    "Logistics Disruption": 15,
    "Raw Material Shortage": 20
}

conn = sqlite3.connect("data/semiconductor_risk.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
    id,
    severity,
    event_type
FROM events
""")

events = cursor.fetchall()

generated = 0

for event_id, severity, event_type in events:

    severity_score = SEVERITY_SCORES.get(severity, 50)
    event_weight = EVENT_WEIGHTS.get(event_type, 10)

    final_score = min(
        severity_score + event_weight,
        100
    )

    if final_score >= 85:
        level = "Critical"
    elif final_score >= 65:
        level = "High"
    elif final_score >= 40:
        level = "Medium"
    else:
        level = "Low"

    cursor.execute("""
    INSERT INTO risk_scores
    (
        event_id,
        risk_score,
        risk_level
    )
    VALUES
    (?,?,?)
    """,
    (
        event_id,
        final_score,
        level
    ))

    generated += 1

conn.commit()
conn.close()

print(f"Generated {generated} risk scores")