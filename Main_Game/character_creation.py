import customtkinter as ctk
from Main_Game import character_logic as Logic
from Utilities.Tools.Global_Menu import GlobalMenu
import random


class CharacterCreator(ctk.CTkFrame):

    MAX_ROLLS = 3
    TRAIT_CHANCE = 0.04  # 4% chance

    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self.pack(expand=True, fill="both")

        self.parent = parent
        self.nav_menu = GlobalMenu(self, self.parent)

        # =========================================================
        # STATE
        # =========================================================
        self.selected_clan = "???"
        self.rolled_trait = None
        self.rolled_tech = None

        self.spinning = False
        self.spin_speed = 50
        self.spin_cycles = 0
        self.max_cycles = 40

        self.rolls_left = self.MAX_ROLLS

        # =========================================================
        # MAIN CONTAINER
        # =========================================================
        self.container = ctk.CTkFrame(
            self,
            width=700,
            height=700,
            corner_radius=25
        )

        self.container.pack(expand=True, padx=40, pady=40)

        # Prevent resizing
        self.container.pack_propagate(False)

        # =========================================================
        # TITLE
        # =========================================================
        self.title_label = ctk.CTkLabel(
            self.container,
            text="Character Creation",
            font=("Arial", 38, "bold")
        )
        self.title_label.pack(pady=(30, 20))

        # =========================================================
        # NAME SECTION
        # =========================================================
        self.name_frame = ctk.CTkFrame(
            self.container,
            fg_color="transparent"
        )
        self.name_frame.pack(pady=(0, 20))

        self.name_label = ctk.CTkLabel(
            self.name_frame,
            text="Character Name",
            font=("Arial", 18, "bold")
        )
        self.name_label.pack()

        self.name_entry = ctk.CTkEntry(
            self.name_frame,
            width=350,
            height=42,
            placeholder_text="Enter your name..."
        )
        self.name_entry.pack(pady=(5, 0))

        self.name_error = ctk.CTkLabel(
            self.name_frame,
            text="",
            text_color="#FF5E5E"
        )
        self.name_error.pack(pady=(5, 0))

        # =========================================================
        # WHEEL AREA
        # =========================================================
        self.wheel_frame = ctk.CTkFrame(
            self.container,
            width=580,
            height=320,
            corner_radius=20
        )
        self.wheel_frame.pack(pady=10)

        # Keep static size
        self.wheel_frame.pack_propagate(False)

        self.wheel_title = ctk.CTkLabel(
            self.wheel_frame,
            text="Clan Wheel",
            font=("Arial", 26, "bold")
        )
        self.wheel_title.pack(pady=(25, 10))

        # Clan display
        self.clan_display = ctk.CTkLabel(
            self.wheel_frame,
            text="???",
            font=("Arial", 44, "bold"),
            text_color="#C084FC",
            width=500,
            height=70
        )
        self.clan_display.pack(pady=10)

        # Status
        self.spin_status = ctk.CTkLabel(
            self.wheel_frame,
            text="Press SPIN to roll your clan",
            font=("Arial", 14),
            text_color="#9A9A9A"
        )
        self.spin_status.pack(pady=(0, 10))

        # Rolls left
        self.roll_counter = ctk.CTkLabel(
            self.wheel_frame,
            text=f"Rolls Left: {self.rolls_left}",
            font=("Arial", 18, "bold"),
            text_color="#FACC15"
        )
        self.roll_counter.pack(pady=(0, 20))

        # Spin button
        self.roll_btn = ctk.CTkButton(
            self.wheel_frame,
            text="SPIN",
            width=220,
            height=50,
            font=("Arial", 20, "bold"),
            fg_color="#5B21B6",
            hover_color="#6D28D9",
            command=self.start_spin
        )
        self.roll_btn.pack()

        # =========================================================
        # RESULTS SECTION
        # =========================================================
        self.results_frame = ctk.CTkFrame(
            self.container,
            width=580,
            height=170,
            corner_radius=20
        )
        self.results_frame.pack(pady=20)

        self.results_frame.pack_propagate(False)

        self.results_title = ctk.CTkLabel(
            self.results_frame,
            text="Innate Results",
            font=("Arial", 22, "bold")
        )
        self.results_title.pack(pady=(15, 10))

        self.trait_display = ctk.CTkLabel(
            self.results_frame,
            text="Trait: None",
            font=("Consolas", 18),
            text_color="#888888"
        )
        self.trait_display.pack(pady=5)

        self.tech_display = ctk.CTkLabel(
            self.results_frame,
            text="Technique: ???",
            font=("Consolas", 18),
            text_color="#FACC15"
        )
        self.tech_display.pack(pady=5)

        # =========================================================
        # FINALIZE BUTTON
        # =========================================================
        self.confirm_btn = ctk.CTkButton(
            self.container,
            text="Create Character",
            width=240,
            height=50,
            font=("Arial", 18, "bold"),
            fg_color="#166534",
            hover_color="#15803D",
            state="disabled",
            command=self.save
        )
        self.confirm_btn.pack(pady=(10, 25))

    # =============================================================
    # START SPIN
    # =============================================================
    def start_spin(self):

        if self.spinning:
            return

        if self.rolls_left <= 0:
            return

        self.spinning = True

        self.roll_btn.configure(state="disabled")
        self.confirm_btn.configure(state="disabled")

        self.spin_cycles = 0
        self.spin_speed = 35

        self.spin_status.configure(
            text="Spinning...",
            text_color="#FACC15"
        )

        self.animate_spin()

    # =============================================================
    # SPIN ANIMATION
    # =============================================================
    def animate_spin(self):

        if self.spin_cycles < self.max_cycles:

            fake_clan = random.choice(Logic.CLANS)

            self.clan_display.configure(
                text=fake_clan
            )

            self.spin_cycles += 1

            # Slow down effect
            self.spin_speed += 7

            self.after(self.spin_speed, self.animate_spin)

        else:
            self.finish_spin()

    # =============================================================
    # FINISH SPIN
    # =============================================================
    def finish_spin(self):

        self.selected_clan = random.choice(Logic.CLANS)

        self.clan_display.configure(
            text=self.selected_clan,
            text_color="#E879F9"
        )

        # =====================================================
        # TRAIT ROLL (VERY LOW CHANCE)
        # =====================================================
        if random.random() < self.TRAIT_CHANCE:

            valid_trait = False

            while not valid_trait:

                trait_file = Logic.get_weighted_roll(
                    Logic.TRAIT_PATH,
                    self.selected_clan
                )

                trait_name = trait_file.replace(".json", "")

                # Remove Heavenly Restriction
                if trait_name.lower() != "heavenly restriction":
                    valid_trait = True
                    self.rolled_trait = trait_name

        else:
            self.rolled_trait = None

        # =====================================================
        # TECHNIQUE ROLL
        # =====================================================
        tech_file = Logic.get_weighted_roll(
            Logic.TECH_PATH,
            self.selected_clan
        )

        self.rolled_tech = tech_file.replace(".json", "")

        # =====================================================
        # UPDATE UI
        # =====================================================
        if self.rolled_trait:

            self.trait_display.configure(
                text=f"Trait: {self.rolled_trait}",
                text_color="#C084FC"
            )

        else:

            self.trait_display.configure(
                text="Trait: None",
                text_color="#777777"
            )

        self.tech_display.configure(
            text=f"Technique: {self.rolled_tech}",
            text_color="#FACC15"
        )

        self.spin_status.configure(
            text="Clan Selected",
            text_color="#4ADE80"
        )

        # =====================================================
        # ROLL LIMIT
        # =====================================================
        self.rolls_left -= 1

        self.roll_counter.configure(
            text=f"Rolls Left: {self.rolls_left}"
        )

        if self.rolls_left <= 0:

            self.roll_btn.configure(
                text="NO ROLLS LEFT",
                state="disabled",
                fg_color="#444444"
            )

        else:

            self.roll_btn.configure(
                state="normal"
            )

        self.confirm_btn.configure(state="normal")

        self.spinning = False

    # =============================================================
    # SAVE
    # =============================================================
    def save(self):

        name = self.name_entry.get().strip()

        if not name:

            self.name_error.configure(
                text="Character name cannot be empty."
            )

            return

        self.name_error.configure(text="")

        final_data = {
            "name": name,
            "clan": self.selected_clan,
            "trait": self.rolled_trait if self.rolled_trait else "None",
            "technique": self.rolled_tech
        }

        print("\n===================================")
        print(" CHARACTER CREATED ")
        print("===================================")
        print(final_data)