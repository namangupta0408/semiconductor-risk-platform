import json

from models.llm import generate
from ai.prompts import EVENT_PROMPT


def extract_event(document):

    prompt = EVENT_PROMPT.format(
        document=document
    )

    response = generate(prompt)

    return json.loads(response)