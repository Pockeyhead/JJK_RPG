import sys
import os
import time
from Main_Game import game
from Utilities.Return_Tools import Technique_Info_Scanner, Trait_Info_Scanner
from Utilities.Tools import Damage_Mult
import customtkinter as ctk

class GameMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Project Kaisen")
        self.settings_window = None  # Track the window to prevent multiple instances
        self.current_mode = "Borderless"
        self.withdraw() 
        self.set_display_mode(self.current_mode)
        self.deiconify() 

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
        if hasattr(self, "settings_window") and self.settings_window is not None and self.settings_window.winfo_exists():
            self.settings_window.focus()
            return

        self.settings_window = ctk.CTkToplevel(self)
        self.settings_window.geometry("400x350")
        self.settings_window.title("Settings")
        
        self.settings_window.attributes("-topmost", True)
        self.settings_window.grab_set()

        label = ctk.CTkLabel(self.settings_window, text="Settings Menu", font=("Arial", 20))
        label.pack(pady=15)
        
        mode_label = ctk.CTkLabel(self.settings_window, text="Window Mode:", font=("Arial", 12))
        mode_label.pack(pady=(10, 0))

        mode_selector = ctk.CTkSegmentedButton(
            self.settings_window, 
            values=["Windowed", "Borderless"],
            command=self.set_display_mode
        )
        mode_selector.set(self.current_mode) 
        mode_selector.pack(pady=10, padx=20)

        vol_label = ctk.CTkLabel(self.settings_window, text="Volume:", font=("Arial", 12))
        vol_label.pack(pady=(10, 0))
        slider = ctk.CTkSlider(self.settings_window, from_=0, to=100)
        slider.pack(pady=10)

        self.close_btn = ctk.CTkButton(
            self.settings_window, 
            text="Close", 
            command=self.close_settings_menu
        )
        self.close_btn.pack(pady=20)

    def close_settings_menu(self):
        if self.settings_window:
            self.settings_window.destroy()
            self.settings_window = None  
            self.lift()                 
            self.focus_force() 

    def quitgame(self):
        app.quit()

    def set_display_mode(self, mode):
        self.current_mode = mode
        self.attributes("-fullscreen", False)
        self.overrideredirect(False)
        self.state('normal')
        self.update()
            
        if mode == "Borderless":
            self.overrideredirect(True) 
            w, h = self.winfo_screenwidth(), self.winfo_screenheight()
            self.geometry(f"{w}x{h}+0+0")
            
        elif mode == "Windowed":
            self.geometry("800x600+100+100")

if __name__ == "__main__":
    app = GameMenu()
    app.mainloop()