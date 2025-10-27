"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Dion Brown]
Date: [10/27/2025]

AI Usage: [AI wrote all the code using my specified directions.]
"""

# project1_starter.py

# ----------------------------
# Character Creation Functions
# ----------------------------

def calculate_stats(character_class, level):
    """Calculate stats based on character class and level.
    Returns a tuple of (strength, magic, health)."""
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
        return (0, 0, 0)

    return (strength, magic, health)


def create_character(name, character_class):
    """Create a new character dictionary."""
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class not in valid_classes:
        return None

    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    gold = 100 + (level * 10)  # starting gold

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


# ----------------------------
# File I/O Functions
# ----------------------------

def save_character(character, filename):
    """Save character to file in the required format.
    Returns True if saved, False if directory or permission issues."""
    if character is None or filename == "":
        return False

    # Build file contents
    content = (
        f"Character Name: {character['name']}\n"
        f"Class: {character['class']}\n"
        f"Level: {character['level']}\n"
        f"Strength: {character['strength']}\n"
        f"Magic: {character['magic']}\n"
        f"Health: {character['health']}\n"
        f"Gold: {character['gold']}\n"
    )

    # Check if we can open file for writing
    try:
        f = open(filename, 'w')
        f.write(content)
        f.close()
        return True
    except (FileNotFoundError, PermissionError):
        return False


def load_character(filename):
    """Load a character from a file. Returns the character dictionary or None if error."""
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        return None
    except PermissionError:
        return None

    lines = f.readlines()
    f.close()

    if len(lines) < 7:
        return None

    # Parse the character
    character = {}
    for line in lines:
        key_value = line.strip().split(": ", 1)
        if len(key_value) != 2:
            continue
        key, value = key_value
        if key == "Character Name":
            character["name"] = value
        elif key == "Class":
            character["class"] = value
        elif key == "Level":
            character["level"] = int(value)
        elif key == "Strength":
            character["strength"] = int(value)
        elif key == "Magic":
            character["magic"] = int(value)
        elif key == "Health":
            character["health"] = int(value)
        elif key == "Gold":
            character["gold"] = int(value)

    # Validate class
    if character.get("class") not in ["Warrior", "Mage", "Rogue", "Cleric"]:
        return None

    return character


# ----------------------------
# Character Display and Leveling
# ----------------------------

def display_character(character):
    """Print character info in readable format. Returns None."""
    if character is None:
        return None

    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    return None


def level_up(character):
    """Increase character level by 1 and recalculate stats."""
    if character is None:
        return None

    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["gold"] = 100 + (character["level"] * 10)
    return character
