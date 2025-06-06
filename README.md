# Customer-Experience-Analytics-for-Fintech-Apps

## Objective

Analyze customer feedback from mobile banking apps to identify key satisfaction drivers and pain points through sentiment and thematic analysis.

---

## Task 1: Review Collection & Preprocessing

### Methodology

- Used `google-play-scraper` to collect reviews for 3 major Ethiopian banking apps:
  - Commercial Bank of Ethiopia (CBE)
  - Bank of Abyssinia (BOA)
  - Dashen Bank (DB)
- Extracted:
  - `review`, `rating`, `date`, `bank`, `source`
- Preprocessing steps:
  - Removed duplicate reviews
  - Dropped missing values
  - Normalized date format to `YYYY-MM-DD`
- Output: `data/clean_reviews.csv`

### Dataset Stats

- CBE: 7,483 reviews scraped
- BOA: 1,044 reviews scraped
- DB: 449 reviews scraped
- **Total cleaned reviews:** 6,661

---

## Task 2: Sentiment & Thematic Analysis

### Sentiment Analysis

- Model: `distilbert-base-uncased-finetuned-sst-2-english` via Hugging Face Transformers
- Classified each review into:
  - `Positive`, `Negative`, or `Neutral` (via probability thresholding)
- Added:
  - `sentiment_label` and `sentiment_score` to dataset
- Output: `data/sentiment_reviews.csv`

### Thematic Analysis

- Used `spaCy` for lemmatization and tokenization
- Extracted keywords using `TF-IDF` (with n-grams)
- Manually grouped keywords into 3–5 themes per bank:
  - Account Access
  - Transaction Performance
  - User Interface & UX
  - Customer Support
  - Reliability & Speed
- Added column `identified_theme`
- Output: `data/thematic_reviews.csv`

---

## Task 3: Store Cleaned Data in PostgreSQL

### Methodology

- Designed relational schema:
  - `banks` table: Stores bank info
  - `reviews` table: Stores cleaned reviews with foreign key to `banks`
- Used `psycopg2` for Python–PostgreSQL integration
- Inserted full dataset (`thematic_reviews.csv`) into PostgreSQL
- Schema and data exported to SQL dump

### Files

- Insert script: `src/store_reviews_postgres.py`
- SQL dump: `sql/db_schema_dump.sql`

---

## Task 4: Insights, Visualizations & Recommendations

### Visualizations

- Created 5 visualizations using `Seaborn`, `Matplotlib` and `WordCloud`:

  - `Sentiment` trend over time by bank

  - `Rating` distribution across banks

  - `Positive` review word cloud (drivers)

  - `Negative` review word cloud (pain points)

  - `Theme` frequency by bank

All visualizations are in:
📁 `notebook/insights_visuals.ipynb`

## File Structure

project/
├── data/
│ ├── clean_reviews.csv
│ ├── raw_reviews.csv
│ ├── sentiment_reviews.csv
│ └── thematic_reviews.csv
├── src/
│ ├── db_schema_dump.sql
├── src/
│ ├── sentiment_analyzer.py
│ └── thematic_analyzer.py
│ ├── review_preprocessor.py
│ └── review_scraper.py
│ └── store_reviews_postgres.py
├── notebook/
│ ├── sentiment_analysis.ipynb
│ └── thematic_analysis.ipynb
│ ├── insights_visuals.ipynb
│ ├── preprocess_reviews.ipynb
│ └── scrape_reviews.ipynb
├── requirements.txt
├── .gitignore
└── README.md

---

## How to Run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt

   ```

2. Run each step using the Jupyter notebooks in the notebook/ folder.

---

## KPIs

- Sentiment score computed for 90%+ of reviews

- Minimum 3 themes per bank identified

- Modular pipeline with reusable classes for sentiment and thematic analysis

- Data inserted into PostgreSQL with full schema

- SQL dump and ETL script committed to GitHub

- 5 visualizations created with labels, legends, and insights

- Evidence-based product recommendations included

---
