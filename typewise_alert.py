from abc import ABC, abstractmethod

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'

#create abstract class - context for the main class
class ClassifyTemperature(ABC):
   @abstractmethod
   def classify_temperature_breach(self,coolingType, temperatureInC):
    pass
  
lowerLimit = 0
upperLimit = 0
class Passive(ClassifyTemperature):
  def classify_temperature_breach(coolingType, temperatureInC):
     if coolingType == 'PASSIVE_COOLING':
        lowerLimit = 0
        upperLimit = 35
        return infer_breach(temperatureInC, lowerLimit, upperLimit)
    
class Active(ClassifyTemperature):
  def classify_temperature_breach(coolingType, temperatureInC):
     if coolingType == 'HI_ACTIVE_COOLING':
        lowerLimit = 0
        upperLimit = 45
        return infer_breach(temperatureInC, lowerLimit, upperLimit)

class Med(ClassifyTemperature):
  def classify_temperature_breach(coolingType, temperatureInC):
     if coolingType == 'MED_ACTIVE_COOLING':
        lowerLimit = 0
        upperLimit = 40
        return infer_breach(temperatureInC, lowerLimit, upperLimit)
    
     
  def check_and_alert(alertTarget, batteryChar, temperatureInC):
   breachType =\
    ClassifyTemperature.classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
   if alertTarget == 'TO_CONTROLLER':
    send_to_controller(breachType)
   elif alertTarget == 'TO_EMAIL':
    send_to_email(breachType)


def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')


def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')
