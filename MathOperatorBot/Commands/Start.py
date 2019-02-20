# Bot Telegram Command Start
# Author: STNIN, Thiago Yuji
# 28/01/2019

from I_Commands import *

class Start(I_Commands):

    def __init__( self ):

        self.response_message = "Ola,\nBem Vindos \'Caras Palidas\'"

    def get_response( self ):

        print("[API] Start Message Sent", "\n")

        return self.response_message
