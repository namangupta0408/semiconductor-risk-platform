import sqlite3
import ollama

conn = sqlite3.connect(
    "data/semiconductor_risk.db"
)

cursor = conn.cursor()

cursor.execute("""

SELECT

company,
country,
event_type,
severity,
summary

FROM events

ORDER BY id DESC

LIMIT 20

""")

rows = cursor.fetchall()

text = ""

for row in rows:

    text += f"""

Company: {row[0]}
Country: {row[1]}
Event: {row[2]}
Severity: {row[3]}
Summary: {row[4]}

"""

prompt = f"""

You are a semiconductor supply chain analyst.

Write an executive briefing in under 250 words.

{text}

"""

response = ollama.chat(

model="llama3.2",

messages=[
{
"role":"user",
"content":prompt
}
]

)

summary = response["message"]["content"]

print(summary)

with open(

"data/executive_summary.txt",

"w"

) as f:

    f.write(summary)

print("\nExecutive summary generated.")