from dotenv import load_dotenv
import os

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

MODEL_NAME = "llama3.2"

DATABASE_PATH = "data/semiconductor_risk.db"

ARTICLE_BATCH_SIZE = 50