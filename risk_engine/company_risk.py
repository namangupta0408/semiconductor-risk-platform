import json
from collections import defaultdict

with open(
    "data/risk_report.json",
    "r"
) as f:

    risks = json.load(f)

company_scores = defaultdict(list)

for risk in risks:

    company = risk["company"]

    company_scores[company].append(
        risk["risk_score"]
    )

company_report = []

for company, scores in company_scores.items():

    avg_score = round(
        sum(scores) / len(scores),
        2
    )

    if avg_score >= 85:
        level = "Critical"

    elif avg_score >= 65:
        level = "High"

    elif avg_score >= 40:
        level = "Medium"

    else:
        level = "Low"

    company_report.append(
        {
            "company": company,
            "average_risk_score": avg_score,
            "risk_level": level
        }
    )

company_report.sort(
    key=lambda x: x["average_risk_score"],
    reverse=True
)

with open(
    "data/company_risk_report.json",
    "w"
) as f:

    json.dump(
        company_report,
        f,
        indent=4
    )

print(
    f"Generated {len(company_report)} company profiles"
)