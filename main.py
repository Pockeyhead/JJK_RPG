import sys
import os
import time
from Main_Game import game
from Main_Game.character_creation import CharacterCreator
from Utilities.Return_Tools import Technique_Info_Scanner, Trait_Info_Scanner
from Utilities.Tools import Damage_Mult
from Utilities.Tools.settings_menu import SettingsWindow
import customtkinter as ctk

class GameMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Project Kaisen")
        self.settings_window = None 
        self.current_mode = "Borderless"
        
        self.withdraw() 
        self.set_display_mode(self.current_mode)
        self.deiconify() 
        self.show_menu() 

    def start_game(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.creation_screen = CharacterCreator(self)
        print("Character Creation Loaded!")

    def open_settings(self):
        if self.settings_window is not None and self.settings_window.winfo_exists():
            self.settings_window.focus()
            return
            
        self.settings_window = SettingsWindow(self)

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

    def show_menu(self):
        self.menu_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.menu_frame.pack(expand=True, fill="both")

        self.label = ctk.CTkLabel(self.menu_frame, text="Project Kaisen", font=("Impact", 50))
        self.label.place(relx=0.5, rely=0.2, anchor="center")

        self.start_btn = ctk.CTkButton(self.menu_frame, text="Start Game", command=self.start_game)
        self.start_btn.place(relx=0.5, rely=0.4, anchor="center")

        self.settings_btn = ctk.CTkButton(self.menu_frame, text="Settings", command=self.open_settings)
        self.settings_btn.place(relx=0.5, rely=0.55, anchor="center")
        
        self.quit_btn = ctk.CTkButton(self.menu_frame, text="Quit", command=self.quit)
        self.quit_btn.place(relx=0.5, rely=0.7, anchor="center")

if __name__ == "__main__":
    app = GameMenu()
    app.mainloop()