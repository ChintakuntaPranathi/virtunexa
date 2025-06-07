# main.py
from assistant import calculate, set_reminder
from weather_api import get_weather

print("🤖 Virtual Assistant Started (type 'help' for commands)")

while True:
    command = input("> ").strip().lower()

    if command.startswith("calculate"):
        expr = command[len("calculate"):].strip()
        print("Result:", calculate(expr))

    elif command.startswith("remind me to"):
        try:
            parts = command[len("remind me to"):].split("at")
            task = parts[0].strip()
            time = parts[1].strip()
            set_reminder(task, time)
        except:
            print("Use format: remind me to <task> at <HH:MM>")

    elif command.startswith("weather in"):
        city = command[len("weather in"):].strip()
        print(get_weather(city))

    elif command in ("exit", "quit"):
        print("Goodbye!")
        break

    elif command == "help":
        print("""
Available Commands:
- calculate <num1> <operator> <num2>   → e.g., calculate 5 + 2
- remind me to <task> at <HH:MM>       → e.g., remind me to study at 18:30
- weather in <city>                    → e.g., weather in Mumbai
- exit                                 → to quit
""")
    else:
        print("Unknown command. Type 'help' for a list.")
