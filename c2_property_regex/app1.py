class Temp():
    _unit = "Kelvin"
    current_unit = "Kelvin"
    conversion = {'Celsius': 273.5, 'Kelvin': 0}

    def __init__(self, temp):
        self._temp = temp


    def substract_temp(self, value):

        if value >= self._temp:
            raise Exception
        self._temp -= value

    def change_unit(self, unit):
        self.current_unit = unit
    @property
    def temperature(self):
        return self._temp - self.conversion[self.current_unit]
    @temperature.setter
    def temperature(self, value):
        self._temp = value + self.conversion[self.current_unit]
    @temperature.deleter
    def temperature(self):
        self._temp = 0


temp=Temp(10)
print(temp.temperature)
temp.change_unit('Celsius')
print(temp.temperature)
temp.substract_temp(1)
print(temp.temperature)