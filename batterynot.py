import psutil
from plyer import notification
import time

def get_battery_status():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    return plugged, percent

def notify_unplug_reminder():
    reminder_title = "Unplug Charger Reminder"
    reminder_message = "Your battery is fully charged. Please unplug your charger to extend battery life."
    reminder_timeout = 5  # seconds

    notification.notify(
        title=reminder_title,
        message=reminder_message,
        timeout=reminder_timeout
    )

def main():
    reminder_interval = 10  # seconds

    while True:
        plugged, percent = get_battery_status()

        if plugged and percent >= 99:
            notify_unplug_reminder()

        # Check battery status every 10 seconds
        time.sleep(reminder_interval)

if __name__ == "__main__":
    main()
