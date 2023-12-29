import tkinter as tk
from tkinter import filedialog
# from PIL import Image, ImageTk
import re


def new_game():
    startup.destroy()
    new_game_setup = tk.Tk()
    new_game_setup.title("New Game Setup")
    new_game_setup.geometry("325x590")

    date_var = tk.StringVar()
    time_var = tk.StringVar()
    location_var = tk.StringVar()
    up_referee_var = tk.StringVar()
    down_referee_var = tk.StringVar()
    scorekeeper_var = tk.StringVar()
    home_name_var = tk.StringVar()
    home_mascot_var = tk.StringVar()
    home_code_var = tk.StringVar()
    home_path_var = tk.StringVar()
    away_name_var = tk.StringVar()
    away_mascot_var = tk.StringVar()
    away_code_var = tk.StringVar()
    away_path_var = tk.StringVar()

    def open_home_mascot():
        home_mascot_path = filedialog.askopenfilename(title="Open Team Image", filetypes=[("PNG Images", "*.png")])
        home_path_var.set(home_mascot_path)

    def open_away_mascot():
        away_mascot_path = filedialog.askopenfilename(title="Open Team Image", filetypes=[("PNG Images", "*.png")])
        away_path_var.set(away_mascot_path)

    def validate_setup():
        errors = []
        if len(date_var.get()) == 0:
            errors.append("Date is empty")
        elif not re.match(r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$', date_var.get()):
            errors.append("Invalid date: "+date_var.get())
        if len(time_var.get()) == 0:
            errors.append("Time is empty")
        elif not re.match(r'^(0[1-9]|1[0-2]):[0-5][0-9]\s(?:AM|PM)$', time_var.get()):
            errors.append("Invalid time: "+time_var.get())
        if len(location_var.get()) == 0:
            errors.append("Location is empty")
        elif not re.match(r'^[\dA-Za-z\'\s\-]+$', location_var.get()):
            errors.append("Invalid characters in Location")
        if len(up_referee_var.get()) == 0:
            errors.append("Up Referee is empty")
        elif not re.match(r'^[A-Za-z\'\s\-]+$', up_referee_var.get()):
            errors.append("Invalid characters in Up Referee")
        if len(down_referee_var.get()) > 0 and not re.match(r'^[A-Za-z\'\s\-]+$', down_referee_var.get()):
            errors.append("Invalid characters in Down Referee")
        if len(scorekeeper_var.get()) == 0:
            errors.append("Scorekeeper is empty")
        elif not re.match(r'^[A-Za-z\'\s\-]+$', scorekeeper_var.get()):
            errors.append("Invalid characters in Scorekeeper")
        if len(home_name_var.get()) == 0:
            errors.append("Home Team Name is empty")
        if len(home_code_var.get()) == 0:
            errors.append("Home Code is empty")
        elif not re.match(r'^[A-Z]{3}$', home_code_var.get()):
            errors.append("Home Code format is invalid: "+home_code_var.get())
        if len(away_name_var.get()) == 0:
            errors.append("Away Team Name is empty")
        if len(away_code_var.get()) == 0:
            errors.append("Away Code is empty")
        elif not re.match(r'^[A-Z]{3}$', away_code_var.get()):
            errors.append("Away Code format is invalid: "+away_code_var.get())
        if not errors:
            print("Positive validation holder")
        else:
            print("Negative validation holder")
            print(errors)

    gen_info_label = tk.Label(new_game_setup, text="General Information", font=("Arial", 20))
    gen_info_label.pack(padx=5, pady=15)

    gen_info_grid = tk.Frame(new_game_setup)
    gen_info_grid.columnconfigure(0, weight=1)
    gen_info_grid.columnconfigure(1, weight=1)

    gen_label1 = tk.Label(gen_info_grid, text="Date: (MM/DD/YYYY)", font=("Arial", 12))
    gen_label1.grid(row=0, column=0)

    gen_q1 = tk.Entry(gen_info_grid, textvariable=date_var)
    gen_q1.grid(row=0, column=1)

    gen_label2 = tk.Label(gen_info_grid, text="Time: (HH:MM AM/PM)", font=("Arial", 12))
    gen_label2.grid(row=1, column=0)

    gen_q2 = tk.Entry(gen_info_grid, textvariable=time_var)
    gen_q2.grid(row=1, column=1)

    gen_label3 = tk.Label(gen_info_grid, text="Location:", font=("Arial", 12))
    gen_label3.grid(row=2, column=0)

    gen_q3 = tk.Entry(gen_info_grid, textvariable=location_var)
    gen_q3.grid(row=2, column=1)

    gen_label4 = tk.Label(gen_info_grid, text="Up Referee:", font=("Arial", 12))
    gen_label4.grid(row=3, column=0)

    gen_q4 = tk.Entry(gen_info_grid, textvariable=up_referee_var)
    gen_q4.grid(row=3, column=1)

    gen_label5 = tk.Label(gen_info_grid, text="Down Referee:", font=("Arial", 12))
    gen_label5.grid(row=4, column=0)

    gen_q5 = tk.Entry(gen_info_grid, textvariable=down_referee_var)
    gen_q5.grid(row=4, column=1)

    gen_label6 = tk.Label(gen_info_grid, text="Scorekeeper:", font=("Arial", 12))
    gen_label6.grid(row=5, column=0)

    gen_q6 = tk.Entry(gen_info_grid, textvariable=scorekeeper_var)
    gen_q6.grid(row=5, column=1)

    gen_info_grid.pack(fill='x')

    home_info_label = tk.Label(new_game_setup, text="Home Team", font=("Arial", 20))
    home_info_label.pack(padx=5, pady=15)

    home_info_grid = tk.Frame(new_game_setup)
    home_info_grid.columnconfigure(0, weight=1)
    home_info_grid.columnconfigure(1, weight=1)

    home_label1 = tk.Label(home_info_grid, text="Team Name:", font=("Arial", 12))
    home_label1.grid(row=0, column=0)

    home_q1 = tk.Entry(home_info_grid, textvariable=home_name_var)
    home_q1.grid(row=0, column=1)

    home_label2 = tk.Label(home_info_grid, text="Mascot:", font=("Arial", 12))
    home_label2.grid(row=1, column=0)

    home_q2 = tk.Entry(home_info_grid, textvariable=home_mascot_var)
    home_q2.grid(row=1, column=1)

    home_label3 = tk.Label(home_info_grid, text="Letter Code: (ABC)", font=("Arial", 12))
    home_label3.grid(row=2, column=0)

    home_q3 = tk.Entry(home_info_grid, textvariable=home_code_var)
    home_q3.grid(row=2, column=1)

    home_label4 = tk.Label(home_info_grid, text="Upload Logo", font=("Arial", 12))
    home_label4.grid(row=3, column=0)

    home_logo = tk.Button(home_info_grid, text="Upload", font=("Arial", 10), command=open_home_mascot)
    home_logo.grid(row=3, column=1, sticky=tk.W+tk.E, padx=10)

    home_info_grid.pack(fill='x')

    away_info_label = tk.Label(new_game_setup, text="Away Team", font=("Arial", 20))
    away_info_label.pack(padx=5, pady=15)

    away_info_grid = tk.Frame(new_game_setup)
    away_info_grid.columnconfigure(0, weight=1)
    away_info_grid.columnconfigure(1, weight=1)

    away_label1 = tk.Label(away_info_grid, text="Team Name:", font=("Arial", 12))
    away_label1.grid(row=0, column=0)

    away_q1 = tk.Entry(away_info_grid, textvariable=away_name_var)
    away_q1.grid(row=0, column=1)

    away_label2 = tk.Label(away_info_grid, text="Mascot:", font=("Arial", 12))
    away_label2.grid(row=1, column=0)

    away_q2 = tk.Entry(away_info_grid, textvariable=away_mascot_var)
    away_q2.grid(row=1, column=1)

    away_label3 = tk.Label(away_info_grid, text="Letter Code: (ABC)", font=("Arial", 12))
    away_label3.grid(row=2, column=0)

    away_q3 = tk.Entry(away_info_grid, textvariable=away_code_var)
    away_q3.grid(row=2, column=1)

    away_label4 = tk.Label(away_info_grid, text="Upload Logo", font=("Arial", 12))
    away_label4.grid(row=3, column=0)

    away_logo = tk.Button(away_info_grid, text="Upload", font=("Arial", 10), command=open_away_mascot)
    away_logo.grid(row=3, column=1, sticky=tk.W+tk.E, padx=10)

    away_info_grid.pack(fill='x')

    setup_next_button = tk.Button(new_game_setup, font=("Arial", 10), text="Next", command=validate_setup)
    setup_next_button.pack(fill='x', padx=10, pady=5)


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
