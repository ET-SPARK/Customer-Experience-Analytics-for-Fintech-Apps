# Customer-Experience-Analytics-for-Fintech-Apps

# Google Play Store Review Analysis

## Objective

Scrape and preprocess user reviews of mobile banking apps from the Google Play Store.

## Methodology

- Used `google-play-scraper` to collect 400+ reviews for 3 major banking apps.
- Extracted review content, rating, date, and app name.
- Preprocessed the dataset:
  - Removed duplicates
  - Handled missing data
  - Normalized date format to `YYYY-MM-DD`
- Saved to clean CSV format with fields: `review`, `rating`, `date`, `bank`, `source`.

## Dataset

- Total reviews: 1,200+
- Missing data: <5%
