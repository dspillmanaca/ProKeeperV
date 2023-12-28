import tkinter as tk
from tkinter import filedialog as fidi

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

def new_game():
    startup.destroy()
    new_game_a = tk.Tk()
    new_game_a.title("New Game Setup")
    new_game_a.geometry("300x600")

    gen_info_label = tk.Label(text="General Information", font=("Arial", 20))
    gen_info_label.pack(padx=5, pady=15)

    gen_info_grid = tk.Frame(new_game)
    gen_info_grid.columnconfigure(0, weight=1)
    gen_info_grid.columnconfigure(1, weight=1)

    gen_label1 = tk.Label(gen_info_grid, text="Date:", font=("Arial", 12))
    gen_label1.grid(row=0, column=0)

    gen_q1 = EntryWithPlaceholder(gen_info_grid, "MM/DD/YYYY")
    gen_q1.grid(row=0, column=1)

    gen_label2 = tk.Label(gen_info_grid, text="Time:", font=("Arial", 12))
    gen_label2.grid(row=1, column=0)

    gen_q2 = EntryWithPlaceholder(gen_info_grid, "HH:MM AM/PM")
    gen_q2.grid(row=1, column=1)

    gen_label3 = tk.Label(gen_info_grid, text="Location:", font=("Arial", 12))
    gen_label3.grid(row=2, column=0)

    gen_q3 = tk.Entry(gen_info_grid)
    gen_q3.grid(row=2, column=1)

    gen_label4 = tk.Label(gen_info_grid, text="Up Referee:", font=("Arial", 12))
    gen_label4.grid(row=3, column=0)

    gen_q4 = tk.Entry(gen_info_grid)
    gen_q4.grid(row=3, column=1)

    gen_label5 = tk.Label(gen_info_grid, text="Down Referee:", font=("Arial", 12))
    gen_label5.grid(row=4, column=0)

    gen_q5 = tk.Entry(gen_info_grid)
    gen_q5.grid(row=4, column=1)

    gen_info_grid.pack(fill='x')

    home_info_label = tk.Label(text="Home Team", font=("Arial", 20))
    home_info_label.pack(padx=5, pady=15)

    home_info_grid = tk.Frame(new_game)
    home_info_grid.columnconfigure(0, weight=1)
    home_info_grid.columnconfigure(1, weight=1)

    home_label1 = tk.Label(home_info_grid, text="Date:", font=("Arial", 12))
    home_label1.grid(row=0, column=0)

    home_q1 = EntryWithPlaceholder(home_info_grid, "MM/DD/YYYY")
    home_q1.grid(row=0, column=1)

    home_label2 = tk.Label(home_info_grid, text="Time:", font=("Arial", 12))
    home_label2.grid(row=1, column=0)

    home_q2 = EntryWithPlaceholder(home_info_grid, "HH:MM AM/PM")
    gen_q2.grid(row=1, column=1)

    home_label3 = tk.Label(home_info_grid, text="Location:", font=("Arial", 12))
    home_label3.grid(row=2, column=0)

    home_q3 = tk.Entry(home_info_grid)
    home_q3.grid(row=2, column=1)

    gen_label4 = tk.Label(home_info_grid, text="Up Referee:", font=("Arial", 12))
    gen_label4.grid(row=3, column=0)

    gen_q4 = tk.Entry(home_info_grid)
    gen_q4.grid(row=3, column=1)

def load_game():
    print("Holder")

def startup_window():
    global startup
    startup = tk.Tk()
    startup.title("PKV")
    startup.geometry("300x250")

    startup_label = tk.Label(text="ProKeeper for Volleyball", font=("Arial", 18))
    startup_label.pack(padx=5, pady=25)

    new_game_button = tk.Button(startup, text="New Game", font=("Arial", 14), command=new_game)
    new_game_button.pack(padx=5, pady=10)

    load_game_button = tk.Button(startup, text="Load Game", font=("Arial", 14), command=load_game)
    load_game_button.pack(padx=5, pady=10)

    startup.mainloop()

startup_window()