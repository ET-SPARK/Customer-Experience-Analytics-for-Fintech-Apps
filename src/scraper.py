from google_play_scraper import Sort, reviews_all
import pandas as pd

def fetch_reviews(app_id, bank_name):
    reviews = reviews_all(
        app_id,
        sleep_milliseconds=0,
        lang='en',
        country='us',
        sort=Sort.NEWEST
    )

    data = [{
        "review": r["content"],
        "rating": r["score"],
        "date": r["at"].strftime('%Y-%m-%d'),
        "bank": bank_name,
        "source": "Google Play"
    } for r in reviews]

    return pd.DataFrame(data)

if __name__ == "__main__":
    apps = {
        "BankA": "com.combanketh.mobilebanking",
        "BankB": "com.boa.boaMobileBanking",
        "BankC": "com.dashen.dashensuperapp"
    }

    all_reviews = pd.DataFrame()
    for bank, app_id in apps.items():
        df = fetch_reviews(app_id, bank)
        print(f"{bank}: {len(df)} reviews scraped.")
        all_reviews = pd.concat([all_reviews, df])

    all_reviews.to_csv("data/raw_reviews.csv", index=False)
