def ImageSize(a, hpx, bpx, ft):
    ap = hpx * bpx
    g = ap * ft
    G = g * a
    GMiB = G/1024/1024/8, 2
    return GMiB

#Testfälle
if __name__ == "__main__":
    #5 Bilder in Full HD
    print(f"5 Bilder in Full HD Auflösung sind {ImageSize(5, 1080, 1920, 16)} MiB groß.")
    #2 Bilder in HD
    print(f"2 Bilder in HD Auflösung sind {ImageSize(2, 720, 1280, 16)} MiB groß.")
    #1 Bild in 4K Auflösung
    print(f"Ein Bild in 4K Auflösung ist {ImageSize(1, 2160, 3840, 16)} MiB groß.")