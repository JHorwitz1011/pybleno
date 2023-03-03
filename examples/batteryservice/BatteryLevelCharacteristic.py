from pybleno import *
import array
import sys
import subprocess
import re

class BatteryLevelCharacteristic(Characteristic):
    def __init__(self):
        Characteristic.__init__(self, {
            'uuid': '2A19',
            'properties': ['read'],
            'value': None,
            'descriptors': [
                  Descriptor({
                    'uuid': '2901',
                    'value': 'Battery level between 0 and 100 percent'
                  }),
                  Descriptor({
                    'uuid': '2904',
                    'value': array.array('B', [0x04, 0x01, 0x27, 0xAD, 0x01, 0x00, 0x00 ]) # maybe 12 0xC unsigned 8 bit
                  })
                ]            
          })
          
        self._value = array.array('B', [0] * 0)
        self._updateValueCallback = self.test()
    def test(self):
       print('DSFOIY ETSID&^FYU SDGUIKISDFGSDYIKFHB')
    def onReadRequest(self, offset, callback):
      callback(Characteristic.RESULT_SUCCESS, array.array('B', [98]))

