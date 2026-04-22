from pathlib import Path
import json
MAIN_DIR = Path("Player_Assets/Traits")

def getTraitInfo(Filename):
    Filename = Filename + ".json"
    with open(MAIN_DIR/Filename, "r") as file:
        data = json.load(file)
    return data