import ollama
import json

sample_article = """
TSMC temporarily halted production after a major earthquake
in Taiwan. Several fabrication facilities experienced power
interruptions and production delays.
"""

prompt = f"""
You are a semiconductor supply chain analyst.

Return ONLY valid JSON.

Allowed event types:

Earthquake
Flood
Fire
Factory Shutdown
Trade Restriction
Sanction
Geopolitical Conflict
Labor Strike
Power Outage
Logistics Disruption
Raw Material Shortage

Allowed severity:

Low
Medium
High
Critical

Choose ONLY from the lists above.

Format:

{{
    "company": "",
    "country": "",
    "event_type": "",
    "severity": "",
    "summary": ""
}}

Article:

{sample_article}
"""

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

raw_output = response["message"]["content"]

print("\nRAW OUTPUT:\n")
print(raw_output)

try:
    data = json.loads(raw_output)

    print("\nPARSED JSON:\n")
    print(json.dumps(data, indent=4))

except Exception as e:
    print("\nJSON PARSE FAILED")
    print(e)