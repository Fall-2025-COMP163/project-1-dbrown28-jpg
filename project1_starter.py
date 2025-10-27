"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Dion Brown]
Date: [10/27/2025]

AI Usage: [AI wrote all the code using my specified directions.]
"""

# project1_starter.py

# ----------------------------
# Character creation functions
# ----------------------------

def create_character(name, character_class):
    """Create a new character dictionary with initial stats and level 1."""
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class not in valid_classes:
        return None  # Invalid class

    level = 1
    strength, magic, health, gold = calculate_stats(character_class, level)
    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }
    return character


def calculate_stats(character_class, level):
    """Calculate stats based on character class and level. Returns a tuple."""
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
    else:
        return (0, 0, 0, 0)

    gold = 100 + (level * 10)
    return (strength, magic, health, gold)


# ----------------------------
# File I/O functions
# ----------------------------

def save_character(character, filename):
    """Save character to a file in the required format."""
    if character is None or filename == "":
        return False
    file = None
    try:
        file = open(filename, "w")
    except:
        return False  # Handles bad directory or permission errors

    file.write("Character Name: " + character["name"] + "\n")
    file.write("Class: " + character["class"] + "\n")
    file.write("Level: " + str(character["level"]) + "\n")
    file.write("Strength: " + str(character["strength"]) + "\n")
    file.write("Magic: " + str(character["magic"]) + "\n")
    file.write("Health: " + str(character["health"]) + "\n")
    file.write("Gold: " + str(character["gold"]) + "\n")
    file.close()
    return True


def load_character(filename):
    """Load character from a file. Return character dictionary or None if file missing."""
    if filename == "":
        return None
    file = None
    try:
        file = open(filename, "r")
    except:
        return None  # File not found or bad directory

    lines = file.readlines()
    file.close()
    if len(lines) < 7:
        return None

    data = {}
    for line in lines:
        if ": " in line:
            key, value = line.strip().split(": ", 1)
            data[key.lower().replace(" ", "_")] = value

    try:
        character = {
            "name": data["character_name"],
            "class": data["class"],
            "level": int(data["level"]),
            "strength": int(data["strength"]),
            "magic": int(data["magic"]),
            "health": int(data["health"]),
            "gold": int(data["gold"])
        }
    except:
        return None

    return character


# ----------------------------
# Display and progression
# ----------------------------

def display_character(character):
    """Display character info. Returns None."""
    if character is None:
        print("Error: Invalid character.")
        return None
    print("Name:", character["name"])
    print("Class:", character["class"])
    print("Level:", character["level"])
    print("Strength:", character["strength"])
    print("Magic:", character["magic"])
    print("Health:", character["health"])
    print("Gold:", character["gold"])
    return None


def level_up(character):
    """Increase character level by 1 and update stats."""
    if character is None:
        return None
    character["level"] += 1
    strength, magic, health, gold = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["gold"] = gold
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

