import tkinter as tk
from tkinter import messagebox

# Funktion zur Berechnung der Durchschnittstemperatur
def berechne_durchschnitt():
    try:
        temp1 = float(entry_temp1.get())
        temp2 = float(entry_temp2.get())
        temp3 = float(entry_temp3.get())
        durchschnitt = (temp1 + temp2 + temp3) / 3
        messagebox.showinfo("Ergebnis", f"Die Durchschnittstemperatur beträgt: {durchschnitt:.2f} °C")
    except ValueError:
        messagebox.showerror("Fehler", "Bitte gib gültige Zahlen ein!")

# Hauptfenster der Anwendung
root = tk.Tk()
root.title("Durchschnittstemperatur Rechner")

# Label und Eingabefelder für die Temperaturen
label_temp1 = tk.Label(root, text="Temperatur 1:")
label_temp1.grid(row=0, column=0, padx=10, pady=10)
entry_temp1 = tk.Entry(root)
entry_temp1.grid(row=0, column=1, padx=10, pady=10)

label_temp2 = tk.Label(root, text="Temperatur 2:")
label_temp2.grid(row=1, column=0, padx=10, pady=10)
entry_temp2 = tk.Entry(root)
entry_temp2.grid(row=1, column=1, padx=10, pady=10)

label_temp3 = tk.Label(root, text="Temperatur 3:")
label_temp3.grid(row=2, column=0, padx=10, pady=10)
entry_temp3 = tk.Entry(root)
entry_temp3.grid(row=2, column=1, padx=10, pady=10)

# Button zur Berechnung der Durchschnittstemperatur
button_berechnen = tk.Button(root, text="Berechnen", command=berechne_durchschnitt)
button_berechnen.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Hauptfenster ausführen
root.mainloop()
