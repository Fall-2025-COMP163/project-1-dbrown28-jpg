"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Dion Brown]
Date: [10/27/2025]

AI Usage: [AI wrote all the code using my specified directions.]
Example: AI helped with file I/O error handling logic in save_character function
"""

# project1_starter.py
# ------------------------------------------------
# Text-Based RPG Character Creation and Story Progression System
# Demonstrates mastery of functions and file I/O operations
# ------------------------------------------------

VALID_CLASSES = ["Warrior", "Mage", "Rogue", "Cleric"]


# ------------------------------------------------
# Create Character
# ------------------------------------------------
def create_character(name, character_class):
    """Create a new character with base stats."""
    if character_class not in VALID_CLASSES:
        return None  # invalid class

    level = 1
    stats = calculate_stats(character_class, level)

    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": stats["strength"],
        "magic": stats["magic"],
        "health": stats["health"],
        "gold": stats["gold"],
    }


# ------------------------------------------------
# Calculate Stats
# ------------------------------------------------
def calculate_stats(character_class, level):
    """Calculate stats using a class-based growth system."""
    base_stats = {
        "Warrior": {"str": 12, "mag": 3, "hp": 30, "growth": 2.0},
        "Mage": {"str": 3, "mag": 12, "hp": 20, "growth": 1.6},
        "Rogue": {"str": 8, "mag": 8, "hp": 18, "growth": 1.8},
        "Cleric": {"str": 7, "mag": 11, "hp": 28, "growth": 1.5},
    }

    if character_class not in base_stats:
        raise ValueError("Invalid character class for stats.")

    base = base_stats[character_class]
    growth = base["growth"]

    strength = int(base["str"] + level * growth)
    magic = int(base["mag"] + level * growth)
    health = int(base["hp"] + level * growth * 5)
    gold = 100 + (level * 10)

    return {"strength": strength, "magic": magic, "health": health, "gold": gold}


# ------------------------------------------------
# Save Character
# ------------------------------------------------
def save_character(character, filename):
    """
    Save character info to a text file in exact format.
    Returns True if successful, False if failed due to bad path or permissions.
    """
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

    except FileNotFoundError:
        # bad directory path (e.g., /invalid/path/)
        return False
    except PermissionError:
        # permission denied (e.g., writing to system directory)
        return False
    except OSError:
        # generic I/O error (covers bad directory or write failures)
        return False
    except Exception:
        # safeguard against any unforeseen issue
        return False


# ------------------------------------------------
# Load Character
# ------------------------------------------------
def load_character(filename):
    """
    Load character from a file and return as a dictionary.
    Returns None if file not found or if contents invalid.
    """
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        data = {}
        for line in lines:
            if ": " in line:
                key, value = line.strip().split(": ", 1)
                data[key.lower().replace(" ", "_")] = value

        # Convert string fields to appropriate types
        return {
            "name": data["character_name"],
            "class": data["class"],
            "level": int(data["level"]),
            "strength": int(data["strength"]),
            "magic": int(data["magic"]),
            "health": int(data["health"]),
            "gold": int(data["gold"]),
        }

    except FileNotFoundError:
        # Missing file (must return None)
        return None
    except PermissionError:
        # Can't read file due to permissions
        return None
    except (ValueError, KeyError):
        # Bad file format or missing fields
        return None
    except Exception:
        # Any other unexpected issue
        return None


# ------------------------------------------------
# Display Character
# ------------------------------------------------
def display_character(character):
    """Return a string representation of the character (no print)."""
    if not character:
        return "Error: Character data unavailable."

    return (
        f"Name: {character['name']}\n"
        f"Class: {character['class']}\n"
        f"Level: {character['level']}\n"
        f"Strength: {character['strength']}\n"
        f"Magic: {character['magic']}\n"
        f"Health: {character['health']}\n"
        f"Gold: {character['gold']}"
    )


# ------------------------------------------------
# Level Up
# ------------------------------------------------
def level_up(character):
    """Increase the character’s level and recalculate stats."""
    if not character or "class" not in character:
        return None

    character["level"] += 1
    new_stats = calculate_stats(character["class"], character["level"])

    character["strength"] = new_stats["strength"]
    character["magic"] = new_stats["magic"]
    character["health"] = new_stats["health"]
    character["gold"] = new_stats["gold"]
    return character


# ------------------------------------------------
# Optional: Simple Story Progression (for creativity)
# ------------------------------------------------
def start_story(character):
    """Return a short story string instead of printing."""
    if not character:
        return "No character to begin story."

    name = character["name"]
    char_class = character["class"]

    story = (
        f"{name}, the brave {char_class}, awakens in a quiet forest.\n"
        f"A rustle in the bushes draws attention...\n"
        f"{name} prepares for the journey ahead!"
    )
    return story


# ------------------------------------------------
# Manual Run (ignored in autograder)
# ------------------------------------------------
if __name__ == "__main__":
    hero = create_character("Aria", "Warrior")
    if hero:
        # Test save with valid and invalid paths
        save_character(hero, "hero.txt")
        save_character(hero, "/invalid/path/hero.txt")  # handled gracefully

        loaded = load_character("hero.txt")
        leveled = level_up(loaded)
        print(display_character(leveled))
        print(start_story(leveled))
