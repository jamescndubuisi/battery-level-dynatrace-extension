
import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent
print(percent)
print(type(percent))
plugged = "Plugged In" if plugged else "Not Plugged In"
# print(percent + '% | ' + plugged)

 # plugin_sdk simulate_plugin

