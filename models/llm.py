import ollama

MODEL = "llama3.2"


def generate(prompt):

    response = ollama.chat(
        model=MODEL,
        format="json",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]