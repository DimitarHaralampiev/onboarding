class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def description_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_range(self, range):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = 'This car can go approximately ' + str(range)
        message += 'miles on a full charge'
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar:
    def __init__(self):
        self.battery_size = 60
        self.battery = Battery()


el_car = ElectricCar()
el_car.battery.get_range(80)
el_car.battery.upgrade_battery()
el_car.battery.get_range(100)
