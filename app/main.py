import subprocess

STEPS = [

    ("Collect News",
     "python collectors/news_collector.py"),

    ("Load Articles",
     "python database/load_articles.py"),

    ("Download Articles",
     "python collectors/article_fetcher.py"),

    ("Extract Events",
     "python -m ai.event_pipeline"),

    ("Calculate Risk",
     "python analytics/scoring.py"),

]

print("=" * 60)
print(" Semiconductor Supply Chain Intelligence Platform ")
print("=" * 60)

for name, command in STEPS:

    print(f"\n{name}")

    print("-" * 60)

    result = subprocess.run(
        command,
        shell=True
    )

    if result.returncode != 0:

        print(f"\n{name} failed.")

        break

print("\nPipeline Finished.")