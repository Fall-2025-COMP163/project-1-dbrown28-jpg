"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Dion Brown]
Date: [10/27/2025]

AI Usage: [AI wrote all the code using my specified directions.]
"""

# project1_starter.py
# -------------------------------------------------------
# Text-Based RPG Character Creation & Story System
# ZyBooks Project - Functions & File I/O Demonstration
# -------------------------------------------------------

# ---------------------------
# Character Stat Calculator
# ---------------------------
def calculate_stats(character_class, level):
    """Return a dictionary of calculated stats based on class and level."""

    # Default base stats for all classes
    strength = 0
    magic = 0
    health = 0
    gold = 100 + (level * 10)

    if character_class == "Warrior":
        strength = 15 + (level * 3)
        magic = 4 + (level * 1)
        health = 35 + (level * 7)
    elif character_class == "Mage":
        strength = 5 + (level * 1)
        magic = 15 + (level * 4)
        health = 25 + (level * 5)
    elif character_class == "Rogue":
        strength = 10 + (level * 2)
        magic = 10 + (level * 2)
        health = 20 + (level * 4)
    elif character_class == "Cleric":
        strength = 10 + (level * 2)
        magic = 14 + (level * 3)
        health = 30 + (level * 6)

    return {
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }


# ---------------------------
# Character Creation
# ---------------------------
def create_character(name, character_class):
    """Create and return a character dictionary."""
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


# ---------------------------
# Save Character to File
# ---------------------------
def save_character(character, filename):
    """
    Save the character data in exact format.
    Return True if successful, False if any issue.
    """
    if character is None or filename == "":
        return False

    # Attempt to open file for writing
    file = open(filename, "w")
    if file is None:
        return False

    # EXACT required format, ending with newline at bottom
    file.write("Character Name: " + character["name"] + "\n")
    file.write("Class: " + character["class"] + "\n")
    file.write("Level: " + str(character["level"]) + "\n")
    file.write("Strength: " + str(character["strength"]) + "\n")
    file.write("Magic: " + str(character["magic"]) + "\n")
    file.write("Health: " + str(character["health"]) + "\n")
    file.write("Gold: " + str(character["gold"]) + "\n")

    file.close()
    return True


# ---------------------------
# Load Character from File
# ---------------------------
def load_character(filename):
    """
    Load a character from a properly formatted file.
    Return the character dictionary, or None if invalid/missing.
    """
    if filename == "":
        return None

    # Attempt to open file for reading
    file = open(filename, "r")
    if file is None:
        return None

    lines = file.readlines()
    file.close()

    # Must contain all 7 lines
    if len(lines) < 7:
        return None

    data = {}
    for line in lines:
        if ": " in line:
            parts = line.strip().split(": ", 1)
            key = parts[0].lower().replace(" ", "_")
            data[key] = parts[1]

    required = [
        "character_name", "class", "level",
        "strength", "magic", "health", "gold"
    ]
    for key in required:
        if key not in data:
            return None

    # Construct the character dictionary
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


# ---------------------------
# Display Character
# ---------------------------
def display_character(character):
    """Return formatted info as a string (no print)."""
    if character is None:
        return "Error: Invalid character."

    text = ""
    text += "Name: " + character["name"] + "\n"
    text += "Class: " + character["class"] + "\n"
    text += "Level: " + str(character["level"]) + "\n"
    text += "Strength: " + str(character["strength"]) + "\n"
    text += "Magic: " + str(character["magic"]) + "\n"
    text += "Health: " + str(character["health"]) + "\n"
    text += "Gold: " + str(character["gold"])
    return text


# ---------------------------
# Level Up
# ---------------------------
def level_up(character):
    """Increase level by one and recalculate stats."""
    if character is None:
        return None

    new_level = character["level"] + 1
    stats = calculate_stats(character["class"], new_level)

    character["level"] = new_level
    character["strength"] = stats["strength"]
    character["magic"] = stats["magic"]
    character["health"] = stats["health"]
    character["gold"] = stats["gold"]

    return character


# ---------------------------
# Optional Story (Not Tested)
# ---------------------------
def start_story(character):
    """Bonus creative element."""
    if character is None:
        return "No hero found."
    return character["name"] + " the " + character["class"] + " begins their journey!"


# ---------------------------
# Manual Test (Ignored by Grader)
# ---------------------------
if __name__ == "__main__":
    hero = create_character("Aiden", "Warrior")
    save_character(hero, "test_hero.txt")
    loaded = load_character("test_hero.txt")
    leveled = level_up(loaded)
    print(display_character(leveled))

