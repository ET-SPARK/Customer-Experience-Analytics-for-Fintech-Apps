import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
import spacy

class ThematicAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def preprocess(self, text):
        doc = self.nlp(text.lower())
        tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
        return " ".join(tokens)

    def extract_keywords(self, df, text_column="review", top_n=20):
        df["processed"] = df[text_column].apply(self.preprocess)
        tfidf = TfidfVectorizer(ngram_range=(1,2), max_features=top_n)
        X = tfidf.fit_transform(df["processed"])
        keywords = tfidf.get_feature_names_out()
        return keywords

    def assign_themes(self, df, keyword_theme_map):
        df["identified_theme"] = df["processed"].apply(
            lambda text: self.match_theme(text, keyword_theme_map)
        )
        return df

    def match_theme(self, text, keyword_theme_map):
        for keyword, theme in keyword_theme_map.items():
            if keyword in text:
                return theme
        return "Other"

    def save(self, df, path):
        df.to_csv(path, index=False)
        print(f"Saved thematic data to {path}")
