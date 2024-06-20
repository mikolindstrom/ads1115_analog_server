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

channel=[]
baca=[]
nilai=[]

class Ads1115_analog_server(NeuronModule):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.readChannel = kwargs.get('readChannel', None)

        if self.readChannel is None:
            raise InvalidParameterException("analog channel must be provided")
        self.assign_variables()

    def assign_variables(self):
        for i, number in enumerate(self.readChannel):
            setattr(self, f'number_{i+1}', number)
            channel.append(number)
        self.display_results()
        
    def display_results(self):
        for i in range(len(self.numbers)):
            nilai.append = AnalogIn(ads, channel[i])
            baca.append = nilai[i].value

        nilai1 = str(baca[0])
        nilai2 = str(baca[1])
        nilai3 = str(baca[2])
        nilai4 = str(baca[3])
        content =http.request("http://xxx.xxx.xxx.xxx/datasensor/terimasuhu.php?sensor1="+nilai1+"&sensor2="+nilai2, +"&sensor3="+nilai3,+"&sensor4="+nilai4, method="GET")[1]
    
        logger.info(message)
        
        
        time.sleep(0.2)

