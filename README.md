# Customer Experience Analytics for Ride-Hailing Apps in Ethiopia

## Objective

Analyze customer feedback from ride-hailing mobile apps to identify key satisfaction drivers and pain points through sentiment and thematic analysis.

---

## Task 1: Review Collection & Preprocessing

### Methodology

- Used `google-play-scraper` to collect reviews for 2 major Ethiopian ride-hailing apps:
  - Ride (com.multibrains.taxi.passenger.ridepassengeret)
  - Feres (com.feres.user)
- Extracted:
  - `review`, `rating`, `date`, `provider`, `source`
- Preprocessing steps:
  - Removed duplicate reviews
  - Dropped missing values
  - Normalized date format to `YYYY-MM-DD`
- Output: `data/clean_reviews.csv`

### Dataset Stats

- Ride: TBD reviews scraped
- Feres: TBD reviews scraped
- **Total cleaned reviews:** TBD

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
- Manually grouped keywords into comprehensive themes per provider:
  - **Driver Availability** - wait times, matching, cancellations
  - **Pricing & Payment** - fares, payment methods, costs
  - **App Performance** - crashes, bugs, speed, reliability
  - **Navigation & GPS** - location accuracy, routing, pickup
  - **Customer Service** - support quality, response time
  - **UI/UX** - interface design, ease of use
  - **Safety & Security** - trust, verification, security features
  - **Driver Behavior** - professionalism, attitude, courtesy
  - **Vehicle Quality** - cleanliness, comfort, condition
  - **Booking & Scheduling** - reservation system, advance booking
  - **Rating System** - feedback mechanisms
  - **Promotions & Discounts** - offers, coupons, deals
  - **Communication** - driver-passenger messaging, calls
  - **Trip Experience** - overall ride quality and satisfaction
- Added column `identified_theme`
- Output: `data/thematic_reviews.csv`

---

## Task 3: Store Cleaned Data in PostgreSQL

### Methodology

- Designed relational schema:
  - `providers` table: Stores ride-hailing provider info
  - `reviews` table: Stores cleaned reviews with foreign key to `providers`
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

  - `Sentiment` trend over time by provider

  - `Rating` distribution across providers

  - `Positive` review word cloud (drivers)

  - `Negative` review word cloud (pain points)

  - `Theme` frequency by provider

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

### Prerequisites
- Python 3.10 or higher
- PostgreSQL (optional, for database storage)
- Virtual environment (recommended)

### Step 1: Set Up Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Analysis Pipeline

The project follows a sequential pipeline. Run each notebook in order:

#### 3.1 Scrape Reviews
```bash
# Open Jupyter Notebook
jupyter notebook

# Then open and run: notebooks/scrape_reviews.ipynb
```
This will scrape reviews from Ride and Feres apps and save to `data/raw_reviews.csv`

#### 3.2 Preprocess Reviews
```bash
# Run: notebooks/preprocess_reviews.ipynb
```
This cleans the data and saves to `data/clean_reviews.csv`

#### 3.3 Sentiment Analysis
```bash
# Run: notebooks/sentiment_analysis.ipynb
```
This analyzes sentiment and saves to `data/sentiment_reviews.csv`

#### 3.4 Thematic Analysis
```bash
# Run: notebooks/thematic_analysis.ipynb
```
This identifies themes and saves to `data/thematic_reviews.csv`

#### 3.5 Generate Insights & Visualizations
```bash
# Run: notebooks/insights_visuals.ipynb
```
This creates visualizations and insights

### Step 4: Store in PostgreSQL (Optional)

If you want to store the data in PostgreSQL:

1. Install and start PostgreSQL
2. Update database credentials in `src/store_reviews_postgres.py`
3. Run:
```bash
python src/store_reviews_postgres.py
```

### Alternative: Run Individual Scripts

You can also run the Python scripts directly:

```bash
# Scraping (if you prefer script over notebook)
python -c "from src.review_scraper import GooglePlayScraper; scraper = GooglePlayScraper({'Ride': 'com.multibrains.taxi.passenger.ridepassengeret', 'Feres': 'com.feres.user'}); scraper.scrape(); scraper.save('data/raw_reviews.csv')"

# Preprocessing
python -c "from src.review_preprocessor import ReviewPreprocessor; p = ReviewPreprocessor('data/raw_reviews.csv', 'data/clean_reviews.csv'); p.load_data(); p.clean(); p.save()"
```

### Troubleshooting

**Issue: Packages not installing**
- Make sure you're using Python 3.10+
- Try upgrading pip: `pip install --upgrade pip`

**Issue: PostgreSQL connection error**
- Make sure PostgreSQL is running
- Check credentials in `src/store_reviews_postgres.py`
- Create the database first: `createdb ridehailing_reviews`

**Issue: Jupyter not found**
- Install Jupyter: `pip install jupyter notebook`

**Issue: Scraping fails**
- Check internet connection
- The Google Play Store might have rate limits
- Try running with smaller batches

---

## KPIs

- Sentiment score computed for 90%+ of reviews

- Minimum 3 themes per provider identified

- Modular pipeline with reusable classes for sentiment and thematic analysis

- Data inserted into PostgreSQL with full schema

- SQL dump and ETL script committed to GitHub

- 5 visualizations created with labels, legends, and insights

- Evidence-based product recommendations included

---
