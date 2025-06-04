# Customer-Experience-Analytics-for-Fintech-Apps

## Objective

Scrape and preprocess user reviews of mobile banking apps from the Google Play Store.

## Methodology

- Used `google-play-scraper` to collect reviews for 3 major banking apps.
- Extracted review content, rating, date, and app name.
- Preprocessed the dataset:
  - Removed duplicates
  - Handled missing data
  - Normalized date format to `YYYY-MM-DD`
- Saved to clean CSV format with fields: `review`, `rating`, `date`, `bank`, `source`.

## Dataset

- Scraping CBE...
- CBE: 7483 reviews scraped.
- Scraping BOA...
- BOA: 1044 reviews scraped.
- Scraping DB...
- DB: 449 reviews scraped.

## Cleaned Data

- Final count: 6661 reviews
