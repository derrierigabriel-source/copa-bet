import duckdb as db

con = db.connect("data/db/matches_raw.db")

con.execute("""CREATE OR REPLACE TABLE matches_raw AS SELECT * FROM read_csv_auto('data/raw/E0.csv')""")

con.close()
print("Ingestão concluída.")
