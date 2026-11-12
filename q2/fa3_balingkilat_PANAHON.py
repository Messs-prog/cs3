from abc import ABC, abstractmethod

class Sensor(ABC):
  @abstractmethod
  def get_reading(self):
    pass

class TempSensor(Sensor):
    def get_reading(self):
        return "24.5°C"

class PHSensor(Sensor):
    def get_reading(self):
        return "7.2 pH (Neutral)"
    
tpsensor = TempSensor()
phsensor = PHSensor()
print ("--- Lab Inventory System ---")
print(f'[pH Sensor] Reading: {phsensor.get_reading()}')
print(f'[Temperature Sensor] Reading: {tpsensor.get_reading()}')
print("----------------------------")
