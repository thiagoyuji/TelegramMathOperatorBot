# Bot Telegram Letters in Expression Exception
# Autor: STNIN, Thiago Yuji
# 29/01/2019

import sys
import re as Regular_Expression

sys.path.append('./MathOperatorBot/Protocols')

from Protocols import *
from CaptureException import *

class LettersExpressionException():

    def __init__( self, expression ):

        Letters = Regular_Expression.compile(r"[a-z,A-Z]")
        validate = Regular_Expression.findall(Letters, expression)

        if( len(validate) != 0 ):

            self.protocol = Protocol.LETTERS_IN_EXPRESSION.value

            raise CaptureException( self.protocol )
