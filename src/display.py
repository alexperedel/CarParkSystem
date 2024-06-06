class Display:
    def __init__(self,car_park, id, message="", is_on=False):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"ID: {self.id}, Message: {self}"

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")
