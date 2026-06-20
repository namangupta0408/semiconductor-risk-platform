RISK_PROMPT = """
You are an expert semiconductor supply chain analyst.

Determine whether the following news represents a meaningful semiconductor supply chain risk.

Return ONLY valid JSON.

Format:

{{
    "is_risk": true
}}

Headline:

{headline}
"""


EVENT_PROMPT = """
You are an expert semiconductor supply chain analyst.

Read the following document carefully.

Extract ONLY ONE semiconductor supply chain event.

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

Format:

{{
    "company":"",
    "country":"",
    "event_type":"",
    "severity":"",
    "summary":""
}}

Document:

{document}
"""