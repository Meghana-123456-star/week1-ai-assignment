import json
from datetime import datetime

print("Welcome to Smart Student Assistant")

name = input("Enter your name: ")
print(f"Hello {name}! 👋")

# Load tips from JSON (if exists)
try:
    with open("tips.json", "r") as file:
        data = json.load(file)
except:
    data = {
        "tips": [
            "Study 2 hours daily",
            "Revise regularly",
            "Practice coding problems"
        ],
        "quotes": [
            "Success is consistency.",
            "Stay focused and never give up.",
            "Hard work beats talent."
        ]
    }

while True:
    print("\n--- MENU ---")
    print("1. Generate Study Tips")
    print("2. Generate Motivation Quote")
    print("3. Display Date & Time")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Tip:", data["tips"][0])

    elif choice == "2":
        print("Quote:", data["quotes"][0])

    elif choice == "3":
        print("Now:", datetime.now())

    elif choice == "4":
        break

    else:
        print("Invalid choice")

    with open("output.txt", "a") as file:
        file.write(f"{choice} executed\n")