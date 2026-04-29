import customtkinter as ctk

class CharacterCreator(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self.pack(expand=True, fill="both")
        self.parent = parent

        self.menu_dropdown = ctk.CTkOptionMenu(
            self,
            values=["≡", "Settings", "Back to Main Menu", "Quit Game"],
            command=self.menu_handler,
            width=60,
            height=40,
            font=("Arial", 25),
            fg_color="#333333",
            button_color="#333333",
            button_hover_color="#555555",
            dropdown_hover_color="#444444"
        )
        self.menu_dropdown.set("≡")
        self.menu_dropdown.place(relx=0.98, rely=0.02, anchor="ne")

        self.title_label = ctk.CTkLabel(
            self, 
            text="Character Creation", 
            font=("Arial", 32, "bold")
        )
        self.title_label.pack(pady=(60, 20))

        self.name_entry = ctk.CTkEntry(
            self, 
            placeholder_text="Enter Character Name...", 
            width=300, 
            height=40
        )
        self.name_entry.pack(pady=10)

        self.desc_label = ctk.CTkLabel(
            self, 
            text="   E", 
            font=("Arial", 14, "italic")
        )
        self.desc_label.pack(pady=10)

    def menu_handler(self, choice):
        if choice == "Settings":
            self.parent.open_settings()
            
        elif choice == "Back to Main Menu":
            self.destroy()
            self.parent.show_menu()
            
        elif choice == "Quit Game":
            self.parent.quit()
        
        self.menu_dropdown.set("≡")
