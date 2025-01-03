import random
class Thermometer():
    def __init__(self):
        self.is_on = False
        self.temp = 0
    def turn_on(self):
        self.is_on = True
        self.temp = None
        print('Thermometer is on.')
    def turn_off(self):
        self.is_on = False
        print('Thermometer is off.')
    def measure(self):
        if self.is_on:
            self.temp = round(random.uniform(34.0,42.0),1)
        else:
            print('Thermometer must be turn on.')
    def status(self):
        if not self.is_on:
            print("Thermometer is off.")
            return

        if self.temp is None:
            print("Temperature not measured yet.")
        else:
            if self.temp >= 41.0:
                print(f"Measured Temperature: {self.temp}C (CRITICAL TEMPERATURE!!)")
            elif self.temp >= 37.0:
                print(f"Measured Temperature: {self.temp}C (fever).")
            else:
                print(f"Measured Temperature: {self.temp}C.")
      
def main():
    my_thermometer = Thermometer()
    my_thermometer.turn_on()
    my_thermometer.status()
    my_thermometer.measure()
    my_thermometer.status()
    my_thermometer.turn_off()
    my_thermometer.status()

if __name__ == '__main__':
    main()