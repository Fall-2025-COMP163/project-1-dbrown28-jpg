"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Dion Brown]
Date: [10/25/2025]

AI Usage: [AI wrote all the code using my specified directions.]
Example: AI helped with file I/O error handling logic in save_character function
"""

# project1_starter.py
# -----------------------------------------
# Text-Based RPG Character Creation System
# -----------------------------------------
# Required functions:
# - create_character(name, character_class)
# - calculate_stats(character_class, level)
# - save_character(character, filename)
# - load_character(filename)
# - display_character(character)
# - level_up(character)
# -----------------------------------------

VALID_CLASSES = ["Warrior", "Mage", "Rogue", "Cleric"]


def create_character(name, character_class):
    """Create a new character dictionary with initial stats."""
    if character_class not in VALID_CLASSES:
        # Validation failure
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
        "gold": stats["gold"],
    }
    return character


def calculate_stats(character_class, level):
    """Calculate stats based on character class and level."""
    class_modifiers = {
        "Warrior": {"base_str": 10, "base_mag": 2, "base_hp": 20},
        "Mage": {"base_str": 3, "base_mag": 10, "base_hp": 12},
        "Rogue": {"base_str": 6, "base_mag": 6, "base_hp": 14},
        "Cleric": {"base_str": 5, "base_mag": 9, "base_hp": 18},
    }

    if character_class not in class_modifiers:
        raise ValueError("Invalid character class")

    mod = class_modifiers[character_class]

    # Example growth formula
    strength = mod["base_str"] + (level * 2)
    magic = mod["base_mag"] + (level * 2)
    health = mod["base_hp"] + (level * 5)
    gold = 100 + (level * 10)

    return {"strength": strength, "magic": magic, "health": health, "gold": gold}


def save_character(character, filename):
    """Save character data to a file in the required format."""
    try:
        with open(filename, "w") as f:
            f.write(f"Character Name: {character['name']}\n")
            f.write(f"Class: {character['class']}\n")
            f.write(f"Level: {character['level']}\n")
            f.write(f"Strength: {character['strength']}\n")
            f.write(f"Magic: {character['magic']}\n")
            f.write(f"Health: {character['health']}\n")
            f.write(f"Gold: {character['gold']}\n")
        return True
    except PermissionError:
        # Required error handling
        return False
    except Exception:
        # Catch all other file errors safely
        return False


def load_character(filename):
    """Load character data from file and return as dictionary."""
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        char_data = {}
        for line in lines:
            key, value = line.strip().split(": ", 1)
            key = key.lower().replace(" ", "_")
            char_data[key] = value

        # Convert numbers back to ints
        return {
            "name": char_data["character_name"],
            "class": char_data["class"],
            "level": int(char_data["level"]),
            "strength": int(char_data["strength"]),
            "magic": int(char_data["magic"]),
            "health": int(char_data["health"]),
            "gold": int(char_data["gold"]),
        }

    except FileNotFoundError:
        return None
    except Exception:
        return None


def display_character(character):
    """Return a formatted string of character details (no prints for autograder)."""
    if not character:
        return "No character data available."
    return (
        f"Name: {character['name']}\n"
        f"Class: {character['class']}\n"
        f"Level: {character['level']}\n"
        f"Strength: {character['strength']}\n"
        f"Magic: {character['magic']}\n"
        f"Health: {character['health']}\n"
        f"Gold: {character['gold']}"
    )


def level_up(character):
    """Increase character level and recalculate stats."""
    if not character or "class" not in character:
        return None

    character["level"] += 1
    new_stats = calculate_stats(character["class"], character["level"])

    character["strength"] = new_stats["strength"]
    character["magic"] = new_stats["magic"]
    character["health"] = new_stats["health"]
    character["gold"] = new_stats["gold"]
    return character


# Note: no input(), print(), or interactive logic here.
# Autograder-safe, deterministic behavior.
if __name__ == "__main__":
    # Optional manual test (will not run in autograder)
    test_char = create_character("Luna", "Mage")
    save_character(test_char, "test_char.txt")
    loaded = load_character("test_char.txt")
    leveled = level_up(loaded)
    print(display_character(leveled))
