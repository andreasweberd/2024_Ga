-- Aufgabe 1
-- a)
CREATE TABLE See (
	SeeNr INTEGER NOT NULL PRIMARY KEY,
	Name TEXT NOT NULL,
	Laenge REAL NOT NULL,
	Breite REAL NOT NULL
);

-- b)
ALTER TABLE See ADD COLUMN Tiefe INTEGER;

-- c)
ALTER TABLE See DROP COLUMN Tiefe;
ALTER TABLE See ADD COLUMN Tiefe REAL;

-- d)
ALTER TABLE See DROP COLUMN Tiefe;

-- e)
DROP TABLE See;

-- Aufgabe 2
-- a)
INSERT INTO Monitor (Name, Preis, Größe) VALUES ('UW3420K',343.50,34.0);

-- b)
UPDATE Monitor SET Preis = Preis*0.95 WHERE Größe = 27.0;

-- c)
UPDATE Monitor SET Name = 'HD2771' WHERE MonitorID = 4;

-- d)
UPDATE Monitor SET Preis = Null WHERE MonitorID = 12;

-- e)
DELETE FROM Monitor WHERE Größe = 17.0;