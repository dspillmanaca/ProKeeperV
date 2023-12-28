import tkinter as tk
from tkinter import ttk, simpledialog, filedialog, messagebox
from datetime import datetime

class NewGameWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("New Game - Step 1")
        self.current_step = 1

        # Initialize questions for each step
        self.questions = {
            1: [("Date (MM/DD/YYYY)", ""), ("Time (HH:MM AM/PM)", ""), ("Up Referee Name", ""), ("Down Referee Name (Optional)", ""), ("Scorekeeper Name", "")],
            2: [("Home Team Name", ""), ("Team Mascot", ""), ("Team Code (3 letters, capital only)", ""), ("Upload Logo (Optional)", "")],
            3: [("Away Team Name", ""), ("Team Mascot", ""), ("Team Code (3 letters, capital only)", ""), ("Upload Logo (Optional)", "")],
            4: [("Orientation: Home Team Side", ""), ("First Serve (Home/Away)", "")]
        }

        # Create and pack the question label
        self.question_label = tk.Label(root, text=f"Step {self.current_step}: General Information", font=("Helvetica", 12, "bold"))
        self.question_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="w")

        # Create a dictionary to store user input
        self.user_inputs = {}

        # Create and pack the input fields
        self.create_input_fields()

        # Create and pack the "Next" button
        self.next_button = tk.Button(root, text="Next", command=self.next_step)
        self.next_button.grid(row=len(self.questions[self.current_step]) + 1, column=1, pady=10, sticky="e")

        # Create and pack the "Previous" button (disabled for the first step)
        self.prev_button = tk.Button(root, text="Previous", command=self.prev_step, state=tk.DISABLED)
        self.prev_button.grid(row=len(self.questions[self.current_step]) + 1, column=0, pady=10, sticky="w")

    def create_input_fields(self):
        # Hide widgets from the previous step
        for widget in self.root.winfo_children():
            widget.grid_remove()

        # Create and pack the question label
        self.update_question_label()

        # Create and pack the input fields for the current step
        for row, (label, default_value) in enumerate(self.questions[self.current_step], start=1):
            label_widget = tk.Label(self.root, text=label, padx=10, pady=5, anchor="e")
            label_widget.grid(row=row, column=0, sticky="e")

            if "Logo" in label:
                entry_widget = ttk.Entry(self.root, state="disabled")
                browse_button = tk.Button(self.root, text="Browse", command=lambda entry=entry_widget: self.browse_logo(entry))
                browse_button.grid(row=row, column=1, pady=5, padx=(0, 10), sticky="w")
            else:
                entry_widget = ttk.Entry(self.root)
                entry_widget.insert(0, default_value)

            entry_widget.grid(row=row, column=1, pady=5, padx=(0, 10), sticky="w")
            self.user_inputs[label] = entry_widget

        # Create and pack the "Next" button
        self.next_button = tk.Button(self.root, text="Next", command=self.next_step)
        self.next_button.grid(row=len(self.questions[self.current_step]) + 1, column=1, pady=10, sticky="e")

        # Create and pack the "Previous" button (disabled for the first step)
        self.prev_button = tk.Button(self.root, text="Previous", command=self.prev_step, state=tk.DISABLED)
        self.prev_button.grid(row=len(self.questions[self.current_step]) + 1, column=0, pady=10, sticky="w")

    def next_step(self):
        # Validate user input for the current step
        if not self.validate_input():
            return

        # Update the question label for the next step
        self.current_step += 1
        if self.current_step > 4:
            # If all steps are completed, show a message with user input and close the window
            self.show_summary()
            self.root.destroy()
        else:
            self.update_question_label()
            self.create_input_fields()
            self.prev_button.config(state=tk.NORMAL)

    def prev_step(self):
        # Update the question label for the previous step
        self.current_step -= 1
        self.update_question_label()

        # Disable "Previous" button on the first step
        if self.current_step == 1:
            self.prev_button.config(state=tk.DISABLED)

    def validate_input(self):
        # Validate user input based on the current step
        current_step_inputs = self.questions[self.current_step]

        for label, _ in current_step_inputs:
            entry_widget = self.user_inputs[label]
            user_input = entry_widget.get().strip()

            # Validate date and time formats
            if self.current_step == 1:
                if label.startswith("Date"):
                    if not self.validate_date(user_input):
                        messagebox.showerror("Error", "Invalid date format. Please use MM/DD/YYYY.")
                        return False
                elif label.startswith("Time"):
                    if not self.validate_time(user_input):
                        messagebox.showerror("Error", "Invalid time format. Please use HH:MM AM/PM.")
                        return False

            # Save user input
            self.user_inputs[label] = user_input

        return True

    def validate_date(self, date_string):
        try:
            # Attempt to parse the date using datetime
            datetime.strptime(date_string, "%m/%d/%Y")
            return True
        except ValueError:
            return False

    def validate_time(self, time_string):
        try:
            # Attempt to parse the time using datetime
            datetime.strptime(time_string, "%I:%M %p")
            return True
        except ValueError:
            return False

    def show_summary(self):
        # Display a summary message with user input
        summary = "Game Information:\n"
        for step, inputs in self.questions.items():
            summary += f"\nStep {step}:\n"
            for label, _ in inputs:
                value = self.user_inputs[label].get().strip()
                summary += f"{label}: {value}\n"

        messagebox.showinfo("Game Information Summary", summary)

    def update_question_label(self):
        # Update the question label for the current step
        self.question_label.config(text=f"Step {self.current_step}: {self.get_step_title()}")

    def get_step_title(self):
        # Get the title for the current step
        return {
            1: "General Information",
            2: "Home Team Information",
            3: "Away Team Information",
            4: "Orientation"
        }.get(self.current_step, "")

    def browse_logo(self, entry_widget):
        # Allow the user to browse and select a logo file
        file_path = filedialog.askopenfilename(title="Select Logo", filetypes=[("PNG files", "*.png")])

        # Update the entry widget with the selected file path
        entry_widget.delete(0, tk.END)
        entry_widget.insert(0, file_path)

def new_game():
    # Close the main menu window
    root.destroy()

    # Open a new window for the new game with multiple steps
    new_game_root = tk.Tk()
    new_game_window = NewGameWindow(new_game_root)

    # Run the Tkinter event loop for the new window
    new_game_root.mainloop()

def main():
    global root
    # Create the main window
    root = tk.Tk()
    root.title("Game Menu")

    # Create a label for the title
    title_label = tk.Label(root, text="Game Menu", font=("Helvetica", 16))
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Create a button for starting a new game
    new_game_button = tk.Button(root, text="New Game", command=new_game)
    new_game_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Create a button for opening an existing game
    open_game_button = tk.Button(root, text="Open Game")
    open_game_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()