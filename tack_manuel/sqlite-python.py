import sqlite3

oSqliteConnection = sqlite3.connect('tack_manuel/DBs/hardwareverwaltung.db')
oCursor = oSqliteConnection.cursor()
sSql = "SELECT * FROM Monitor ORDER BY Preis ASC;"
oCursor.execute(sSql)
for l in oCursor.fetchall():
    print(f"Name: {l[1]}, Preis: {l[2]}€")
oCursor.close()