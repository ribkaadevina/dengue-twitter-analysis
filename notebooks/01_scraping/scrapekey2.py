import os
from dotenv import load_dotenv
from Scweet import Scweet
import pandas as pd

load_dotenv()

# --- EDIT THESE BEFORE EACH RUN ---
SINCE_DATE = "2025-12-01"
UNTIL_DATE = "2025-12-15"
OUTPUT_FILENAME = "Key2_Dec1_25.csv"
# -----------------------------------

print("Starting scraping...")

auth_token = os.environ.get("SCWEET_AUTH_TOKEN")
if not auth_token:
    raise ValueError("SCWEET_AUTH_TOKEN not found. Please set it in your .env file.")

s = Scweet(
    auth_token=auth_token
)

tweets = s.search("aedes aegypti", since=SINCE_DATE, until=UNTIL_DATE, lang="id", limit=500, save=False)

print("Scraping finished.")

for i in range(100, len(tweets)+1, 100):
    print(f"Collected {i} tweets")

print(f"Total collected: {len(tweets)} tweets")

df = pd.DataFrame(tweets)

df.to_csv(OUTPUT_FILENAME, index=False, encoding="utf-8-sig")

print(f"Saved to {OUTPUT_FILENAME}")