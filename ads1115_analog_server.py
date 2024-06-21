import logging
import busio
import digitalio
import board
import microcontroller
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time
import httplib2
http=httplib2.Http()
from kalliope.core.NeuronModule import NeuronModule, MissingParameterException, InvalidParameterException

logging.basicConfig()
logger = logging.getLogger("kalliope")

# Initialize the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)
# Create an ADS1115 object
ads = ADS.ADS1115(i2c)

analog_value1 = 0
analog_value2 = 0
analog_value3 = 0
analog_value4 = 0

class Ads1115_analog_server(NeuronModule):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.readChannel = kwargs.get('readChannel', None)

        if self.readChannel is None:
            raise InvalidParameterException("analog channel must be provided")
        
        channel0 = AnalogIn(ads, ADS.P0)
        analog_value1 = channel0.value        
        nilai1 = str(analog_value1)
        channel1 = AnalogIn(ads, ADS.P1)
        analog_value2 = channel1.value        
        nilai2 = str(analog_value2)
        channel2 = AnalogIn(ads, ADS.P2)
        analog_value3 = channel2.value        
        nilai3 = str(analog_value3)
        channel3 = AnalogIn(ads, ADS.P3)
        analog_value4 = channel3.value        
        nilai4 = str(analog_value4)
        #self.say(nilai4)
        #logger.info(nilai4)

        content =http.request("http://xxx.xxx.xxx.xxx/datasensor/terimaanalog.php?sensor1="+nilai1+"&sensor2="+nilai2+"&sensor3="+nilai3+"&sensor4="+nilai4, method="GET")[1]
        time.sleep(1)

