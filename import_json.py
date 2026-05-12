import json
import os

# Default Directory & File
DEFAULT_DIR  = "/Users/gregoriotovar/Library/CloudStorage/GoogleDrive-gregtovar@gmail.com/My Drive/A_Lyfter/Programs/"
DEFAULT_FILE = "pokemon.json"


#
#
# Returns a dictionary with ANSI color codes.
#
#
def color_setup() -> dict:
    return {
        "GREEN":      "\033[92m",
        "DARK_GREEN": "\033[32m",
        "RED":        "\033[91m",
        "YELLOW":     "\033[93m",
        "BLUE":       "\033[94m",
        "RESET":      "\033[0m",
    }


#
#
# Prints the program header.
#
#
def print_header(colors: dict) -> None:
    print(f"{colors['DARK_GREEN']}")
    print("=" * 55)
    print("      🐾 Pokémon Reader — Filter by Generation")
    print("=" * 55)


#
#
# Shows the default directory and lets the user keep it or enter a custom one.
#
#
def ask_directory(colors: dict) -> str:
    print(f"\n{colors['BLUE']}📁 Default working directory:")
    print(f"   {DEFAULT_DIR}{colors['DARK_GREEN']}\n")

    print(f"   {colors['YELLOW']}Enter 0{colors['DARK_GREEN']} to keep the default directory.")
    print(f"   {colors['YELLOW']}Enter 1{colors['DARK_GREEN']} to use a different directory.\n")

    while True:
        choice = input("🔷 Your choice (0 or 1): ").strip()

        if choice == "0":
            print(f"\n{colors['GREEN']}✅ Using default directory.{colors['DARK_GREEN']}")
            return DEFAULT_DIR

        elif choice == "1":
            while True:
                custom_dir = input("\n🔷 Enter the full directory path: ").strip()

                if not custom_dir:
                    print(f"{colors['RED']}❌ Directory cannot be empty. Try again.{colors['DARK_GREEN']}")
                    continue

                if not custom_dir.endswith("/"):
                    custom_dir += "/"

                print(f"\n{colors['GREEN']}✅ Using custom directory: {custom_dir}{colors['DARK_GREEN']}")
                return custom_dir

        else:
            print(f"{colors['RED']}❌ Invalid choice. Please enter 0 or 1.{colors['DARK_GREEN']}")


#
#
# Asks the user which generation to filter by, or 0 to show all.
#
#
def ask_generation(colors: dict) -> int | None:
    print(f"\n{colors['BLUE']}ℹ️  Available generations: 1 (1996)  2 (1999)  3 (2002)")
    print(f"                          4 (2006)  5 (2010)  6 (2013)")
    print(f"   Enter 0 to show ALL Pokémon.{colors['DARK_GREEN']}\n")

    while True:
        choice = input("🔷 Filter by generation (0–6): ").strip()

        if not choice.isdigit() or int(choice) > 6:
            print(f"{colors['RED']}❌ Please enter a number between 0 and 6.{colors['DARK_GREEN']}")
            continue

        selection = int(choice)
        if selection == 0:
            print(f"\n{colors['GREEN']}✅ Showing ALL Pokémon.{colors['DARK_GREEN']}")
        else:
            print(f"\n{colors['GREEN']}✅ Filtering by Generation {selection}.{colors['DARK_GREEN']}")

        return selection


#
#
# Loads and parses the JSON file. Returns None on error.
#
#
def load_json(filepath: str, colors: dict) -> dict | None:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"\n{colors['GREEN']}✅ Loaded '{filepath}'{colors['DARK_GREEN']}")
        return data
    except FileNotFoundError:
        print(f"{colors['RED']}❌ Error: File not found at '{filepath}'{colors['DARK_GREEN']}")
        return None
    except json.JSONDecodeError as e:
        print(f"{colors['RED']}❌ Error: Could not parse JSON — {e}{colors['DARK_GREEN']}")
        return None


#
#
# Returns all Pokémon, or only those matching the given generation.
#
#
def filter_pokemon(data: dict, generation: int) -> list[dict]:
    if "pokemon" not in data:
        print(f"❌ Error: JSON file does not contain a 'pokemon' key.")
        print(f"   Keys found in file: {list(data.keys())}")
        return []

    all_pokemon = data["pokemon"]

    if generation == 0:
        return all_pokemon

    return [p for p in all_pokemon if p["generation"] == generation]


#
#
# Prints the filtered Pokémon list in a formatted table.
#
#
def print_results(pokemon_list: list[dict], generation: int, colors: dict) -> None:
    if not pokemon_list:
        print(f"\n{colors['YELLOW']}⚠️  No Pokémon found for Generation {generation}.{colors['DARK_GREEN']}")
        return

    label = "ALL Generations" if generation == 0 else f"Generation {generation}"
    print(f"\n{colors['BLUE']}{'=' * 45}")
    print(f"  🐾 Pokémon — {label}  ({len(pokemon_list)} found)")
    print(f"{'=' * 45}{colors['DARK_GREEN']}")
    print(f"  {'#':<5} {'Name':<15} {'Year':<8} {'Gen'}")
    print(f"  {'-'*5} {'-'*15} {'-'*8} {'-'*4}")

    for p in pokemon_list:
        print(f"  {p['id']:<5} {p['name']:<15} {p['year']:<8} {p['generation']}")

    print(f"{colors['BLUE']}{'=' * 45}{colors['DARK_GREEN']}")


#
#
# Entry point of the program.
#
#
def main() -> None:
    colors = color_setup()
    print_header(colors)

    directory  = ask_directory(colors)
    filepath   = os.path.join(directory, DEFAULT_FILE)
    generation = ask_generation(colors)
    data       = load_json(filepath, colors)

    if data is not None:
        pokemon_list = filter_pokemon(data, generation)
        print_results(pokemon_list, generation, colors)

    print(colors["RESET"])


if __name__ == "__main__":
    main()