import json

VALID_SEVERITIES = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

VALID_EVENTS = [
    "Earthquake",
    "Flood",
    "Fire",
    "Factory Shutdown",
    "Trade Restriction",
    "Sanction",
    "Geopolitical Conflict",
    "Labor Strike",
    "Power Outage",
    "Logistics Disruption",
    "Raw Material Shortage"
]

with open("data/known_companies.json", "r") as f:
    KNOWN_COMPANIES = json.load(f)

with open("data/countries.json", "r") as f:
    COUNTRIES = json.load(f)


def validate_event(event):

    company = event.get("company", "").strip()
    country = event.get("country", "").strip()

    if company in COUNTRIES:
        company = "Unknown"

    if company not in KNOWN_COMPANIES:
        company = "Unknown"

    if not country:
        country = "Unknown"

    if country not in COUNTRIES:
        country = "Unknown"

    severity = event.get("severity", "Medium")

    if severity not in VALID_SEVERITIES:
        severity = "Medium"

    event_type = event.get("event_type", "Unknown")

    if event_type not in VALID_EVENTS:
        event_type = "Unknown"

    summary = event.get("summary", "")

    event["company"] = company
    event["country"] = country
    event["severity"] = severity
    event["event_type"] = event_type
    event["summary"] = summary

    return event