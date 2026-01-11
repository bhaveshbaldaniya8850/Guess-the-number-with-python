import customtkinter as ctk
from game_engine import GameEngine
import time

# Theme settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

class SciFiGuessGame(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.engine = GameEngine()

        # Window Setup
        self.title("SYSTEM ACCESS TERMINAL")
        self.geometry("600x500")
        self.resizable(False, False)

        # Sci-Fi Colors
        self.color_bg = "#050505"         # Deep black
        self.color_accent = "#00ffcc"     # Neon Cyan
        self.color_error = "#ff3333"      # Neon Red
        self.color_warning = "#00ccff"    # Neon Blue (using for Low/High)
        self.color_success = "#33ff33"    # Neon Green
        self.color_text = "#e0e0e0"

        self.configure(fg_color=self.color_bg)

        self.setup_ui()

    def setup_ui(self):
        # Header / Status
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(pady=20)

        self.status_label = ctk.CTkLabel(
            self.header_frame, 
            text="SECURITY FIREWALL DETECTED", 
            font=("Consolas", 24, "bold"),
            text_color=self.color_error
        )
        self.status_label.pack()

        self.sub_status_label = ctk.CTkLabel(
            self.header_frame, 
            text="PROTOCOL: GUESS SEQUENCE [1-100]", 
            font=("Consolas", 14),
            text_color=self.color_accent
        )
        self.sub_status_label.pack(pady=(5, 0))

        # Main Feedback Display (The "Monitor")
        self.monitor_frame = ctk.CTkFrame(self, fg_color="#111111", border_color=self.color_accent, border_width=2)
        self.monitor_frame.pack(pady=20, padx=40, fill="x")

        self.feedback_label = ctk.CTkLabel(
            self.monitor_frame, 
            text="AWAITING INPUT...", 
            font=("Courier New", 20, "bold"),
            text_color=self.color_text
        )
        self.feedback_label.pack(pady=30)

        # Input Area
        self.input_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.input_frame.pack(pady=10)

        self.entry = ctk.CTkEntry(
            self.input_frame, 
            placeholder_text="KEY", 
            width=150, 
            justify="center",
            font=("Consolas", 18),
            fg_color="#1a1a1a",
            border_color=self.color_accent,
            text_color=self.color_accent
        )
        self.entry.pack(side="left", padx=10)
        self.entry.bind("<Return>", self.process_guess)

        self.submit_btn = ctk.CTkButton(
            self.input_frame, 
            text="EXECUTE", 
            command=self.process_guess,
            width=120,
            font=("Consolas", 14, "bold"),
            fg_color=self.color_accent,
            text_color="black",
            hover_color="#00cca3"
        )
        self.submit_btn.pack(side="left", padx=10)

        # Attempts / Stats
        self.stats_label = ctk.CTkLabel(
            self, 
            text="ATTEMPTS: 0 | INTEGRITY: 100%", 
            font=("Consolas", 12),
            text_color="#555555"
        )
        self.stats_label.pack(side="bottom", pady=10)

    def process_guess(self, event=None):
        guess = self.entry.get()
        if not guess:
            return

        result = self.engine.check_guess(guess)
        self.update_ui(result, guess)
        self.entry.delete(0, "end")

    def update_ui(self, result, guess):
        attempts = self.engine.attempts
        integrity = max(0, 100 - (attempts * 5)) # Dummy integrity logic
        
        self.stats_label.configure(text=f"ATTEMPTS: {attempts} | INTEGRITY: {integrity}%")

        if result == 'INVALID':
            self.feedback_label.configure(text="ERROR: INVALID DATA TYPE", text_color=self.color_error)
            self.sound_effect_visual(self.color_error)
        elif result == 'CORRECT':
            self.feedback_label.configure(text="ACCESS GRANTED TO THE USER.\nSYSTEM UNLOCKED SUCESSFULLY!!!.", text_color=self.color_success)
            self.status_label.configure(text="BYPASS SUCCESSFUL", text_color=self.color_success)
            self.entry.configure(state="disabled")
            self.submit_btn.configure(text="RESET", command=self.reset_game, fg_color=self.color_success)
            self.sound_effect_visual(self.color_success)
        elif result == 'LOW':
            self.feedback_label.configure(text=f"INPUT '{guess}' REJECTED.\nSIGNAL LEVEL: LOW", text_color=self.color_warning)
            self.sound_effect_visual(self.color_warning)
        elif result == 'HIGH':
            self.feedback_label.configure(text=f"INPUT '{guess}' REJECTED.\nSIGNAL LEVEL: HIGH", text_color=self.color_error)
            self.sound_effect_visual(self.color_error)

    def reset_game(self):
        self.engine.reset_game()
        self.status_label.configure(text="SECURITY FIREWALL DETECTED", text_color=self.color_error)
        self.feedback_label.configure(text="AWAITING INPUT...", text_color=self.color_text)
        self.entry.configure(state="normal")
        self.entry.delete(0, "end")
        self.submit_btn.configure(
            text="EXECUTE", 
            command=self.process_guess, 
            fg_color=self.color_accent
        )
        self.stats_label.configure(text="ATTEMPTS: 0 | INTEGRITY: 100%")

    def sound_effect_visual(self, color):
        # Flash the border of the monitor frame
        self.monitor_frame.configure(border_color=color)
        self.after(200, lambda: self.monitor_frame.configure(border_color=self.color_accent) if color != self.color_success else None)

if __name__ == "__main__":
    app = SciFiGuessGame()
    app.mainloop()
