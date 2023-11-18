import tkinter as tk
from tkinter import simpledialog, messagebox, ttk


class CountIT:
    def __init__(self, master):
        self.master = master
        self.master.title("CountIT")

        self.master.configure(bg='#1e1e1e')  # ciemne tło
        self.master.tk_setPalette(background='#1e1e1e', foreground='#c1c1c1')  # jasny tekst

        self.food_database = {
            "jabłko": 52,
            "banan": 96,
            "chleb": 265,
            "uran": 9898292745,
            "kot": 2137
        }

        self.activity_database = {
            "chodzenie": 3.8,
            "bieganie": 9.8,
            "rower": 7.4,
            "seks": 69.69,
            "spanie": 0.1
        }

        self.total_calories_consumed = 0
        self.total_calories_burned = 0

        # Create buttons
        self.add_food_btn = tk.Button(master, text="Dodaj pokarm", command=self.add_food)
        self.add_food_btn.pack()

        self.add_activity_btn = tk.Button(master, text="Dodaj aktywność", command=self.add_activity)
        self.add_activity_btn.pack()

        self.show_balance_btn = tk.Button(master, text="Pokaż bilans kaloryczny", command=self.show_balance)
        self.show_balance_btn.pack()

    def add_food(self):
        food = simpledialog.askstring("Dodaj pokarm", "Podaj nazwę pokarmu:")
        grams = simpledialog.askfloat("Dodaj pokarm", "Ile gramów tego pokarmu spożyłeś?")
        if food in self.food_database:
            calories = (self.food_database[food] * grams) / 100
            self.total_calories_consumed += calories
            messagebox.showinfo("Dodano kalorie", f"Dodałeś {calories} kalorii spożywając {grams}g {food}.")
        else:
            messagebox.showerror("Błąd", "Przepraszamy, tego produktu nie ma w naszej bazie.")

    def add_activity(self):
        activity = simpledialog.askstring("Dodaj aktywność", "Podaj nazwę aktywności:")
        minutes = simpledialog.askfloat("Dodaj aktywność", "Ile minut trwała ta aktywność?")
        if activity in self.activity_database:
            calories_burned = self.activity_database[activity] * minutes
            self.total_calories_burned += calories_burned
            messagebox.showinfo("Dodano aktywność",
                                f"Spaliłeś {calories_burned} kalorii wykonując {activity} przez {minutes} minut.")
        else:
            messagebox.showerror("Błąd", "Przepraszamy, tej aktywności nie ma w naszej bazie.")

    def show_balance(self):
        net_calories = self.total_calories_consumed - self.total_calories_burned
        messagebox.showinfo("Bilans Kaloryczny",
                            f"Spożyte kalorie: {self.total_calories_consumed}\n"
                            f"Spalone kalorie: {self.total_calories_burned}\n"
                            f"Netto kalorie: {net_calories}")


if __name__ == "__main__":
    root = tk.Tk()

    # Ustawienie rozmiaru okna
    root.geometry("300x200")

    style = ttk.Style()
    style.configure('TFrame', background='pink')

    # Dodanie ramki z odpowiednimi kolorami
    main_frame = ttk.Frame(root, padding="10", style="TFrame")
    main_frame.pack(padx=10, pady=10, expand=True, fill="both")

    label = ttk.Label(main_frame, text="Count IT", font=("Arial", 20))
    label.pack(pady=10)

    app = CountIT(root)
    root.mainloop()
