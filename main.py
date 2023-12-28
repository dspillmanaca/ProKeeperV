import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

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

def open_home_mascot():
    global home_mascot_path
    home_mascot_path = filedialog.askopenfilename(title="Open Team Image", filetypes=[("PNG Images", "*.png")])

def open_away_mascot():
    global away_mascot_path
    away_mascot_path = filedialog.askopenfilename(title="Open Team Image", filetypes=[("PNG Images", "*.png")])

def new_game():
    startup.destroy()
    new_game = tk.Tk()
    new_game.title("New Game Setup")
    new_game.geometry("300x575")

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

    gen_q3 = EntryWithPlaceholder(gen_info_grid, "Brownson Arena")
    gen_q3.grid(row=2, column=1)

    gen_label4 = tk.Label(gen_info_grid, text="Up Referee:", font=("Arial", 12))
    gen_label4.grid(row=3, column=0)

    gen_q4 = tk.Entry(gen_info_grid)
    gen_q4.grid(row=3, column=1)

    gen_label5 = tk.Label(gen_info_grid, text="Down Referee:", font=("Arial", 12))
    gen_label5.grid(row=4, column=0)

    gen_q5 = tk.Entry(gen_info_grid)
    gen_q5.grid(row=4, column=1)

    gen_label6 = tk.Label(gen_info_grid, text="Scorekeeper:", font=("Arial", 12))
    gen_label6.grid(row=5, column=0)

    gen_q6 = tk.Entry(gen_info_grid)
    gen_q6.grid(row=5, column=1)

    gen_info_grid.pack(fill='x')

    home_info_label = tk.Label(text="Home Team", font=("Arial", 20))
    home_info_label.pack(padx=5, pady=15)

    home_info_grid = tk.Frame(new_game)
    home_info_grid.columnconfigure(0, weight=1)
    home_info_grid.columnconfigure(1, weight=1)

    home_label1 = tk.Label(home_info_grid, text="Team Name:", font=("Arial", 12))
    home_label1.grid(row=0, column=0)

    home_q1 = EntryWithPlaceholder(home_info_grid, "Central High")
    home_q1.grid(row=0, column=1)

    home_label2 = tk.Label(home_info_grid, text="Mascot:", font=("Arial", 12))
    home_label2.grid(row=1, column=0)

    home_q2 = EntryWithPlaceholder(home_info_grid, "Eagles")
    home_q2.grid(row=1, column=1)

    home_label3 = tk.Label(home_info_grid, text="Letter Code:", font=("Arial", 12))
    home_label3.grid(row=2, column=0)

    home_q3 = EntryWithPlaceholder(home_info_grid, "CHE")
    home_q3.grid(row=2, column=1)

    home_label4 = tk.Label(home_info_grid, text="Upload Logo", font=("Arial", 12))
    home_label4.grid(row=3, column=0)

    home_logo = tk.Button(home_info_grid, text="Upload", font=("Arial", 10), command=open_home_mascot)
    home_logo.grid(row=3, column=1, sticky=tk.W+tk.E, padx=10)

    home_info_grid.pack(fill='x')

    away_info_label = tk.Label(text="Away Team", font=("Arial", 20))
    away_info_label.pack(padx=5, pady=15)

    away_info_grid = tk.Frame(new_game)
    away_info_grid.columnconfigure(0, weight=1)
    away_info_grid.columnconfigure(1, weight=1)

    away_label1 = tk.Label(away_info_grid, text="Team Name:", font=("Arial", 12))
    away_label1.grid(row=0, column=0)

    away_q1 = EntryWithPlaceholder(away_info_grid, "Colorado Mesa")
    away_q1.grid(row=0, column=1)

    away_label2 = tk.Label(away_info_grid, text="Mascot:", font=("Arial", 12))
    away_label2.grid(row=1, column=0)

    away_q2 = EntryWithPlaceholder(away_info_grid, "Mavericks")
    away_q2.grid(row=1, column=1)

    away_label3 = tk.Label(away_info_grid, text="Letter Code:", font=("Arial", 12))
    away_label3.grid(row=2, column=0)

    away_q3 = EntryWithPlaceholder(away_info_grid, "CMM")
    away_q3.grid(row=2, column=1)

    away_label4 = tk.Label(away_info_grid, text="Upload Logo", font=("Arial", 12))
    away_label4.grid(row=3, column=0)

    away_logo = tk.Button(away_info_grid, text="Upload", font=("Arial", 10), command=open_away_mascot)
    away_logo.grid(row=3, column=1, sticky=tk.W+tk.E, padx=10)

    away_info_grid.pack(fill='x')


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