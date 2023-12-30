import tkinter as tk
from tkinter import filedialog
# from PIL import Image, ImageTk
import re
import json


def new_game_():
    startup.destroy()
    basic_setup = tk.Tk()
    basic_setup.title("New Game Setup")
#    basic_setup.geometry("1x1")
    new_game_setup = tk.Frame()

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
    home_coach_var = tk.StringVar()
    home_acoach_var = tk.StringVar()
    home_cap_var = tk.StringVar()
    home_cap_num_var = tk.StringVar()
    home_acap_var = tk.StringVar()
    home_acap_num_var = tk.StringVar()
    home_lib_e_var = tk.StringVar()
    home_lib_e_num_var = tk.StringVar()
    home_lib_f_var = tk.StringVar()
    home_lib_f_num_var = tk.StringVar()
    home_ps_g_var = tk.StringVar()
    home_ps_g_num_var = tk.StringVar()
    home_ps_h_var = tk.StringVar()
    home_ps_h_num_var = tk.StringVar()
    home_ps_i_var = tk.StringVar()
    home_ps_i_num_var = tk.StringVar()
    home_ps_j_var = tk.StringVar()
    home_ps_j_num_var = tk.StringVar()
    home_ps_k_var = tk.StringVar()
    home_ps_k_num_var = tk.StringVar()
    home_ps_l_var = tk.StringVar()
    home_ps_l_num_var = tk.StringVar()
    home_ps_m_var = tk.StringVar()
    home_ps_m_num_var = tk.StringVar()
    home_ps_n_var = tk.StringVar()
    home_ps_n_num_var = tk.StringVar()
    home_ps_o_var = tk.StringVar()
    home_ps_o_num_var = tk.StringVar()
    home_ps_p_var = tk.StringVar()
    home_ps_p_num_var = tk.StringVar()
    home_ps_q_var = tk.StringVar()
    home_ps_q_num_var = tk.StringVar()
    home_ps_r_var = tk.StringVar()
    home_ps_r_num_var = tk.StringVar()
    home_ps_s_var = tk.StringVar()
    home_ps_s_num_var = tk.StringVar()
    home_ps_t_var = tk.StringVar()
    home_ps_t_num_var = tk.StringVar()
    home_ps_u_var = tk.StringVar()
    home_ps_u_num_var = tk.StringVar()
    home_ps_v_var = tk.StringVar()
    home_ps_v_num_var = tk.StringVar()
    home_ps_w_var = tk.StringVar()
    home_ps_w_num_var = tk.StringVar()
    home_ps_x_var = tk.StringVar()
    home_ps_x_num_var = tk.StringVar()
    home_ps_y_var = tk.StringVar()
    home_ps_y_num_var = tk.StringVar()
    home_ps_z_var = tk.StringVar()
    home_ps_z_num_var = tk.StringVar()
    away_coach_var = tk.StringVar()
    away_acoach_var = tk.StringVar()
    away_cap_var = tk.StringVar()
    away_cap_num_var = tk.StringVar()
    away_acap_var = tk.StringVar()
    away_acap_num_var = tk.StringVar()
    away_lib_e_var = tk.StringVar()
    away_lib_e_num_var = tk.StringVar()
    away_lib_f_var = tk.StringVar()
    away_lib_f_num_var = tk.StringVar()
    away_ps_g_var = tk.StringVar()
    away_ps_g_num_var = tk.StringVar()
    away_ps_h_var = tk.StringVar()
    away_ps_h_num_var = tk.StringVar()
    away_ps_i_var = tk.StringVar()
    away_ps_i_num_var = tk.StringVar()
    away_ps_j_var = tk.StringVar()
    away_ps_j_num_var = tk.StringVar()
    away_ps_k_var = tk.StringVar()
    away_ps_k_num_var = tk.StringVar()
    away_ps_l_var = tk.StringVar()
    away_ps_l_num_var = tk.StringVar()
    away_ps_m_var = tk.StringVar()
    away_ps_m_num_var = tk.StringVar()
    away_ps_n_var = tk.StringVar()
    away_ps_n_num_var = tk.StringVar()
    away_ps_o_var = tk.StringVar()
    away_ps_o_num_var = tk.StringVar()
    away_ps_p_var = tk.StringVar()
    away_ps_p_num_var = tk.StringVar()
    away_ps_q_var = tk.StringVar()
    away_ps_q_num_var = tk.StringVar()
    away_ps_r_var = tk.StringVar()
    away_ps_r_num_var = tk.StringVar()
    away_ps_s_var = tk.StringVar()
    away_ps_s_num_var = tk.StringVar()
    away_ps_t_var = tk.StringVar()
    away_ps_t_num_var = tk.StringVar()
    away_ps_u_var = tk.StringVar()
    away_ps_u_num_var = tk.StringVar()
    away_ps_v_var = tk.StringVar()
    away_ps_v_num_var = tk.StringVar()
    away_ps_w_var = tk.StringVar()
    away_ps_w_num_var = tk.StringVar()
    away_ps_x_var = tk.StringVar()
    away_ps_x_num_var = tk.StringVar()
    away_ps_y_var = tk.StringVar()
    away_ps_y_num_var = tk.StringVar()
    away_ps_z_var = tk.StringVar()
    away_ps_z_num_var = tk.StringVar()

    def open_home_mascot():
        home_mascot_path = filedialog.askopenfilename(title="Open Team Image", filetypes=[("PNG Images", "*.png")])
        home_path_var.set(home_mascot_path)

    def open_away_mascot():
#         away_mascot_path = filedialog.askopenfilename(title="Open Team Image", filetypes=[("PNG Images", "*.png")])
#         away_path_var.set(away_mascot_path)
#
#     def save_home_roster():
        home_roster = {
            "Co": home_coach_var.get(),
            "ACo": home_acoach_var.get(),
            "Ca": home_cap_var.get(),
            "CaNum": home_cap_num_var.get(),
            "ACa": home_acap_var.get(),
            "ACaNum": home_acap_num_var.get(),
            "LE": home_lib_e_var.get(),
            "LENum": home_lib_e_num_var.get(),
            "LF": home_lib_f_var.get(),
            "LFNum": home_lib_f_num_var.get(),
            "PSG": home_ps_g_var.get(),
            "PSGNum": home_ps_g_num_var.get(),
            "PSH": home_ps_h_var.get(),
            "PSHNum": home_ps_h_num_var.get(),
            "PSI": home_ps_i_var.get(),
            "PSINum": home_ps_i_num_var.get(),
            "PSJ": home_ps_j_var.get(),
            "PSJNum": home_ps_j_num_var.get(),
            "PSK": home_ps_k_var.get(),
            "PSKNum": home_ps_k_num_var.get(),
            "PSL": home_ps_l_var.get(),
            "PSLNum": home_ps_l_num_var.get(),
            "PSM": home_ps_m_var.get(),
            "PSMNum": home_ps_m_num_var.get(),
            "PSN": home_ps_n_var.get(),
            "PSNNum": home_ps_n_num_var.get(),
            "PSO": home_ps_o_var.get(),
            "PSONum": home_ps_o_num_var.get(),
            "PSP": home_ps_p_var.get(),
            "PSPNum": home_ps_p_num_var.get(),
            "PSQ": home_ps_q_var.get(),
            "PSQNum": home_ps_q_num_var.get(),
            "PSR": home_ps_r_var.get(),
            "PSRNum": home_ps_r_num_var.get(),
            "PSS": home_ps_s_var.get(),
            "PSSNum": home_ps_s_num_var.get(),
            "PST": home_ps_t_var.get(),
            "PSTNum": home_ps_t_num_var.get(),
            "PSU": home_ps_u_var.get(),
            "PSUNum": home_ps_u_num_var.get(),
            "PSV": home_ps_v_var.get(),
            "PSVNum": home_ps_v_num_var.get(),
            "PSW": home_ps_w_var.get(),
            "PSWNum": home_ps_w_num_var.get(),
            "PSX": home_ps_x_var.get(),
            "PSXNum": home_ps_x_num_var.get(),
            "PSY": home_ps_y_var.get(),
            "PSYNum": home_ps_y_num_var.get(),
            "PSZ": home_ps_z_var.get(),
            "PSZNum": home_ps_z_num_var.get(),
        }
        home_roster_writer = json.dumps(home_roster)
        with open(filedialog.asksaveasfilename(initialfile=f"{home_name_var.get()}.rostr", title="Save Roster", filetypes=[("ProKeeper Volleyball Team Roster", "*.rostr")]), 'w') as file:
            file.write(home_roster_writer)


    def commit_setup_data():
        basic_data = {
            "Date": date_var.get(),
            "Time": time_var.get(),
            "Location": location_var.get(),
            "Up Referee": up_referee_var.get(),
            "Down Referee": down_referee_var.get(),
            "Scorekeeper": scorekeeper_var.get(),
            "Home Team Name": home_name_var.get(),
            "Home Team Mascot": home_mascot_var.get(),
            "Home Team Code": home_code_var.get(),
            "Home Team Logo Path": home_path_var.get(),
            "Away Team Name": away_name_var.get(),
            "Away Team Mascot": away_mascot_var.get(),
            "Away Team Code": away_code_var.get(),
            "Away Team Logo Path": away_path_var.get(),
        }

        json_writer = json.dumps(basic_data)
        with open(filedialog.asksaveasfilename(initialfile=f"""{basic_data['Date'].replace('/', '-')}
        _{basic_data['Away Team Code']}_at_{basic_data['Home Team Code']}
        .json""", title="Save Game", filetypes=[("ProKeeper Volleyball Game", "*.pkvgame")]), 'w') as file:
            file.write(json_writer)

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
        if errors:
            tk.messagebox.showerror("Validation Error", "\n".join(errors))
        else:
            if len(down_referee_var.get()) == 0:
                down_referee_var.set("N/A")
            if len(home_mascot_var.get()) == 0:
                home_mascot_var.set("N/A")
            if len(home_path_var.get()) == 0:
                home_path_var.set("N/A")
            if len(away_mascot_var.get()) == 0:
                away_mascot_var.set("N/A")
            if len(away_path_var.get()) == 0:
                away_path_var.set("N/A")
            commit_setup_data()

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

    new_game_setup.pack(side=tk.RIGHT, padx=30)

    home_roster_frame = tk.Frame(basic_setup)

    home_roster_label = tk.Label(home_roster_frame, text="Home Team Roster", font=("Arial", 20))
    home_roster_label.pack(padx=5, pady=10)

    home_roster_grid = tk.Frame(home_roster_frame)
    home_roster_grid.columnconfigure(0, weight=2)
    home_roster_grid.columnconfigure(1, weight=2)
    home_roster_grid.columnconfigure(2, weight=1)

    home_coach_label = tk.Label(home_roster_grid, text="Coach:", font=("Arial", 12))
    home_coach_label.grid(column=0, row=0)

    home_coach_entry = tk.Entry(home_roster_grid, textvariable=home_coach_var)
    home_coach_entry.grid(column=1, row=0)

    home_acoach_label = tk.Label(home_roster_grid, text="Ast. Coach:", font=("Arial", 12))
    home_acoach_label.grid(column=0, row=1)

    home_acoach_entry = tk.Entry(home_roster_grid, textvariable=home_acoach_var)
    home_acoach_entry.grid(column=1, row=1)

    home_cap_label = tk.Label(home_roster_grid, text="Captain:", font=("Arial", 12))
    home_cap_label.grid(column=0, row=2)

    home_cap_entry = tk.Entry(home_roster_grid, textvariable=home_cap_var)
    home_cap_entry.grid(column=1, row=2)

    home_cap_num_entry = tk.Entry(home_roster_grid, textvariable=home_cap_num_var, width=3)
    home_cap_num_entry.grid(column=2, row=2)

    home_acap_label = tk.Label(home_roster_grid, text="Ast. Captain:", font=("Arial", 12))
    home_acap_label.grid(column=0, row=3)

    home_acap_entry = tk.Entry(home_roster_grid, textvariable=home_acap_var)
    home_acap_entry.grid(column=1, row=3)

    home_acap_num_entry = tk.Entry(home_roster_grid, textvariable=home_acap_num_var, width=3)
    home_acap_num_entry.grid(column=2, row=3)

    home_lib_e_label = tk.Label(home_roster_grid, text="Libero:", font=("Arial", 12))
    home_lib_e_label.grid(column=0, row=4)

    home_lib_e_entry = tk.Entry(home_roster_grid, textvariable=home_lib_e_var)
    home_lib_e_entry.grid(column=1, row=4)

    home_lib_e_num_entry = tk.Entry(home_roster_grid, textvariable=home_lib_e_num_var, width=3)
    home_lib_e_num_entry.grid(column=2, row=4)

    home_lib_f_label = tk.Label(home_roster_grid, text="Libero:", font=("Arial", 12))
    home_lib_f_label.grid(column=0, row=5)

    home_lib_f_entry = tk.Entry(home_roster_grid, textvariable=home_lib_f_var)
    home_lib_f_entry.grid(column=1, row=5)

    home_lib_f_num_entry = tk.Entry(home_roster_grid, textvariable=home_lib_f_num_var, width=3)
    home_lib_f_num_entry.grid(column=2, row=5)

    home_ps_g_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_g_label.grid(column=0, row=6)

    home_ps_g_label = tk.Entry(home_roster_grid, textvariable=home_ps_g_var)
    home_ps_g_label.grid(column=1, row=6)

    home_ps_g_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_g_num_var, width=3)
    home_ps_g_num_entry.grid(column=2, row=6)

    home_ps_h_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_h_label.grid(column=0, row=7)

    home_ps_h_label = tk.Entry(home_roster_grid, textvariable=home_ps_h_var)
    home_ps_h_label.grid(column=1, row=7)

    home_ps_h_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_h_num_var, width=3)
    home_ps_h_num_entry.grid(column=2, row=7)

    home_ps_i_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_i_label.grid(column=0, row=8)

    home_ps_i_label = tk.Entry(home_roster_grid, textvariable=home_ps_i_var)
    home_ps_i_label.grid(column=1, row=8)

    home_ps_i_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_i_num_var, width=3)
    home_ps_i_num_entry.grid(column=2, row=8)

    home_ps_j_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_j_label.grid(column=0, row=9)

    home_ps_j_label = tk.Entry(home_roster_grid, textvariable=home_ps_j_var)
    home_ps_j_label.grid(column=1, row=9)

    home_ps_j_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_j_num_var, width=3)
    home_ps_j_num_entry.grid(column=2, row=9)

    home_ps_k_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_k_label.grid(column=0, row=10)

    home_ps_k_label = tk.Entry(home_roster_grid, textvariable=home_ps_k_var)
    home_ps_k_label.grid(column=1, row=10)

    home_ps_k_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_k_num_var, width=3)
    home_ps_k_num_entry.grid(column=2, row=10)

    home_ps_l_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_l_label.grid(column=0, row=11)

    home_ps_l_label = tk.Entry(home_roster_grid, textvariable=home_ps_l_var)
    home_ps_l_label.grid(column=1, row=11)

    home_ps_l_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_l_num_var, width=3)
    home_ps_l_num_entry.grid(column=2, row=11)

    home_ps_m_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_m_label.grid(column=0, row=12)

    home_ps_m_label = tk.Entry(home_roster_grid, textvariable=home_ps_m_var)
    home_ps_m_label.grid(column=1, row=12)

    home_ps_m_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_m_num_var, width=3)
    home_ps_m_num_entry.grid(column=2, row=12)

    home_ps_n_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_n_label.grid(column=0, row=13)

    home_ps_n_label = tk.Entry(home_roster_grid, textvariable=home_ps_n_var)
    home_ps_n_label.grid(column=1, row=13)

    home_ps_n_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_n_num_var, width=3)
    home_ps_n_num_entry.grid(column=2, row=13)

    home_ps_o_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_o_label.grid(column=0, row=14)

    home_ps_o_label = tk.Entry(home_roster_grid, textvariable=home_ps_o_var)
    home_ps_o_label.grid(column=1, row=14)

    home_ps_o_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_o_num_var, width=3)
    home_ps_o_num_entry.grid(column=2, row=14)

    home_ps_p_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_p_label.grid(column=0, row=15)

    home_ps_p_label = tk.Entry(home_roster_grid, textvariable=home_ps_p_var)
    home_ps_p_label.grid(column=1, row=15)

    home_ps_p_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_p_num_var, width=3)
    home_ps_p_num_entry.grid(column=2, row=15)

    home_ps_q_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_q_label.grid(column=0, row=16)

    home_ps_q_label = tk.Entry(home_roster_grid, textvariable=home_ps_q_var)
    home_ps_q_label.grid(column=1, row=16)

    home_ps_q_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_q_num_var, width=3)
    home_ps_q_num_entry.grid(column=2, row=16)

    home_ps_r_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_r_label.grid(column=0, row=17)

    home_ps_r_label = tk.Entry(home_roster_grid, textvariable=home_ps_r_var)
    home_ps_r_label.grid(column=1, row=17)

    home_ps_r_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_r_num_var, width=3)
    home_ps_r_num_entry.grid(column=2, row=17)

    home_ps_s_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_s_label.grid(column=0, row=18)

    home_ps_s_label = tk.Entry(home_roster_grid, textvariable=home_ps_s_var)
    home_ps_s_label.grid(column=1, row=18)

    home_ps_s_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_s_num_var, width=3)
    home_ps_s_num_entry.grid(column=2, row=18)

    home_ps_t_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_t_label.grid(column=0, row=19)

    home_ps_t_label = tk.Entry(home_roster_grid, textvariable=home_ps_t_var)
    home_ps_t_label.grid(column=1, row=19)

    home_ps_t_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_t_num_var, width=3)
    home_ps_t_num_entry.grid(column=2, row=19)

    home_ps_u_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_u_label.grid(column=0, row=20)

    home_ps_u_label = tk.Entry(home_roster_grid, textvariable=home_ps_u_var)
    home_ps_u_label.grid(column=1, row=20)

    home_ps_u_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_u_num_var, width=3)
    home_ps_u_num_entry.grid(column=2, row=20)

    home_ps_v_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_v_label.grid(column=0, row=21)

    home_ps_v_label = tk.Entry(home_roster_grid, textvariable=home_ps_v_var)
    home_ps_v_label.grid(column=1, row=21)

    home_ps_v_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_v_num_var, width=3)
    home_ps_v_num_entry.grid(column=2, row=21)

    home_ps_w_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_w_label.grid(column=0, row=22)

    home_ps_w_label = tk.Entry(home_roster_grid, textvariable=home_ps_w_var)
    home_ps_w_label.grid(column=1, row=22)

    home_ps_w_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_w_num_var, width=3)
    home_ps_w_num_entry.grid(column=2, row=22)

    home_ps_x_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_x_label.grid(column=0, row=23)

    home_ps_x_label = tk.Entry(home_roster_grid, textvariable=home_ps_x_var)
    home_ps_x_label.grid(column=1, row=23)

    home_ps_x_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_x_num_var, width=3)
    home_ps_x_num_entry.grid(column=2, row=23)

    home_ps_y_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_y_label.grid(column=0, row=24)

    home_ps_y_label = tk.Entry(home_roster_grid, textvariable=home_ps_y_var)
    home_ps_y_label.grid(column=1, row=24)

    home_ps_y_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_y_num_var, width=3)
    home_ps_y_num_entry.grid(column=2, row=24)

    home_ps_z_label = tk.Label(home_roster_grid, text="Player:", font=("Arial", 12))
    home_ps_z_label.grid(column=0, row=25)

    home_ps_z_label = tk.Entry(home_roster_grid, textvariable=home_ps_z_var)
    home_ps_z_label.grid(column=1, row=25)

    home_ps_z_num_entry = tk.Entry(home_roster_grid, textvariable=home_ps_z_num_var, width=3)
    home_ps_z_num_entry.grid(column=2, row=25)

    home_roster_grid.pack()
    home_roster_frame.pack(side=tk.LEFT, padx=100)

    away_roster_frame = tk.Frame(basic_setup)

    away_roster_label = tk.Label(away_roster_frame, text="Away Team Roster", font=("Arial", 20))
    away_roster_label.pack(padx=5, pady=10)

    away_roster_grid = tk.Frame(away_roster_frame)
    away_roster_grid.columnconfigure(0, weight=2)
    away_roster_grid.columnconfigure(1, weight=2)
    away_roster_grid.columnconfigure(2, weight=1)

    away_coach_label = tk.Label(away_roster_grid, text="Coach:", font=("Arial", 12))
    away_coach_label.grid(column=0, row=0)

    away_coach_entry = tk.Entry(away_roster_grid, textvariable=away_coach_var)
    away_coach_entry.grid(column=1, row=0)

    away_acoach_label = tk.Label(away_roster_grid, text="Ast. Coach:", font=("Arial", 12))
    away_acoach_label.grid(column=0, row=1)

    away_acoach_entry = tk.Entry(away_roster_grid, textvariable=away_acoach_var)
    away_acoach_entry.grid(column=1, row=1)

    away_cap_label = tk.Label(away_roster_grid, text="Captain:", font=("Arial", 12))
    away_cap_label.grid(column=0, row=2)

    away_cap_entry = tk.Entry(away_roster_grid, textvariable=away_cap_var)
    away_cap_entry.grid(column=1, row=2)

    away_cap_num_entry = tk.Entry(away_roster_grid, textvariable=away_cap_num_var, width=3)
    away_cap_num_entry.grid(column=2, row=2)

    away_acap_label = tk.Label(away_roster_grid, text="Ast. Captain:", font=("Arial", 12))
    away_acap_label.grid(column=0, row=3)

    away_acap_entry = tk.Entry(away_roster_grid, textvariable=away_acap_var)
    away_acap_entry.grid(column=1, row=3)

    away_acap_num_entry = tk.Entry(away_roster_grid, textvariable=away_acap_num_var, width=3)
    away_acap_num_entry.grid(column=2, row=3)

    away_lib_e_label = tk.Label(away_roster_grid, text="Libero:", font=("Arial", 12))
    away_lib_e_label.grid(column=0, row=4)

    away_lib_e_entry = tk.Entry(away_roster_grid, textvariable=away_lib_e_var)
    away_lib_e_entry.grid(column=1, row=4)

    away_lib_e_num_entry = tk.Entry(away_roster_grid, textvariable=away_lib_e_num_var, width=3)
    away_lib_e_num_entry.grid(column=2, row=4)

    away_lib_f_label = tk.Label(away_roster_grid, text="Libero:", font=("Arial", 12))
    away_lib_f_label.grid(column=0, row=5)

    away_lib_f_entry = tk.Entry(away_roster_grid, textvariable=away_lib_f_var)
    away_lib_f_entry.grid(column=1, row=5)

    away_lib_f_num_entry = tk.Entry(away_roster_grid, textvariable=away_lib_f_num_var, width=3)
    away_lib_f_num_entry.grid(column=2, row=5)

    away_ps_g_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_g_label.grid(column=0, row=6)

    away_ps_g_label = tk.Entry(away_roster_grid, textvariable=away_ps_g_var)
    away_ps_g_label.grid(column=1, row=6)

    away_ps_g_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_g_num_var, width=3)
    away_ps_g_num_entry.grid(column=2, row=6)

    away_ps_h_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_h_label.grid(column=0, row=7)

    away_ps_h_label = tk.Entry(away_roster_grid, textvariable=away_ps_h_var)
    away_ps_h_label.grid(column=1, row=7)

    away_ps_h_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_h_num_var, width=3)
    away_ps_h_num_entry.grid(column=2, row=7)

    away_ps_i_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_i_label.grid(column=0, row=8)

    away_ps_i_label = tk.Entry(away_roster_grid, textvariable=away_ps_i_var)
    away_ps_i_label.grid(column=1, row=8)

    away_ps_i_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_i_num_var, width=3)
    away_ps_i_num_entry.grid(column=2, row=8)

    away_ps_j_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_j_label.grid(column=0, row=9)

    away_ps_j_label = tk.Entry(away_roster_grid, textvariable=away_ps_j_var)
    away_ps_j_label.grid(column=1, row=9)

    away_ps_j_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_j_num_var, width=3)
    away_ps_j_num_entry.grid(column=2, row=9)

    away_ps_k_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_k_label.grid(column=0, row=10)

    away_ps_k_label = tk.Entry(away_roster_grid, textvariable=away_ps_k_var)
    away_ps_k_label.grid(column=1, row=10)

    away_ps_k_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_k_num_var, width=3)
    away_ps_k_num_entry.grid(column=2, row=10)

    away_ps_l_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_l_label.grid(column=0, row=11)

    away_ps_l_label = tk.Entry(away_roster_grid, textvariable=away_ps_l_var)
    away_ps_l_label.grid(column=1, row=11)

    away_ps_l_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_l_num_var, width=3)
    away_ps_l_num_entry.grid(column=2, row=11)

    away_ps_m_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_m_label.grid(column=0, row=12)

    away_ps_m_label = tk.Entry(away_roster_grid, textvariable=away_ps_m_var)
    away_ps_m_label.grid(column=1, row=12)

    away_ps_m_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_m_num_var, width=3)
    away_ps_m_num_entry.grid(column=2, row=12)

    away_ps_n_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_n_label.grid(column=0, row=13)

    away_ps_n_label = tk.Entry(away_roster_grid, textvariable=away_ps_n_var)
    away_ps_n_label.grid(column=1, row=13)

    away_ps_n_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_n_num_var, width=3)
    away_ps_n_num_entry.grid(column=2, row=13)

    away_ps_o_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_o_label.grid(column=0, row=14)

    away_ps_o_label = tk.Entry(away_roster_grid, textvariable=away_ps_o_var)
    away_ps_o_label.grid(column=1, row=14)

    away_ps_o_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_o_num_var, width=3)
    away_ps_o_num_entry.grid(column=2, row=14)

    away_ps_p_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_p_label.grid(column=0, row=15)

    away_ps_p_label = tk.Entry(away_roster_grid, textvariable=away_ps_p_var)
    away_ps_p_label.grid(column=1, row=15)

    away_ps_p_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_p_num_var, width=3)
    away_ps_p_num_entry.grid(column=2, row=15)

    away_ps_q_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_q_label.grid(column=0, row=16)

    away_ps_q_label = tk.Entry(away_roster_grid, textvariable=away_ps_q_var)
    away_ps_q_label.grid(column=1, row=16)

    away_ps_q_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_q_num_var, width=3)
    away_ps_q_num_entry.grid(column=2, row=16)

    away_ps_r_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_r_label.grid(column=0, row=17)

    away_ps_r_label = tk.Entry(away_roster_grid, textvariable=away_ps_r_var)
    away_ps_r_label.grid(column=1, row=17)

    away_ps_r_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_r_num_var, width=3)
    away_ps_r_num_entry.grid(column=2, row=17)

    away_ps_s_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_s_label.grid(column=0, row=18)

    away_ps_s_label = tk.Entry(away_roster_grid, textvariable=away_ps_s_var)
    away_ps_s_label.grid(column=1, row=18)

    away_ps_s_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_s_num_var, width=3)
    away_ps_s_num_entry.grid(column=2, row=18)

    away_ps_t_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_t_label.grid(column=0, row=19)

    away_ps_t_label = tk.Entry(away_roster_grid, textvariable=away_ps_t_var)
    away_ps_t_label.grid(column=1, row=19)

    away_ps_t_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_t_num_var, width=3)
    away_ps_t_num_entry.grid(column=2, row=19)

    away_ps_u_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_u_label.grid(column=0, row=20)

    away_ps_u_label = tk.Entry(away_roster_grid, textvariable=away_ps_u_var)
    away_ps_u_label.grid(column=1, row=20)

    away_ps_u_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_u_num_var, width=3)
    away_ps_u_num_entry.grid(column=2, row=20)

    away_ps_v_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_v_label.grid(column=0, row=21)

    away_ps_v_label = tk.Entry(away_roster_grid, textvariable=away_ps_v_var)
    away_ps_v_label.grid(column=1, row=21)

    away_ps_v_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_v_num_var, width=3)
    away_ps_v_num_entry.grid(column=2, row=21)

    away_ps_w_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_w_label.grid(column=0, row=22)

    away_ps_w_label = tk.Entry(away_roster_grid, textvariable=away_ps_w_var)
    away_ps_w_label.grid(column=1, row=22)

    away_ps_w_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_w_num_var, width=3)
    away_ps_w_num_entry.grid(column=2, row=22)

    away_ps_x_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_x_label.grid(column=0, row=23)

    away_ps_x_label = tk.Entry(away_roster_grid, textvariable=away_ps_x_var)
    away_ps_x_label.grid(column=1, row=23)

    away_ps_x_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_x_num_var, width=3)
    away_ps_x_num_entry.grid(column=2, row=23)

    away_ps_y_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_y_label.grid(column=0, row=24)

    away_ps_y_label = tk.Entry(away_roster_grid, textvariable=away_ps_y_var)
    away_ps_y_label.grid(column=1, row=24)

    away_ps_y_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_y_num_var, width=3)
    away_ps_y_num_entry.grid(column=2, row=24)

    away_ps_z_label = tk.Label(away_roster_grid, text="Player:", font=("Arial", 12))
    away_ps_z_label.grid(column=0, row=25)

    away_ps_z_label = tk.Entry(away_roster_grid, textvariable=away_ps_z_var)
    away_ps_z_label.grid(column=1, row=25)

    away_ps_z_num_entry = tk.Entry(away_roster_grid, textvariable=away_ps_z_num_var, width=3)
    away_ps_z_num_entry.grid(column=2, row=25)

    away_roster_grid.pack()
    away_roster_frame.pack(side=tk.RIGHT, padx=100)

    basic_setup.state('zoomed')
    basic_setup.mainloop()


def load_game():
    print("Holder")


def startup_window():
    global startup
    startup = tk.Tk()
    startup.title("PKV")
    startup.geometry("300x250")

    startup_label = tk.Label(text="ProKeeper for Volleyball", font=("Arial", 18))
    startup_label.pack(padx=5, pady=25)

    new_game_button = tk.Button(startup, text="New Game", font=("Arial", 14), command=new_game_)
    new_game_button.pack(padx=5, pady=10)

    load_game_button = tk.Button(startup, text="Load Game", font=("Arial", 14), command=load_game)
    load_game_button.pack(padx=5, pady=10)

    startup.mainloop()


startup_window()