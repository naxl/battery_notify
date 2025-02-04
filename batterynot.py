from psutil import sensors_battery
from plyer import notification
from time import sleep
from os import path
def gbs():
    b = sensors_battery()
    pl = b.power_plugged
    p = b.percent
    return pl, p
m4 = "Your battery is fully charged. Please unplug your charger to extend battery life."
m3 = "Charge is at 70 or less. Plug for consistent performance!"
m2 = "Your battery is at charge 40 or below. Please plug your charger to increase performance."
m = "Your battery is at charge 25 or below. Please plug your charger immediately!"
t4 = "Unplug Charger Reminder!"
t3 = "Plug Charger Reminder!"
t2 = "Plug Charger Reminder!"
t = "Plug Charger Immediately"
base= path.dirname(path.abspath(__file__))
i4 = path.join(base, 'icons', 'i4.ico')
i3 = path.join(base, 'icons', 'i3.ico')
i2 = path.join(base, 'icons', 'i2.ico')
i = path.join(base, 'icons', 'i.ico')
def n4(ms, ti):
    notification.notify(
        title=ti,
        message=ms,
        timeout=10,
        app_icon=i4
    )
def n3(ms, ti):
    notification.notify(
        title=ti,
        message=ms,
        timeout=10,
        app_icon=i3
    )
def n2(ms, ti):
    notification.notify(
        title=ti,
        message=ms,
        timeout=10,
        app_icon=i2
    )
def n(ms, ti):
    notification.notify(
        title=ti,
        message=ms,
        timeout=10,
        app_icon=i
    )
def main():
    while True:
        pl, p = gbs()
        if not pl and p <=25:
            n(m,t)
        if not pl and p <=40:
            n2(m2,t2)
        if not pl and p <= 70:
            n3(m3,t3)
        if pl and p >= 99:
            n4(m4,t4)
        sleep(40)
if __name__ == "__main__":
    main()
