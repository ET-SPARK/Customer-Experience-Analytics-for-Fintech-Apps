# src/review_scraper.py

from google_play_scraper import Sort, reviews_all
import pandas as pd

class GooglePlayScraper:
    def __init__(self, apps: dict):
        """
        apps: dict of bank_name -> app_id
        """
        self.apps = apps
        self.reviews_df = pd.DataFrame()

    def fetch_reviews(self, app_id, bank_name):
        reviews = reviews_all(
            app_id,
            sleep_milliseconds=0,
            lang='en',
            country='us',
            sort=Sort.NEWEST
        )

        return [{
            "review": r["content"],
            "rating": r["score"],
            "date": r["at"].strftime('%Y-%m-%d'),
            "bank": bank_name,
            "source": "Google Play"
        } for r in reviews]

    def scrape(self):
        all_data = []
        for bank, app_id in self.apps.items():
            print(f"Scraping {bank}...")
            bank_reviews = self.fetch_reviews(app_id, bank)
            print(f"{bank}: {len(bank_reviews)} reviews scraped.")
            all_data.extend(bank_reviews)

        self.reviews_df = pd.DataFrame(all_data)

    def save(self, path="data/raw_reviews.csv"):
        self.reviews_df.to_csv(path, index=False)
        print(f"Saved raw reviews to {path}")
