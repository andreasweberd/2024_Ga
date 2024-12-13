anzahlBilder = 1
pixelHöhe = 352
pixelBreite = 121
farbTiefe = 24

pixelGesamt = pixelHöhe * pixelBreite

speicherPlatzBild = pixelGesamt * farbTiefe

speicherPlatzGesamt = speicherPlatzBild * anzahlBilder / 8

speicherPlatzGesamtInMib = speicherPlatzGesamt / (1024 * 1024)

print (speicherPlatzGesamtInMib, "Mib")