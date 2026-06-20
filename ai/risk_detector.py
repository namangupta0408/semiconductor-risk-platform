import json

from models.llm import generate
from ai.prompts import RISK_PROMPT


def detect_risk(headline):

    prompt = RISK_PROMPT.format(
        headline=headline
    )

    response = generate(prompt)

    return json.loads(response)