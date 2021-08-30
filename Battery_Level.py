from ruxit.api.base_plugin import BasePlugin
import psutil
from ruxit.api.data import MEAttribute


class BatteryChecker(BasePlugin):
    def get_battery_data(self):
        print("starting")
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = battery.percent
        print(f"percent is {percent}")
        plugged = "True" if plugged else "False"
        return {"Level": percent, "Plugged In": plugged}

    def query(self, **kwargs):
        stats = self.get_battery_data()
        self.results_builder.absolute(key='Level', value=stats["Level"])
        self.results_builder.state_metric(key='Plugged In', value=stats["Plugged In"])
        self.results_builder.report_property(key="data", value=stats['Level'],
                                             me_attribute=MEAttribute.CUSTOM_PG_METADATA)
        # plugin_sdk simulate_plugin

