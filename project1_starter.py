"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Dion Brown]
Date: [10/25/2025]

AI Usage: [AI wrote all the code using my specified directions.]
Example: AI helped with file I/O error handling logic in save_character function
"""

# project1_starter.py

# -------------------------------------------------
# Text-Based RPG Character System
# -------------------------------------------------

# Function 1: Create a new character
def create_character(name, character_class):
    """Creates a new character dictionary with default level and gold."""
    level = 1
    gold = 100  # Starting gold for all players
    stats = calculate_stats(character_class, level)

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": stats["strength"],
        "magic": stats["magic"],
        "health": stats["health"],
        "gold": gold
    }
    return character


# Function 2: Calculate character stats based on class and level
def calculate_stats(character_class, level):
    """Calculates stats for a character based on class and level."""
    base_strength = base_magic = base_health = 0

    if character_class.lower() == "warrior":
        base_strength = 10
        base_magic = 2
        base_health = 12
    elif character_class.lower() == "mage":
        base_strength = 3
        base_magic = 10
        base_health = 8
    elif character_class.lower() == "rogue":
        base_strength = 6
        base_magic = 6
        base_health = 7
    elif character_class.lower() == "cleric":
        base_strength = 5
        base_magic = 8
        base_health = 10
    else:
        raise ValueError("Invalid character class!")

    # Scale stats by level
    stats = {
        "strength": base_strength + level * 2,
        "magic": base_magic + level * 2,
        "health": base_health + level * 3
    }
    return stats


# Function 3: Save character to file
def save_character(character, filename):
    """Saves the character dictionary to a text file in a specific format."""
    with open(filename, "w") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
    print(f"{character['name']} saved successfully to {filename}!")


# Function 4: Load character from file
def load_character(filename):
    """Loads a character from a file and returns a dictionary."""
    character = {}
    with open(filename, "r") as file:
        for line in file:
            key, value = line.strip().split(": ")
            key = key.replace("Character Name", "name").lower()
            if key in ["level", "strength", "magic", "health", "gold"]:
                value = int(value)
            character[key] = value
    return character


# Function 5: Display character information
def display_character(character):
    """Prints character information neatly."""
    print("\n=== CHARACTER INFO ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("======================\n")


# Function 6: Level up character
def level_up(character):
    """Increases character level by 1 and updates stats."""
    character["level"] += 1
    stats = calculate_stats(character["class"], character["level"])
    character["strength"] = stats["strength"]
    character["magic"] = stats["magic"]
    character["health"] = stats["health"]
    print(f"{character['name']} leveled up to level {character['level']}!")
    return character


# -------------------------------------------------
# Example main section for testing (you can remove this for submission)
# -------------------------------------------------
if __name__ == "__main__":
    hero = create_character("Aria", "Mage")
    display_character(hero)
    level_up(hero)
    display_character(hero)
    save_character(hero, "aria_save.txt")

    loaded_hero = load_character("aria_save.txt")
    display_character(loaded_hero)

