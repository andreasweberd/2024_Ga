import sqlite3

connection = sqlite3.connect('lawen_eric/hardwareverwaltung.db')

cursor = connection.cursor()

Suche = input()

sqlQuery = ('select * from Monitor WHERE Name LIKE "%'+Suche+'%" order by Preis asc')

cursor.execute(sqlQuery)

for datensatz in cursor:
    print ('MonitorID: ' + str(datensatz[0]) + ' Name: ' + str(datensatz[1]) + ' Preis: ' + str(datensatz[2])+ ' Größe: ' + str(datensatz[3]))

connection.close()