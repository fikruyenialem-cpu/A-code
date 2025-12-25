# time_planner_notification.py
# Requires: pip install plyer

import time
from datetime import datetime
from plyer import notification

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

tasks = []

print("Time Planner (24-hour format HH:MM)")
print("Add tasks. Type 'done' when finished.\n")

while True:
    name = input("Task name (or 'done'): ")
    if name.lower() == "done":
        break
    t = input("Time (HH:MM): ")
    tasks.append({"name": name, "time": t, "notified": False})

print("\nPlanner running... Notifications will appear at scheduled times.")

while True:
    now = datetime.now().strftime("%H:%M")
    for task in tasks:
        if not task["notified"] and task["time"] == now:
            notify("Time Alert ⏰", f"It's time for: {task['name']}")
            task["notified"] = True
    time.sleep(30)
