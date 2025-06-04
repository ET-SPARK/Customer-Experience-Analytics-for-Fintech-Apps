import pandas as pd
from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        self.model = pipeline("sentiment-analysis", model=model_name)

    def analyze(self, df, text_column="review"):
        sentiments = self.model(df[text_column].tolist(), truncation=True)
        df["sentiment_label"] = [r["label"] for r in sentiments]
        df["sentiment_score"] = [r["score"] for r in sentiments]
        return df

    def save(self, df, path):
        df.to_csv(path, index=False)
        print(f"Saved sentiment data to {path}")
