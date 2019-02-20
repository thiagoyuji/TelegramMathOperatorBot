# Bot Telegram Division by Zero Expression
# Autor: STNIN, Thiago Yuji
# 29/01/2019

import sys
import re as Regular_Expression

sys.path.append('./MathOperatorBot/Protocols')

from Protocols import *
from CaptureException import *

class DivisionZeroException():

    def __init__( self, expression ):

        self.protocol = ""

        DivisionZero = Regular_Expression.compile(r"(\/[ ]*0\.0*(?![0-9]))|(\/[ ]*0(?![\.])0*)")
        validate = Regular_Expression.findall(DivisionZero, expression)

        if( len(validate) != 0 ):

            self.protocol = Protocol.DIVISION_BY_ZERO.value

            raise CaptureException( self.protocol )
