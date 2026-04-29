import customtkinter as ctk

class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent
        self.geometry("400x350")
        self.title("Settings")
        
        # Focus and Modal settings
        self.attributes("-topmost", True)
        self.grab_set()

        label = ctk.CTkLabel(self, text="Settings Menu", font=("Arial", 20))
        label.pack(pady=15)
        
        mode_label = ctk.CTkLabel(self, text="Window Mode:", font=("Arial", 12))
        mode_label.pack(pady=(10, 0))

        # Mode Selector
        self.mode_selector = ctk.CTkSegmentedButton(
            self, 
            values=["Windowed", "Borderless"],
            command=self.parent.set_display_mode # Calls back to main app
        )
        self.mode_selector.set(self.parent.current_mode) 
        self.mode_selector.pack(pady=10, padx=20)

        vol_label = ctk.CTkLabel(self, text="Volume:", font=("Arial", 12))
        vol_label.pack(pady=(10, 0))
        slider = ctk.CTkSlider(self, from_=0, to=100)
        slider.pack(pady=10)

        self.close_btn = ctk.CTkButton(
            self, 
            text="Close", 
            command=self.close_settings
        )
        self.close_btn.pack(pady=20)

    def close_settings(self):
        self.destroy()
        self.parent.settings_window = None
        self.parent.lift()
        self.parent.focus_force()