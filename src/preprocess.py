import pandas as pd

def preprocess_reviews(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    # Drop duplicates and nulls
    df.drop_duplicates(subset=['review'], inplace=True)
    df.dropna(subset=['review', 'rating', 'date'], inplace=True)

    # Normalize date format
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

    # Ensure correct columns and order
    df = df[['review', 'rating', 'date', 'bank', 'source']]

    df.to_csv(output_csv, index=False)
    print(f"Saved cleaned data to {output_csv}")
    print(f"Final count: {len(df)} reviews")

if __name__ == "__main__":
    preprocess_reviews("data/raw_reviews.csv", "data/clean_reviews.csv")
