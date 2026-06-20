import feedparser

RSS_FEEDS = [
    "https://feeds.feedburner.com/TechCrunch/",
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
]

for feed_url in RSS_FEEDS:
    print(f"\nChecking: {feed_url}")

    feed = feedparser.parse(feed_url)

    print("Entries found:", len(feed.entries))

    if len(feed.entries) > 0:
        print("First title:")
        print(feed.entries[0].title)