import sqlite3

dbfile = r'C:\Users\Ivan\Documents\schule\LF5\sql\hardwareverwaltung.db'
con = sqlite3.connect(dbfile)

cur = con.cursor()

search = input('Welsches monitor suchen sie: ')

cur.execute(f'SELECT Name, Preis from Monitor where Name LIKE "%{search.upper()}%" ORDER BY Preis asc')
rows = cur.fetchall()

print("All monitor records:")
for row in rows:
    print(f'Name: {row[0]} - Preis: {row[1]}€')

con.close()

