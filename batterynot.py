import psutil
from plyer import notification
import time

def get_battery_status():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    return plugged, percent

msg100 = "Your battery is fully charged. Please unplug your charger to extend battery life."
msg40 = "Your battery is at charge 40 or below. Please plug your charger to increase performance."
title100 = "Unplug Charger Reminder"
title40 = "Plug Charger Reminder"


def notify_unplug_reminder(msg, title):
    reminder_title = title
    reminder_message = msg
    reminder_timeout = 5  # seconds

    notification.notify(
        title=reminder_title,
        message=reminder_message,
        timeout=reminder_timeout
    )

def main():
    reminder_interval = 30  # seconds

    while True:
        plugged, percent = get_battery_status()

        if not plugged and percent <=40:
            notify_unplug_reminder(msg40,title40)

        if plugged and percent >= 99:
            notify_unplug_reminder(msg100,title100)

        # Check battery status every 30 seconds
        time.sleep(reminder_interval)

if __name__ == "__main__":
    main()
