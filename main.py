import tkinter as tk

def new_game():
    startup.destroy()
    new_game_a = tk.Tk()
    new_game_a.title("New Game Setup")
    new_game_a.geometry("300x600")

    gen_info_label = tk.Label(text="General Information", font=("Arial", 20))
    gen_info_label.pack(padx=5, pady=15)

    gen_info_grid = tk.Frame(new_game_a)
    gen_info_grid.columnconfigure(0, weight=1)
    gen_info_grid.columnconfigure(1, weight=1)

    gen_label1 = tk.Label(gen_info_grid, text="Date:", font=("Arial", 14))
    gen_label1.grid(row=0, column=0)

    gen_q1 = tk.Entry(gen_info_grid,)
    gen_q1.grid(row=0, column=1)

    gen_info_grid.pack(fill='x')

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