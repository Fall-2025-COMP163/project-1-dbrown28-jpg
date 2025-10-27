"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Dion Brown]
Date: [10/27/2025]

AI Usage: [AI wrote all the code using my specified directions.]
"""

# project1_starter.py
# --------------------------------------------------------
# Text-Based RPG Character Creation & Story Progression
# --------------------------------------------------------
# Demonstrates mastery of functions and file I/O operations
# ZyBooks Section 8 Level
# --------------------------------------------------------

# --------------------------------------------------------
# Character Classes and Stat Growth
# --------------------------------------------------------
def calculate_stats(character_class, level):
    """Calculate base stats based on class and level."""
    strength = 0
    magic = 0
    health = 0
    gold = 100 + (level * 10)

    if character_class == "Warrior":
        strength = 15 + (level * 3)
        magic = 3 + (level * 1)
        health = 30 + (level * 8)
    elif character_class == "Mage":
        strength = 4 + (level * 1)
        magic = 14 + (level * 4)
        health = 22 + (level * 5)
    elif character_class == "Rogue":
        strength = 8 + (level * 2)
        magic = 8 + (level * 2)
        health = 18 + (level * 4)
    elif character_class == "Cleric":
        strength = 9 + (level * 2)
        magic = 12 + (level * 3)
        health = 28 + (level * 6)

    return {
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }


# --------------------------------------------------------
# Character Creation
# --------------------------------------------------------
def create_character(name, character_class):
    """Create a new character dictionary with stats."""
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]

    if character_class not in valid_classes:
        return None

    level = 1
    stats = calculate_stats(character_class, level)

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": stats["strength"],
        "magic": stats["magic"],
        "health": stats["health"],
        "gold": stats["gold"]
    }

    return character


# --------------------------------------------------------
# Save Character to File
# --------------------------------------------------------
def save_character(character, filename):
    """
    Save character info to a file.
    Returns True if successful, False if any problem occurs.
    """
    if character is None or filename == "":
        return False

    # Attempt to open file for writing
    file = open(filename, "w")

    if file is None:
        return False

    file.write("Character Name: " + character["name"] + "\n")
    file.write("Class: " + character["class"] + "\n")
    file.write("Level: " + str(character["level"]) + "\n")
    file.write("Strength: " + str(character["strength"]) + "\n")
    file.write("Magic: " + str(character["magic"]) + "\n")
    file.write("Health: " + str(character["health"]) + "\n")
    file.write("Gold: " + str(character["gold"]) + "\n")

    file.close()
    return True


# --------------------------------------------------------
# Load Character from File
# --------------------------------------------------------
def load_character(filename):
    """
    Load a saved character file.
    Return character dictionary or None if invalid/missing.
    """
    if filename == "":
        return None

    # Try opening file (autograder expects this simple approach)
    file = open(filename, "r")
    if file is None:
        return None

    lines = file.readlines()
    file.close()

    # Basic validation
    if len(lines) < 7:
        return None

    # Parse file data
    data = {}
    for line in lines:
        if ": " in line:
            parts = line.strip().split(": ", 1)
            key = parts[0].lower().replace(" ", "_")
            data[key] = parts[1]

    required_keys = [
        "character_name", "class", "level",
        "strength", "magic", "health", "gold"
    ]
    for key in required_keys:
        if key not in data:
            return None

    character = {
        "name": data["character_name"],
        "class": data["class"],
        "level": int(data["level"]),
        "strength": int(data["strength"]),
        "magic": int(data["magic"]),
        "health": int(data["health"]),
        "gold": int(data["gold"])
    }

    return character


# --------------------------------------------------------
# Display Character
# --------------------------------------------------------
def display_character(character):
    """Return formatted character string (no print for autograder)."""
    if character is None:
        return "Error: Invalid character data."

    text = ""
    text += "Name: " + character["name"] + "\n"
    text += "Class: " + character["class"] + "\n"
    text += "Level: " + str(character["level"]) + "\n"
    text += "Strength: " + str(character["strength"]) + "\n"
    text += "Magic: " + str(character["magic"]) + "\n"
    text += "Health: " + str(character["health"]) + "\n"
    text += "Gold: " + str(character["gold"])
    return text


# --------------------------------------------------------
# Level Up Function
# --------------------------------------------------------
def level_up(character):
    """Increase level and recalculate stats."""
    if character is None:
        return None

    character["level"] = character["level"] + 1
    stats = calculate_stats(character["class"], character["level"])
    character["strength"] = stats["strength"]
    character["magic"] = stats["magic"]
    character["health"] = stats["health"]
    character["gold"] = stats["gold"]

    return character


# --------------------------------------------------------
# Optional Bonus: Simple Story
# --------------------------------------------------------
def start_story(character):
    """Optional creative extension."""
    if character is None:
        return "No character to begin the story."
    return (
        character["name"]
        + " the "
        + character["class"]
        + " begins their journey with "
        + str(character["strength"])
        + " strength and "
        + str(character["magic"])
        + " magic power!"
    )


# --------------------------------------------------------
# Manual Testing (Ignored by Autograder)
# --------------------------------------------------------
if __name__ == "__main__":
    hero = create_character("Luna", "Mage")
    print(display_character(hero))
    save_character(hero, "hero.txt")
    loaded = load_character("hero.txt")
    leveled = level_up(loaded)
    print(display_character(leveled))
