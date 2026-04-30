import customtkinter as ctk
from Main_Game import character_logic as Logic  # Import your logic file
from Utilities.Tools.Global_Menu import GlobalMenu

class CharacterCreator(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self.pack(expand=True, fill="both")
        self.parent = parent 
        self.nav_menu = GlobalMenu(self, self.parent)

        # --- State Variables ---
        self.selected_clan = "No clan"
        self.debug_mode = False
        self.rolled_trait = None
        self.rolled_tech = None
        
        # --- Keybindings ---
        self.parent.bind("<Alt-d>", lambda e: self.toggle_debug_mode())

        # --- UI Elements ---
        self.title_label = ctk.CTkLabel(self, text="Character Creation", font=("Arial", 32, "bold"))
        self.title_label.pack(pady=(40, 20))

        # 1. Name Input
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Enter Name...", width=300)
        self.name_entry.pack(pady=10)
        
        # Error label for name validation
        self.name_error_label = ctk.CTkLabel(self, text="", font=("Arial", 12), text_color="#FF6B6B")
        self.name_error_label.pack(pady=(0, 10))

        # 2. Clan Section
        self.clan_label = ctk.CTkLabel(self, text="Clan: ???", font=("Arial", 16, "italic"))
        self.clan_label.pack(pady=(10, 0))
        self.clan_btn = ctk.CTkButton(self, text="Roll Clan", command=self.roll_clan_ui, fg_color="#3b3b3b")
        self.clan_btn.pack(pady=5)

        # 4. Results Display
        self.trait_display = ctk.CTkLabel(self, text="Trait: --", font=("Consolas", 14))
        self.trait_display.pack(pady=5)
        self.trait_display.pack_forget()  # Hidden by default

        self.tech_display = ctk.CTkLabel(self, text="Technique: --", font=("Consolas", 14))
        self.tech_display.pack(pady=5)
        self.tech_display.pack_forget()  # Hidden by default

        # 5. Roll Potential & Save
        self.roll_btn = ctk.CTkButton(self, text="Roll Potential", state="disabled", command=self.roll_potential_ui)
        self.roll_btn.pack(pady=5)

        self.confirm_btn = ctk.CTkButton(self, text="Finalize", fg_color="#2c5d33", state="disabled", command=self.save)
        self.confirm_btn.pack(pady=20)

    def toggle_debug_mode(self):
        self.debug_mode = not self.debug_mode
        if self.debug_mode:
            print("[DEBUG MODE ON]")
            self.trait_display.pack(pady=5)
            self.tech_display.pack(pady=5)
        else:
            print("[DEBUG MODE OFF]")
            self.trait_display.pack_forget()
            self.tech_display.pack_forget()

    def roll_clan_ui(self):
        import random
        self.selected_clan = random.choice(Logic.CLANS)
        self.clan_label.configure(text=f"Clan: {self.selected_clan}", font=("Arial", 16, "bold"))
        self.roll_btn.configure(state="normal")

    def roll_potential_ui(self):
        import random
        # Only roll a trait 20% of the time
        if random.random() < 0.1:
            trait_file = Logic.get_weighted_roll(Logic.TRAIT_PATH, self.selected_clan)
            self.rolled_trait = trait_file.replace('.json', '')
        else:
            self.rolled_trait = None
        
        # Always roll technique
        tech_file = Logic.get_weighted_roll(Logic.TECH_PATH, self.selected_clan)
        self.rolled_tech = tech_file.replace('.json', '')
        
        # Display trait if it exists
        if self.rolled_trait:
            self.trait_display.configure(text=f"Trait: {self.rolled_trait}", text_color="#A855F7")
        else:
            self.trait_display.configure(text="Trait: None", text_color="#808080")
        
        self.tech_display.configure(text=f"Technique: {self.rolled_tech}", text_color="#EAB308")
        
        # Show in debug mode
        if self.debug_mode:
            self.trait_display.pack(pady=5)
            self.tech_display.pack(pady=5)
        
        self.confirm_btn.configure(state="normal")

    def save(self):
        # Validate name input
        name = self.name_entry.get().strip()
        if not name:
            self.name_error_label.configure(text="Character name cannot be empty or whitespace only.")
            return
        
        # Clear error message if validation passes
        self.name_error_label.configure(text="")
        
        # Gather final data for saving
        final_data = {
            "name": name,
            "clan": self.selected_clan,
            "trait": self.rolled_trait if self.rolled_trait else "--",
            "technique": self.rolled_tech if self.rolled_tech else "--"
        }
        print(f"Character Created: {final_data}")
