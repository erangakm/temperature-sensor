from sense_hat import SenseHat

class SenseHatSensor:
    def __init__(self):
        self.__sense = SenseHat()

    def __tempFromHumiditySensor(self):
        return self.__sense.get_temperature_from_humidity()

    def __tempFromPressureSensor(self):
        return self.__sense.get_temperature_from_pressure()

    def getTemperature(self):
        return ((self.__tempFromPressureSensor() + self.__tempFromHumiditySensor()) / 2)
