# Bot Telegram # Command Math
# Author: STNIN, Thiago Yuji
# 28/01/2019

import sys

sys.path.append('./MathOperatorBot/Exceptions')

from Interceptor import *
from I_Commands import *

class Math(I_Commands):

    def __init__( self, expression ):

        try:

            Interceptor( expression )

        except CaptureException as exception:

            self.response_message = exception.get_protocol()

        else:

            self.response_message = "@result : " + expression + "   =   " + str( eval(expression) )

    def get_response( self ):

        print("[API] Math Result Message Sent", "\n")

        return self.response_message
