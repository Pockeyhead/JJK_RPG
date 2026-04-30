import os
import random

# Path Configuration
TECH_PATH = "Player_Assets/Cursed_Techniques"
TRAIT_PATH = "Player_Assets/Traits"

CLANS = ["Gojo", "Zenin", "Kamo", "Inumaki", "Fujiwara", "Abe", "Sugawara", "Taira", "Minamoto", "Itadori", "Fushiguro", "Okkotsu", "Iori", "Mei", "Kusakabe", "Nanami", "Sukuna", "No clan"]

# Multipliers: Higher number = Higher chance for specific files
INFLUENCES = {
    "Zenin": {
        "Projection_Sorcery_24.json": 5, 
        "Projection_Sorcery_32.json": 5,
        "Heavenly_Restriction_Perfected.json": 3
    },
    "Gojo": {
        "Limitless.json": 8, 
        "Six_Eyes.json": 6
    },
    "Sukuna": {
        "Shrine.json": 6, 
        "Truly_Mutilated.json": 5
    },
    "No clan": {
        "7-3_Ratio.json": 2,
        "Perfected_Vessel.json": 4,
        "Heavenly_Restriction_Weakened.json": 3 # Moved here
    }
}

def get_assets(directory):
    """Scans the directory for .json files."""
    if not os.path.exists(directory):
        return []
    return [f for f in os.listdir(directory) if f.endswith('.json')]

def get_weighted_roll(directory, clan):
    """Reads folder, applies clan weights, and returns a random filename string."""
    options = get_assets(directory)
    if not options:
        return "None.json"

    weights = []
    clan_mods = INFLUENCES.get(clan, {})
    
    for opt in options:
        # Check if the specific filename has a multiplier, otherwise use baseline 1
        weights.append(clan_mods.get(opt, 1))
    
    # Extracting the string from the list returned by choices
    return random.choices(options, weights=weights, k=1)[0]
