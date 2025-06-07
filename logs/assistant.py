# assistant.py
import logging
import datetime
import threading
import operator
from weather_api import get_weather
from logger import log_operation

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': lambda a, b: a / b if b != 0 else 'Error: Division by zero'
}

def calculate(expression):
    try:
        parts = expression.split()
        a, op, b = float(parts[0]), parts[1], float(parts[2])
        if op in ops:
            result = ops[op](a, b)
            log_operation(expression, result)
            return result
        else:
            return "Error: Unsupported operation"
    except:
        return "Error: Invalid expression (use format: number op number)"

def set_reminder(task, remind_time_str):
    def reminder():
        now = datetime.datetime.now()
        
        # Parse the time string to a datetime object (today's date + given time)
        try:
            reminder_time = datetime.datetime.strptime(remind_time_str, "%H:%M")
            reminder_time = reminder_time.replace(
                year=now.year, month=now.month, day=now.day
            )
        except ValueError:
            print("Invalid time format. Use HH:MM (24-hour).")
            return

        # If the reminder time already passed today, schedule for tomorrow
        if reminder_time < now:
            reminder_time += timedelta(days=1)

        delay = (reminder_time - now).total_seconds()

        threading.Timer(delay, lambda: print(f"\n🔔 Reminder: {task}\n> ", end="")).start()
        print("Reminder set successfully.")
        logging.info(f"Reminder set: '{task}' at {remind_time_str}")
    reminder()
