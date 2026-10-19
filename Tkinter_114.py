
import tkinter as tk
from tkinter import messagebox

def hasil_prediksi():
    hasil_label.config(text="Hasil Prediksi: TeknologiInformasi")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x650")
root.resizable(False, False)

# Judul aplikasi
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold")
)
judul.pack(pady=20)

# Input 10 nilai mata pelajaran
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

entries = []

for i in range(10):
    baris = tk.Frame(frame_input)
    baris.pack(fill="x", pady=5)

    label = tk.Label(
        baris,
        text=f"Nilai Mata Pelajaran {i + 1}",
        width=25,
        anchor="w"
    )
    label.pack(side="left", padx=5)

    entry = tk.Entry(baris, width=15)
    entry.pack(side="left", padx=5)

    entries.append(entry)

# Tombol prediksi
tombol = tk.Button(
    root,
    text="Hasil Prediksi",
    font=("Arial", 11, "bold"),
    command=hasil_prediksi,
    bg="#2E7D32",
    fg="white",
    padx=15,
    pady=8
)
tombol.pack(pady=20)

# Label hasil prediksi
hasil_label = tk.Label(
    root,
    text="Hasil Prediksi akan muncul di sini",
    font=("Arial", 12, "bold"),
    fg="blue",
    wraplength=450
)
hasil_label.pack(pady=10)

root.mainloop()
