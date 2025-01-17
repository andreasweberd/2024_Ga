def berechneUebertragungszeit():
    print('Bitte geben Sie die Datenmenge in MB an:')
    datenmenge = float(input()) / 8000 #Umrechnung von MB in Kb
    print('Bitte geben Sie die Übertragungsrate in Kb/s an:')
    uebertragungsrate = float(input())
    
    uebertragungszeit = datenmenge / uebertragungsrate
    print('Die Übertragungszeit beträgt ' + str(uebertragungszeit * 60) + 'Minuten')
    
berechneUebertragungszeit()
    