"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Dion Brown]
Date: [10/25/2025]

AI Usage: [AI wrote all the code using my specified directions.]
Example: AI helped with file I/O error handling logic in save_character function
"""

# project1_starter.py

# -----------------------------------------
# RPG Character Creation and Story System
# Demonstrates mastery of functions and file I/O
# -----------------------------------------

VALID_CLASSES = ["Warrior", "Mage", "Rogue", "Cleric"]


# ------------------------------------------------
# 1. Create Character
# ------------------------------------------------
def create_character(name, character_class):
    """Creates a new character dictionary with default level and stats."""
    if character_class not in VALID_CLASSES:
        print("Error: Invalid character class.")
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


# ------------------------------------------------
# 2. Calculate Stats
# ------------------------------------------------
def calculate_stats(character_class, level):
    """Calculates stats based on class and level."""

    # Base stat modifiers and growth rates by class
    class_data = {
        "Warrior": {"str": 10, "mag": 2, "hp": 15, "growth": 2},
        "Mage": {"str": 3, "mag": 10, "hp": 8, "growth": 1.5},
        "Rogue": {"str": 7, "mag": 5, "hp": 10, "growth": 1.8},
        "Cleric": {"str": 6, "mag": 9, "hp": 12, "growth": 1.6},
    }

    if character_class not in class_data:
        raise ValueError("Invalid class for stat calculation.")

    base = class_data[character_class]
    growth = base["growth"]

    strength = base["str"] + int(level * growth)
    magic = base["mag"] + int(level * growth)
    health = base["hp"] + int(level * growth * 5)
    gold = 50 + (level * 10)

    return {"strength": strength, "magic": magic, "health": health, "gold": gold}


# ------------------------------------------------
# 3. Save Character
# ------------------------------------------------
def save_character(character, filename):
    """Saves character data to file in the specified format."""
    try:
        with open(filename, "w") as f:
            f.write(f"Character Name: {character['name']}\n")
            f.write(f"Class: {character['class']}\n")
            f.write(f"Level: {character['level']}\n")
            f.write(f"Strength: {character['strength']}\n")
            f.write(f"Magic: {character['magic']}\n")
            f.write(f"Health: {character['health']}\n")
            f.write(f"Gold: {character['gold']}\n")
    except PermissionError:
        print("Error: Permission denied while saving file.")
        return False
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

    return True


# ------------------------------------------------
# 4. Load Character
# ------------------------------------------------
def load_character(filename):
    """Loads character data from file and returns a dictionary."""
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        char_data = {}
        for line in lines:
            key, value = line.strip().split(": ")
            key = key.lower().replace(" ", "_")
            char_data[key] = value

        # Convert numeric fields
        char_data["level"] = int(char_data["level"])
        char_data["strength"] = int(char_data["strength"])
        char_data["magic"] = int(char_data["magic"])
        char_data["health"] = int(char_data["health"])
        char_data["gold"] = int(char_data["gold"])

        # Rename keys for consistent format
        character = {
            "name": char_data["character_name"],
            "class": char_data["class"],
            "level": char_data["level"],
            "strength": char_data["strength"],
            "magic": char_data["magic"],
            "health": char_data["health"],
            "gold": char_data["gold"],
        }

        return character

    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print(f"Error loading character: {e}")
        return None


# ------------------------------------------------
# 5. Display Character
# ------------------------------------------------
def display_character(character):
    """Prints character information to the console."""
    if not character:
        print("No character data to display.")
        return

    print(f"\n--- Character Info ---")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("----------------------\n")


# ------------------------------------------------
# 6. Level Up
# ------------------------------------------------
def level_up(character):
    """Increases the character's level and recalculates stats."""
    if not character:
        print("Error: No character data found.")
        return None

    character["level"] += 1
    new_stats = calculate_stats(character["class"], character["level"])

    character["strength"] = new_stats["strength"]
    character["magic"] = new_stats["magic"]
    character["health"] = new_stats["health"]
    character["gold"] += 20  # Bonus for leveling up

    return character


# ------------------------------------------------
# Optional: Simple story progression system
# ------------------------------------------------
def start_story(character):
    """A short example text adventure progression."""
    print(f"\nWelcome, {character['name']} the {character['class']}!")
    print("You wake up in a misty forest with your trusty weapon at your side.\n")

    choice = input("A wild goblin appears! Do you (1) fight or (2) run? ")

    if choice == "1":
        print("You bravely face the goblin...")
        character["gold"] += 15
        print("Victory! You earn 15 gold.")
    else:
        print("You run away safely, but earn no gold.")

    print("Your journey has just begun...\n")
    return character


# ------------------------------------------------
# Example Run (for manual testing)
# ------------------------------------------------
if __name__ == "__main__":
    hero = create_character("Aria", "Warrior")
    display_character(hero)
    save_character(hero, "hero.txt")
    hero = load_character("hero.txt")
    hero = level_up(hero)
    display_character(hero)

