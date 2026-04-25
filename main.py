import sys
import os
import time
from Utilities.Return_Tools import Technique_Info_Scanner, Trait_Info_Scanner
from Utilities.Tools import Damage_Mult
import customtkinter as ctk

class GameMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Project Kaisen")

        # Title Label
        self.label = ctk.CTkLabel(self, text="Project Kaisen", font=("Impact", 30))
        self.label.place(relx=0.5, rely=0.2, anchor="center")

        # Start Button
        self.start_btn = ctk.CTkButton(self, text="Start Game", command=self.start_game)
        self.start_btn.place(relx=0.5, rely=0.4, anchor="center")

        # Settings Button
        self.settings_btn = ctk.CTkButton(self, text="Settings", command=self.open_settings)
        self.settings_btn.place(relx=0.5, rely=0.55, anchor="center")
        
        # Quit Button
        self.quit_btn = ctk.CTkButton(self, text= "Quit", command=self.quitgame)
        self.quit_btn.place(relx = 0.5, rely = 0.7, anchor = "center")

    def start_game(self):
        print("Game Started!")

    def open_settings(self):
        settings_window = ctk.CTkToplevel(self)
        settings_window.geometry("300x200")
        settings_window.title("Settings")
        
        # Make it modal (focus stays here)
        settings_window.grab_set()

        # Add settings content
        label = ctk.CTkLabel(settings_window, text="Settings Menu", font=("Arial", 20))
        label.pack(pady=20)
        
        slider = ctk.CTkSlider(settings_window, from_=0, to=100)
        slider.pack(pady=10)

        close_btn = ctk.CTkButton(settings_window, text="Close", command=settings_window.destroy)
        close_btn.pack(pady=10)

    def quitgame(self):
        app.quit()

if __name__ == "__main__":
    app = GameMenu()
    app.mainloop()