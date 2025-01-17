def avgTemp():
    count = int(input("wie viele Temperaturen willst du inputten (english *thumbs up*): "))
    totalTemp = 0
    for i in range(count):
        temp = float(input("gib deine Temperatur ein: "))
        totalTemp += temp


    averageTemp = totalTemp / count
    print(f"der Temperatur Durchschnitt ist: {averageTemp}")


avgTemp()