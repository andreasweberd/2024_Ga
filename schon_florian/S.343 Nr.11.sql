CREATE TABLE See (
    SeeNr INT PRIMARY KEY,
    Name VARCHAR(100),
    Laenge DECIMAL,
    Breite DECIMAL
);

Alter Table See add Tiefe DECIMAL

Alter Table See drop COLUMN Tiefe
Alter Table See add Tiefe Float

Alter Table See drop COLUMN Tiefe

drop Table See