import sqlite3
import pandas as pd

conn = sqlite3.connect('database/cultural.db')

# Convert CSVs to SQLite tables
pd.read_csv('data/art_forms.csv').to_sql('art_forms', conn, if_exists='replace', index=False)
pd.read_csv('data/cultural_sites.csv').to_sql('cultural_sites', conn, if_exists='replace', index=False)
pd.read_csv('data/seasonal_trends.csv').to_sql('seasonal_trends', conn, if_exists='replace', index=False)
pd.read_csv('data/untouched_regions.csv').to_sql('untouched_regions', conn, if_exists='replace', index=False)

print("✅ SQLite database created successfully!")