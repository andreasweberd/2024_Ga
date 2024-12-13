anzahlBilder = 1
pixelHöhe = 352
pixelBreite = 121
farbTiefe = 24

pixelGesamt = pixelHöhe * pixelBreite

speicherPlatzBild = pixelGesamt * farbTiefe

speicherPlatzGesamtinByte = speicherPlatzBild * anzahlBilder / 8

speicherPlatzGesamtInMib = speicherPlatzGesamtinByte / (1024 * 1024)

print (speicherPlatzGesamtInMib, "Mib")