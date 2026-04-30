import customtkinter as ctk

class GlobalMenu:
    def __init__(self, master, parent_app):
        self.master = master
        self.parent_app = parent_app

        self.menu_dropdown = ctk.CTkOptionMenu(
            self.master,
            values=["Settings", "Back to Main Menu", "Quit Game"],
            command=self.menu_handler,
            width=60,
            height=40,
            font=("Arial", 25),
            fg_color="#333333",
            button_color="#333333",
            button_hover_color="#555555"
        )
        self.menu_dropdown.set("≡")
        self.menu_dropdown.place(relx=0.98, rely=0.02, anchor="ne")

    def menu_handler(self, choice):
        if choice == "Settings":
            self.parent_app.open_settings()
            
        elif choice == "Back to Main Menu":
            # If we are in a sub-frame, destroy it and show main menu
            if hasattr(self.master, "destroy"):
                self.master.destroy()
            self.parent_app.show_menu()
            
        elif choice == "Quit Game":
            self.parent_app.quit()
        
        # Reset display
        self.menu_dropdown.set("≡")
