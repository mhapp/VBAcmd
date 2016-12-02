'''
Started December 2, 2016
@author: Carl Schoonover
DAQ and scaling parameters for VBAcmd2
'''

class VBAconfig():

    def __init__(self):

        self.channels = {'aiChannelIDs': 'dev5/ai0:3',       # Laser / Force / Servo position / Optional analog input
                         'ainumchanels': 4,
                         'aoChannelIDs': 'dev5/ao0',         # Servo command
                         'diChannelIDs': 'dev5/port0/line0', # Toggle closed / open loop mode
                         'doChannelIDs': 'dev5/port1/line0', # Indicate ready state to stimulus control
                         }

        self.encoding = {'rangeServo':        [0, 30],     # measured range 0 to 30 mm        FIRGELLI
                         'rangeServoVout':    [0, 3.3],    # output signal  0 to 3.3 V           L12-30-50-12-I
                         'rangeServoSet':     [0, 30],     # travel range   0 to 30 mm        FIRGELLI
                         'rangeServoSetVcmd': [0, 5],      # command signal 0 to 5 V             L12-30-50-12-I
                         'rangeForce':        [-100, 100], # force range    -100 to 100 g     FUTEK
                         'rangeForceVout':    [-5, 5],     # output signal  -5 to +5 V           FSH02664 load cell with FUTEK QSH00602 signal conditioner in +/-5 VDC mode
                         'rangeLaser':        [0, 50],     # position range  0 to 50 mm       MICRO-EPSILON
                         'rangeLaserVout':    [1, 5],      # output signal   1V to 5V            ILD1302-50
                         }