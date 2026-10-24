def intro():
    print("Welcome to the Dungeon Adventure!")
    print("You must make choices to survive and find the hidden treasure.")


def show_room(room):
    print(f"\nYou are in the {room['name']}.")
    print(room["description"])

    for index, option in enumerate(room["choices"], start=1):
        print(f"{index}. {option['text']}")


def get_choice(room):
    while True:
        choice = input("Choose an option: ")
        if choice.isdigit():
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(room["choices"]):
                return choice_index
        print("Invalid choice. Please try again.")


def play_game():
    health = 10
    inventory = []
    current_room = "entrance"

    rooms = {
        "entrance": {
            "name": "Dungeon Entrance",
            "description": "A stone gate stands before you. The air smells of old treasure and danger.",
            "choices": [
                {"text": "Enter the torch-lit hallway", "next": "hallway"},
                {"text": "Search the crates by the gate", "next": "crates"},
            ],
        },
        "hallway": {
            "name": "Torch-lit Hallway",
            "description": "Candles flicker along the walls. A rusty key lies on the floor.",
            "choices": [
                {"text": "Take the key and continue forward", "next": "vault"},
                {"text": "Return to the entrance", "next": "entrance"},
            ],
        },
        "crates": {
            "name": "Old Crates",
            "description": "You find a small healing potion and a torn map.",
            "choices": [
                {"text": "Take the potion and continue", "next": "vault"},
                {"text": "Ignore the supplies and leave", "next": "entrance"},
            ],
        },
        "vault": {
            "name": "Treasure Vault",
            "description": "A glowing chest sits in the center of the room. The final decision is before you.",
            "choices": [
                {"text": "Open the chest", "next": "ending"},
                {"text": "Leave the treasure behind", "next": "ending"},
            ],
        },
    }

    intro()

    while current_room != "ending":
        room = rooms[current_room]
        show_room(room)
        option_index = get_choice(room)
        next_room = room["choices"][option_index]["next"]
        current_room = next_room

        if current_room == "vault":
            print("You are getting closer to the treasure...")

    print("\nThe adventure ends here.")
    print("Your story is complete. Try again and choose a different path!")


if __name__ == "__main__":
    play_game()
