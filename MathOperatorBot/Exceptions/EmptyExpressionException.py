# Bot Telegram Empty Expression Exception
# Autor: STNIN, Thiago Yuji
# 29/01/2019

import sys

sys.path.append('./MathOperatorBot/Protocols')

from Protocols import *
from CaptureException import *

class EmptyExpressionException():

    def __init__( self, expression ):

        if( expression == '' ):

            self.protocol = Protocol.EXPRESSION_EMPTY.value

            raise CaptureException( self.protocol )
