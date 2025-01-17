def calculate_transfer_time():
    try:
        mb_size = float(input("Datenmenge (MB): "))
        speed = float(input("Übertragungsrate (Kbit/s): "))

        kbit_size = mb_size * 8192

        seconds = kbit_size / speed
        minutes = seconds / 60

        print(f"\nÜbertragungszeit: {minutes:.2f} Minuten")
        return minutes

    except ValueError:
        print("Fehler: Bitte geben Sie nur Zahlen ein!")
    except ZeroDivisionError:
        print("Fehler: Die Übertragungsrate darf nicht 0 sein!")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")


if __name__ == "__main__":
    calculate_transfer_time()