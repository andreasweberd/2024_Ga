def filesize(anzahl, hoehe, breite, farbtiefe):
    i = anzahl * hoehe * breite
    bit = i * farbtiefe
    byte = bit / 8
    mebibyte = (byte/ 1024 / 1024)
    print ('Die Datei ist', mebibyte ,'Mebibyte groß')

#Test 5 Bilder, 1920 Pixel Hoch, 1080 Pixel Breit, Farbtiefe 16
filesize(5,1920,1080,16)