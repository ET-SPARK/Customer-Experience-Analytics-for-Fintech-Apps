# src/review_preprocessor.py

import pandas as pd

class ReviewPreprocessor:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.df = pd.DataFrame()

    def load_data(self):
        self.df = pd.read_csv(self.input_path)

    def clean(self):
        self.df.drop_duplicates(subset=['review'], inplace=True)
        self.df.dropna(subset=['review', 'rating', 'date'], inplace=True)
        self.df['date'] = pd.to_datetime(self.df['date']).dt.strftime('%Y-%m-%d')
        self.df = self.df[['review', 'rating', 'date', 'bank', 'source']]

    def save(self):
        self.df.to_csv(self.output_path, index=False)
        print(f"Saved cleaned data to {self.output_path}")
        print(f"Final count: {len(self.df)} reviews")
