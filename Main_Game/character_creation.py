import customtkinter as ctk
from Main_Game import character_logic as Logic
from Utilities.Tools.Global_Menu import GlobalMenu
import random


class CharacterCreator(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        self.pack(expand=True, fill="both")

        self.parent = parent
        self.nav_menu = GlobalMenu(self, self.parent)

        # =========================================================
        # STATE
        # =========================================================
        self.selected_clan = "No clan"
        self.is_rolling = False

        # ---- Identity / Appearance ----
        self.gender = ctk.StringVar(value="Male")
        self.pronouns = ctk.StringVar(value="He/Him")
        self.body_type = ctk.StringVar(value="Average")
        self.skin_tone = ctk.StringVar(value="Light")

        self.hair = ctk.StringVar(value="Short")
        self.eye_color = ctk.StringVar(value="Brown")
        self.height = ctk.StringVar(value="Average")

        # ---- Stats ----
        self.stats = {
            "Strength": 5,
            "Agility": 5,
            "Intelligence": 5,
            "Endurance": 5,
            "Willpower": 5,
            "Perception": 5
        }

        self.base_stats = self.stats.copy()
        self.stat_points = 8

        self.build = "Unformed"

        # =========================================================
        # MAIN UI
        # =========================================================
        self.container = ctk.CTkFrame(self, corner_radius=20)
        self.container.pack(expand=True, fill="both", padx=120, pady=40)

        self.content = ctk.CTkFrame(self.container, fg_color="transparent")
        self.content.pack(expand=True)

        ctk.CTkLabel(
            self.content,
            text="Character Creation",
            font=("Arial", 38, "bold")
        ).pack(pady=(20, 25))

        # =========================================================
        # NAME
        # =========================================================
        self.name_entry = ctk.CTkEntry(
            self.content,
            placeholder_text="Character Name",
            width=380,
            height=42
        )
        self.name_entry.pack(pady=10)

        self.name_error = ctk.CTkLabel(self.content, text="", text_color="red")
        self.name_error.pack()

        # =========================================================
        # CLAN
        # =========================================================
        self.clan_label = ctk.CTkLabel(
            self.content,
            text="???",
            font=("Arial", 30, "bold"),
            text_color="#C084FC"
        )
        self.clan_label.pack(pady=15)

        self.roll_btn = ctk.CTkButton(
            self.content,
            text="Roll Clan",
            width=200,
            command=self.roll_clan_animation
        )
        self.roll_btn.pack()

        # =========================================================
        # APPEARANCE
        # =========================================================
        appearance = ctk.CTkFrame(self.content)
        appearance.pack(pady=15)

        ctk.CTkLabel(
            appearance,
            text="Appearance",
            font=("Arial", 16, "bold")
        ).pack(pady=5)

        # ---- Row 1: Identity ----
        row1 = ctk.CTkFrame(appearance, fg_color="transparent")
        row1.pack(pady=4)

        ctk.CTkOptionMenu(
            row1,
            variable=self.gender,
            values=["Male", "Female", "Nonbinary"]
        ).pack(side="left", padx=5)

        ctk.CTkOptionMenu(
            row1,
            variable=self.pronouns,
            values=["He/Him", "She/Her", "They/Them"]
        ).pack(side="left", padx=5)

        # ---- Row 2: Physical ----
        row2 = ctk.CTkFrame(appearance, fg_color="transparent")
        row2.pack(pady=4)

        ctk.CTkOptionMenu(
            row2,
            variable=self.body_type,
            values=["Slim", "Athletic", "Average", "Broad", "Lean"]
        ).pack(side="left", padx=5)

        ctk.CTkOptionMenu(
            row2,
            variable=self.height,
            values=["Short", "Average", "Tall", "Very Tall"]
        ).pack(side="left", padx=5)

        # ---- Row 3: Visual ----
        row3 = ctk.CTkFrame(appearance, fg_color="transparent")
        row3.pack(pady=4)

        ctk.CTkOptionMenu(
            row3,
            variable=self.hair,
            values=["Short", "Long", "Spiky", "Braided"]
        ).pack(side="left", padx=5)

        ctk.CTkOptionMenu(
            row3,
            variable=self.eye_color,
            values=["Brown", "Blue", "Green", "Gray", "Amber"]
        ).pack(side="left", padx=5)

        ctk.CTkOptionMenu(
            row3,
            variable=self.skin_tone,
            values=["Light", "Tan", "Brown", "Dark", "Ashen"]
        ).pack(side="left", padx=5)

        # =========================================================
        # STATS
        # =========================================================
        stats_frame = ctk.CTkFrame(self.content)
        stats_frame.pack(pady=15)

        self.stat_labels = {}

        for stat in self.stats:
            row = ctk.CTkFrame(stats_frame)
            row.pack(fill="x", pady=2)

            label = ctk.CTkLabel(row, text="")
            label.pack(side="left")

            ctk.CTkButton(
                row, text="-", width=30,
                command=lambda s=stat: self.remove_stat(s)
            ).pack(side="right", padx=2)

            ctk.CTkButton(
                row, text="+", width=30,
                command=lambda s=stat: self.add_stat(s)
            ).pack(side="right")

            self.stat_labels[stat] = label

        self.points_label = ctk.CTkLabel(self.content, text="")
        self.points_label.pack()

        # =========================================================
        # BUILD
        # =========================================================
        self.build_label = ctk.CTkLabel(
            self.content,
            text="Build: Unformed",
            font=("Arial", 18, "bold"),
            text_color="#FACC15"
        )
        self.build_label.pack(pady=10)

        # =========================================================
        # FINAL
        # =========================================================
        self.confirm_btn = ctk.CTkButton(
            self.content,
            text="Create Character",
            state="disabled",
            command=self.save
        )
        self.confirm_btn.pack(pady=20)

        self.update_ui()

    # =========================================================
    # CLAN ROLL ANIMATION
    # =========================================================
    def roll_clan_animation(self):
        if self.is_rolling:
            return

        self.is_rolling = True
        self.roll_btn.configure(state="disabled")

        cycles = 18
        delay = 60

        def spin(i=0):
            if i < cycles:
                fake_clan = random.choice(Logic.CLANS)
                self.clan_label.configure(text=fake_clan)
                self.after(delay, lambda: spin(i + 1))
            else:
                self.selected_clan = random.choice(Logic.CLANS)
                self.clan_label.configure(text=self.selected_clan)

                self.update_build()
                self.confirm_btn.configure(state="normal")

                self.roll_btn.configure(state="normal")
                self.is_rolling = False

        spin()

    # =========================================================
    # STATS
    # =========================================================
    def add_stat(self, stat):
        if self.stat_points <= 0:
            return
        self.stats[stat] += 1
        self.stat_points -= 1
        self.update_build()
        self.update_ui()

    def remove_stat(self, stat):
        if self.stats[stat] <= self.base_stats[stat]:
            return
        self.stats[stat] -= 1
        self.stat_points += 1
        self.update_build()
        self.update_ui()

    # =========================================================
    # BUILD (CLAN INFLUENCE)
    # =========================================================
    def update_build(self):
        clan = self.selected_clan

        if clan in ["Zenith", "Kurogane"]:
            self.build = "Frontline Warrior"
        elif clan in ["Veyra"]:
            self.build = "Shadow Skirmisher"
        elif clan in ["Astra"]:
            self.build = "Arcane Specialist"
        else:
            self.build = "Wanderer"

        self.build_label.configure(text=f"Build: {self.build}")

    # =========================================================
    # UI UPDATE
    # =========================================================
    def update_ui(self):
        for stat in self.stats:
            self.stat_labels[stat].configure(
                text=f"{stat}: {self.stats[stat]}"
            )

        self.points_label.configure(text=f"Points: {self.stat_points}")

    # =========================================================
    # SAVE
    # =========================================================
    def save(self):
        name = self.name_entry.get().strip()

        if not name:
            self.name_error.configure(text="Name required")
            return

        data = {
            "name": name,
            "clan": self.selected_clan,
            "build": self.build,
            "appearance": {
                "gender": self.gender.get(),
                "pronouns": self.pronouns.get(),
                "body_type": self.body_type.get(),
                "skin_tone": self.skin_tone.get(),
                "hair": self.hair.get(),
                "eye_color": self.eye_color.get(),
                "height": self.height.get()
            },
            "stats": self.stats
        }

        print("CHARACTER CREATED")
        print(data)