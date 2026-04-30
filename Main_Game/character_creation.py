import customtkinter as ctk
from Utilities.Tools.Global_Menu import GlobalMenu

class CharacterCreator(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self.pack(expand=True, fill="both")
        self.parent = parent 

        # --- Import the Global Menu ---
        self.nav_menu = GlobalMenu(self, self.parent)

        # --- UI Elements ---
        self.title_label = ctk.CTkLabel(self, text="Character Creation", font=("Arial", 32, "bold"))
        self.title_label.pack(pady=(60, 30))

        # Name Input
        self.name_label = ctk.CTkLabel(self, text="Character Name", font=("Arial", 16))
        self.name_label.pack(pady=(10, 5))
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Enter Name...", width=300)
        self.name_entry.pack(pady=10)

        # Role Selection
        self.role_label = ctk.CTkLabel(self, text="Select Your Path", font=("Arial", 16))
        self.role_label.pack(pady=(20, 5))
        self.role_var = ctk.StringVar(value="Sorcerer")
        self.role_selector = ctk.CTkSegmentedButton(
            self,
            values=["Sorcerer", "Curse User", "Reincarnated Sorcerer"],
            variable=self.role_var,
            width=450,
            height=40
        )
        self.role_selector.pack(pady=10)

        self.confirm_btn = ctk.CTkButton(self, text="Continue", fg_color="#2c5d33", command=self.save)
        self.confirm_btn.pack(pady=40)

    def save(self):
        print(f"Saving: {self.name_entry.get()} as {self.role_var.get()}")
