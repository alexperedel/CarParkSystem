from datetime import datetime

from src.display import Display
from src.sensor import Sensor


class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

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
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
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

