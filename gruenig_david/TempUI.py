import tkinter as tk
from tkinter import messagebox

# Funktion zur Berechnung der Durchschnittstemperatur
def berechne_durchschnitt():
    try:
        temperatur1 = float(entry1.get())
        temperatur2 = float(entry2.get())
        temperatur3 = float(entry3.get())
        durchschnitt = (temperatur1 + temperatur2 + temperatur3) / 3
        messagebox.showinfo("Durchschnittstemperatur", f"Die Durchschnittstemperatur beträgt: {durchschnitt:.2f}°C")
    except ValueError:
        messagebox.showerror("Fehler", "Bitte geben Sie gültige Temperaturwerte ein.")

# Erstellen des Hauptfensters
root = tk.Tk()
root.title("Durchschnittstemperatur Rechner")

# Erstellen und Platzieren der Eingabefelder und Beschriftungen
label1 = tk.Label(root, text="Geben Sie die erste Temperatur ein:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Geben Sie die zweite Temperatur ein:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Geben Sie die dritte Temperatur ein:")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()

# Erstellen und Platzieren des Berechnungsbuttons
button = tk.Button(root, text="Berechne Durchschnittstemperatur", command=berechne_durchschnitt)
button.pack()

# Starten der GUI-Hauptschleife
root.mainloop()
