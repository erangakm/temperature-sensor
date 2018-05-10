from senseHatSensor import *

# Measure temperature and calibrate.
class Temperature:
    def __init__(self):
        self.__sensor = SenseHatSensor()
        
    # Get CPU running temperature.
    def __getCpuTemp(self):
        cpuFile = open('/sys/class/thermal/thermal_zone0/temp')
        cpuTemp = float(cpuFile.read())
        cpuTemp = cpuTemp / 1000

        cpuFile.close()
        return cpuTemp

    # Calibrate temperature because temps taken from sensors are affected
    # by CPU temperatures.
    def __calibratedTemprature(self):
        roomTemp = self.__sensor.getTemperature()
        cpuTemp = self.__getCpuTemp()

        return (roomTemp - ((cpuTemp - roomTemp) / 5.466))

    # Get ambient temperature.
    def getTemperature(self):
        return self.__calibratedTemprature()
