import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from newsapi import NewsApiClient
from config import NEWS_API_KEY
import pandas as pd

newsapi = NewsApiClient(api_key=NEWS_API_KEY)

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

for term in SEARCH_TERMS:

    print(f"\nSearching: {term}")

    response = newsapi.get_everything(
        q=term,
        language="en",
        sort_by="publishedAt",
        page_size=20
    )

    print(f"Found {len(response['articles'])} articles")

    for article in response["articles"]:

        articles.append({

            "search_term": term,

            "title": article.get("title", ""),

            "description": article.get("description", ""),

            "url": article.get("url", ""),

            "source": article.get("source", {}).get("name", ""),

            "published": article.get("publishedAt", "")

        })

df = pd.DataFrame(articles)

df.drop_duplicates(
    subset=["url"],
    inplace=True
)

df.to_csv(
    "data/news_articles.csv",
    index=False
)

print(f"\nSaved {len(df)} articles")