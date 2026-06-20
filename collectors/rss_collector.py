import feedparser
import pandas as pd

RSS_FEEDS = [

    # Semiconductor Engineering
    "https://semiengineering.com/feed/",

    # EE Times
    "https://www.eetimes.com/feed/",

    # Tom's Hardware
    "https://www.tomshardware.com/feeds/all",

    # AnandTech
    "https://www.anandtech.com/rss/",

    # NYTimes Technology
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
]

articles = []

for feed_url in RSS_FEEDS:

    print(f"\nChecking {feed_url}")

    feed = feedparser.parse(feed_url)

    print(f"Found {len(feed.entries)} entries")

    for entry in feed.entries:

        articles.append({

            "title": entry.get("title", ""),

            "url": entry.get("link", ""),

            "published": entry.get("published", ""),

            "source": feed.feed.get("title", "")

        })

df = pd.DataFrame(articles)

df.drop_duplicates(
    subset=["url"],
    inplace=True
)

df.to_csv(
    "data/rss_articles.csv",
    index=False
)

print(f"\nSaved {len(df)} articles")