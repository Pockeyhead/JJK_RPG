import customtkinter as ctk

class CharacterCreator(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self.pack(expand=True, fill="both")
        self.parent = parent # Reference to GameMenu

        # --- Hamburger Menu (Dropdown) ---
        self.menu_dropdown = ctk.CTkOptionMenu(
            self,
            values=["Back to Main Menu", "Quit Game"],
            command=self.menu_handler,
            width=50,
            font=("Arial", 20),
            fg_color="#333333",
            button_color="#333333",
            button_hover_color="#555555"
        )
        self.menu_dropdown.set("≡") # Set the icon as the initial text
        self.menu_dropdown.place(relx=0.98, rely=0.02, anchor="ne")

        # UI Placeholder
        self.label = ctk.CTkLabel(self, text="Character Creation", font=("Arial", 30))
        self.label.pack(pady=50)

    def menu_handler(self, choice):
        if choice == "Back to Main Menu":
            self.destroy()          # Remove creation screen
            self.parent.show_menu() # Tell parent to show menu buttons again
        elif choice == "Quit Game":
            self.parent.quit()      # Close the app
        
        # Reset the dropdown text back to the icon
        self.menu_dropdown.set("≡")
