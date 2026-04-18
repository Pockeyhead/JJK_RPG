from pathlib import Path
import json
MAIN_DIR = Path("Player_Assets/Cursed_Techniques")

def getTechniqueInfo(Filename):
    Filename = Filename + ".json"
    with open(MAIN_DIR/Filename, "r") as file:
        data = json.load(file)
    return data