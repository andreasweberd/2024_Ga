anzahlBilder = 4
pixelHöhe = 1024
pixelBreite = 1024
farbTiefe = 16

pixelGesamt = pixelHöhe * pixelBreite

speicherPlatzBild = pixelGesamt * farbTiefe

speicherPlatzGesamt = speicherPlatzBild * anzahlBilder

speicherPlatzGesamtInMib = speicherPlatzGesamt / (1024 * 1024)

print (speicherPlatzGesamtInMib, "Mib")