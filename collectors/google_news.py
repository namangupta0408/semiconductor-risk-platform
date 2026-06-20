import requests
import pandas as pd
from bs4 import BeautifulSoup

SEARCH_TERMS = [
    "semiconductor earthquake",
    "semiconductor fire",
    "semiconductor factory shutdown",
    "chip shortage",
    "semiconductor export restrictions",
    "TSMC disruption",
    "ASML export controls",
    "semiconductor sanctions",
    "semiconductor power outage",
    "Taiwan semiconductor risk"
]

articles = []

headers = {
    "User-Agent":
    "Mozilla/5.0"
}

for term in SEARCH_TERMS:

    print(f"Searching: {term}")

    url = (
        "https://news.google.com/search?q="
        + term.replace(" ", "%20")
    )

    try:

        response = requests.get(
            url,
            headers=headers
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        titles = soup.find_all("a")

        count = 0

        for title in titles:

            text = title.text.strip()

            if len(text) > 30:

                articles.append(
                    {
                        "search_term": term,
                        "title": text
                    }
                )

                count += 1

            if count >= 20:
                break

        print(
            f"Collected {count}"
        )

    except Exception as e:

        print(e)

df = pd.DataFrame(
    articles
)

df.drop_duplicates(
    subset=["title"],
    inplace=True
)

df.to_csv(
    "data/news_articles.csv",
    index=False
)

print(
    f"\nSaved {len(df)} articles"
)