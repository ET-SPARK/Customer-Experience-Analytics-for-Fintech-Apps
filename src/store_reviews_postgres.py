import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

class PostgresDB:
    def __init__(self, dbname="bank_reviews", user="postgres", password="password", host="localhost", port=5432):
        try:
            self.conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            self.cursor = self.conn.cursor()
            print("✅ Connected to PostgreSQL database.")
        except Exception as e:
            print(f"❌ Failed to connect: {e}")
            raise

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS banks (
                id SERIAL PRIMARY KEY,
                name TEXT UNIQUE NOT NULL
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS reviews (
                id SERIAL PRIMARY KEY,
                bank_id INTEGER REFERENCES banks(id),
                review TEXT NOT NULL,
                rating INTEGER,
                date DATE,
                source TEXT,
                sentiment_label TEXT,
                sentiment_score REAL,
                identified_theme TEXT
            );
        """)
        self.conn.commit()
        print("✅ Tables created (if not exist).")

    def insert_banks(self, df):
        banks = df['bank'].unique()
        for bank in banks:
            self.cursor.execute("""
                INSERT INTO banks (name)
                VALUES (%s)
                ON CONFLICT (name) DO NOTHING;
            """, (bank,))
        self.conn.commit()
        print(f"✅ Inserted {len(banks)} banks.")

    def get_bank_id(self, bank_name):
        self.cursor.execute("SELECT id FROM banks WHERE name = %s;", (bank_name,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def insert_reviews(self, df):
        rows = []
        for _, row in df.iterrows():
            bank_id = self.get_bank_id(row['bank'])
            if not bank_id:
                continue
            rows.append((
                bank_id,
                row['review'],
                int(row['rating']),
                row['date'],
                row['source'],
                row.get('sentiment_label'),
                row.get('sentiment_score'),
                row.get('identified_theme')
            ))

        query = """
            INSERT INTO reviews (
                bank_id, review, rating, date, source,
                sentiment_label, sentiment_score, identified_theme
            ) VALUES %s;
        """
        execute_values(self.cursor, query, rows)
        self.conn.commit()
        print(f"✅ Inserted {len(rows)} reviews.")

    def close(self):
        self.cursor.close()
        self.conn.close()
        print("🔒 Connection closed.")


if __name__ == "__main__":
    # Load cleaned + analyzed CSV
    df = pd.read_csv("data/thematic_reviews.csv")

    # Connect and insert
    db = PostgresDB(
        dbname="bank_reviews",
        user="postgres",        
        password="password",     
        host="localhost",
        port=5432
    )

    db.create_tables()
    db.insert_banks(df)
    db.insert_reviews(df)
    db.close()
