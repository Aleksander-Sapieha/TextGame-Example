import engine

print("Commands: ")
print("1. quit (Quits the game)")
print("2. go <direction> (Goes to the desired direction)")
print("3. take <item> (Picks up an item)")
print("4. drop <item> (Drops an item)")
print("5. inventory (Displays inventory)")
print("6. save (Saves the game)")
print("7. load (Loads the game)")

world_data = {
    "start": {
        "description": "You are in a dark room. Exits are north and east.",
        "connections": {"north": "hallway", "east": "closet"},
        "items": ["torch"]
    },
    "hallway": {
        "description": "A long hallway with a locked door to the north.",
        "connections": {"south": "start", "north": "boss_room"},
        "items": ["key"],
        "locked": False
    },
    "closet": {
        "description": "A small closet with a puzzle on the wall.",
        "connections": {"west": "start"},
        "items": [],
        "puzzle": {
            "question": "What has keys but can't open locks?",
            "answer": "piano",
            "reward": "gold coin"
        }
    },
    "boss_room": {
        "description": "The lair of the Goblin King.",
        "connections": {"south": "hallway"},
        "enemy": {"name": "Goblin King", "health": 50, "attack_power": 15},
        "locked": True,
        "key": "key"
    }
}


if __name__ == "__main__":
    Engine = engine.TextGameEngine()
    Engine.load_world(world_data)
    Engine.main_loop()
