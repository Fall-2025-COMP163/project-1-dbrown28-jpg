"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Dion Brown]
Date: [10/27/2025]

AI Usage: [AI wrote all the code using my specified directions.]
"""

# project1_starter.py
# ------------------------------------------------------------
# Text-Based RPG Character Creation & Story Progression System
# ZyBooks Section 8 Project — Functions and File I/O Mastery
# ------------------------------------------------------------

# ------------------------------------------------------------
# GLOBAL DATA
# ------------------------------------------------------------
VALID_CLASSES = ["Warrior", "Mage", "Rogue", "Cleric"]


# ------------------------------------------------------------
# 1. CREATE CHARACTER
# ------------------------------------------------------------
def create_character(name, character_class):
    """Create and return a new character dictionary."""
    if character_class not in VALID_CLASSES:
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


# ------------------------------------------------------------
# 2. CALCULATE STATS
# ------------------------------------------------------------
def calculate_stats(character_class, level):
    """Calculate stats based on class and level."""

    if character_class == "Warrior":
        base_str, base_mag, base_hp, growth = 14, 3, 30, 2.2
    elif character_class == "Mage":
        base_str, base_mag, base_hp, growth = 4, 14, 22, 1.6
    elif character_class == "Rogue":
        base_str, base_mag, base_hp, growth = 8, 8, 18, 1.8
    elif character_class == "Cleric":
        base_str, base_mag, base_hp, growth = 9, 12, 28, 1.7
    else:
        # Should never reach here if validated earlier
        base_str, base_mag, base_hp, growth = 0, 0, 0, 0

    strength = int(base_str + (level * growth))
    magic = int(base_mag + (level * growth))
    health = int(base_hp + (level * growth * 5))
    gold = 100 + (level * 10)

    return {"strength": strength, "magic": magic, "health": health, "gold": gold}


# ------------------------------------------------------------
# 3. SAVE CHARACTER
# ------------------------------------------------------------
def save_character(character, filename):
    """
    Save the character data to a file in exact format.
    Return True if successful, False if an error occurs.
    """
    # Attempt to open the file for writing
    file = open(filename, "w")

    # Simple check: If file didn't open properly, return False
    if file is None:
        return False

    # Write character data in exact format
    file.write("Character Name: " + character["name"] + "\n")
    file.write("Class: " + character["class"] + "\n")
    file.write("Level: " + str(character["level"]) + "\n")
    file.write("Strength: " + str(character["strength"]) + "\n")
    file.write("Magic: " + str(character["magic"]) + "\n")
    file.write("Health: " + str(character["health"]) + "\n")
    file.write("Gold: " + str(character["gold"]) + "\n")

    file.close()
    return True


# ------------------------------------------------------------
# 4. LOAD CHARACTER
# ------------------------------------------------------------
def load_character(filename):
    """
    Load a saved character file and return its dictionary.
    Return None if file not found or improperly formatted.
    """
    # Attempt to open the file for reading
    file = open(filename, "r")

    if file is None:
        return None

    lines = file.readlines()
    file.close()

    if len(lines) < 7:
        return None

    data = {}
    for line in lines:
        if ": " in line:
            parts = line.strip().split(": ", 1)
            key = parts[0].lower().replace(" ", "_")
            value = parts[1]
            data[key] = value

    required = ["character_name", "class", "level", "strength", "magic", "health", "gold"]
    for key in required:
        if key not in data:
            return None

    # Convert numeric values
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


# ------------------------------------------------------------
# 5. DISPLAY CHARACTER
# ------------------------------------------------------------
def display_character(character):
    """Return formatted text for displaying character info."""
    if character is None:
        return "Error: No character data available."

    output = ""
    output += "Name: " + character["name"] + "\n"
    output += "Class: " + character["class"] + "\n"
    output += "Level: " + str(character["level"]) + "\n"
    output += "Strength: " + str(character["strength"]) + "\n"
    output += "Magic: " + str(character["magic"]) + "\n"
    output += "Health: " + str(character["health"]) + "\n"
    output += "Gold: " + str(character["gold"])
    return output


# ------------------------------------------------------------
# 6. LEVEL UP
# ------------------------------------------------------------
def level_up(character):
    """Increase character level and recalculate stats."""
    if character is None or "class" not in character:
        return None

    new_level = character["level"] + 1
    stats = calculate_stats(character["class"], new_level)

    character["level"] = new_level
    character["strength"] = stats["strength"]
    character["magic"] = stats["magic"]
    character["health"] = stats["health"]
    character["gold"] = stats["gold"]

    return character


# ------------------------------------------------------------
# BONUS: STORY PROGRESSION
# ------------------------------------------------------------
def start_story(character):
    """Simple story intro (bonus creative)."""
    if character is None:
        return "No hero to begin the story."

    return (
        character["name"]
        + " the "
        + character["class"]
        + " awakens in a quiet village.\nArmed with "
        + str(character["strength"])
        + " strength, they prepare for an epic journey!"
    )


# ------------------------------------------------------------
# MANUAL TEST (ignored by autograder)
# ------------------------------------------------------------
if __name__ == "__main__":
    hero = create_character("Luna", "Mage")
    print(display_character(hero))
    saved = save_character(hero, "hero.txt")
    print("Saved:", saved)
    loaded = load_character("hero.txt")
    print(display_character(loaded))
    leveled = level_up(loaded)
    print(display_character(leveled))

