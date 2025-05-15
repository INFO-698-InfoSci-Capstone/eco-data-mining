import sqlite3

db_path = r"C:\Users\VikRuhil\Desktop\MS DS\Capstone\Eco Data Mining\eco-data-mining\data-discovery-tool\data\eco.db"


# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Query tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

cursor.execute("PRAGMA table_info('field_stations');")
print(cursor.fetchall())

cursor.execute("PRAGMA table_info('journals');")
print(cursor.fetchall())

cursor.execute("PRAGMA table_info('journal_nlp');")
print(cursor.fetchall())

cursor.execute("PRAGMA foreign_key_list('journals');")
print(cursor.fetchall())

cursor.execute("PRAGMA foreign_key_list('journal_nlp');")
print(cursor.fetchall())

cursor.execute("SELECT COUNT(*) FROM field_stations;")
print(f"Field Stations: {cursor.fetchone()[0]}")

cursor.execute("SELECT COUNT(*) FROM journals;")
print(f"Journals: {cursor.fetchone()[0]}")

cursor.execute("SELECT COUNT(*) FROM journal_nlp;")
print(f"Journal NLP Entries: {cursor.fetchone()[0]}")


print(f"Tables in {db_path}:")
for table in tables:
    print(f" - {table[0]}")

conn.close()
