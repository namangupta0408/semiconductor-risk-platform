from extraction.risk_detector import detect_risk
from extraction.event_extractor import extract_event

from database.event_repository import (
    get_unprocessed_articles,
    save_event,
    mark_processed
)

articles = get_unprocessed_articles()

print(f"\nProcessing {len(articles)} articles...\n")

for article_id, title in articles:

    try:

        risk = detect_risk(title)

        if not risk.get("is_risk"):

            print(f"IGNORE -> {title}")

            mark_processed(article_id)

            continue

        print(f"RISK -> {title}")

        event = extract_event(title)

        save_event(article_id, event)

        mark_processed(article_id)

    except Exception as e:

        print(f"\nERROR: {title}")

        print(e)

print("\nPipeline Finished")