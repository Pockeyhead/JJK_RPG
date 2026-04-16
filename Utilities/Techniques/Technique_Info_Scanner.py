from pathlib import Path
MAIN_DIR = Path("Player_Assets/Cursed_Techniques")

def getTechniqueInfo(Filename):
    Filename = Filename + ".json"
    with open(MAIN_DIR/Filename, "r"):
        print("opened")