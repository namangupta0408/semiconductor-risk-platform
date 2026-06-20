import json
import ollama

import sys

sys.path.append(".")

from extraction.validator import validate_event


EVENT_TYPES = [
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

with open("data/sample_articles.json", "r") as f:
    articles = json.load(f)

results = []

for item in articles:

    article = item["article"]

    prompt = f"""
Return a valid JSON object.

Allowed event types:
{', '.join(EVENT_TYPES)}

Allowed severity:
Low
Medium
High
Critical

All fields must be present.

If company is unknown return "Unknown".

If country is unknown return "Unknown".

If severity cannot be determined return "Medium".

Format:

{{
    "company": "",
    "country": "",
    "event_type": "",
    "severity": "",
    "summary": ""
}}

Article:

{article}
"""

    response = ollama.chat(
        model="llama3.2",
        format="json",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    try:

        raw_response = response["message"]["content"]

        event = json.loads(raw_response)

        event = validate_event(event)

        results.append(event)

        print(f"Processed article {item['id']}")

    except Exception as e:

        print(f"\nFailed article {item['id']}")

        print("\nRAW RESPONSE:")
        print(response["message"]["content"])

        print("\nERROR:")
        print(e)

with open(
    "data/extracted_events.json",
    "w"
) as f:

    json.dump(
        results,
        f,
        indent=4
    )

print(f"\nSaved {len(results)} events")