import json
from datetime import datetime
from pathlib import Path
from src.display import Display
from src.sensor import Sensor


class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None, log_file=Path("log.txt"), config_file=Path("config.json")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        self.log_file.touch(exist_ok=True)

    def __str__(self):
        return f"Location: {self.location}, Capacity: {self}"

    def register(self,component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self._log_car_activity(plate, "entered")
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self._log_car_activity(plate, "exited")
        self.update_displays()

    @property
    def available_bays(self):
        if self.capacity - len(self.plates) < 0:
            return 0
        else:
            return self.capacity - len(self.plates)

    def update_displays(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        data = {"available_bays": self.available_bays, "temperature": 25, "time": current_time}
        for display in self.displays:
            display.update(data)

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def write_config(self):
        with open(self.config_file, "w") as f: # TODO: use self.config_file; use Path; add optional parm to __init__
            json.dump({"location": self.location,
                           "capacity": self.capacity,
                           "log_file": str(self.log_file)}, f)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])
