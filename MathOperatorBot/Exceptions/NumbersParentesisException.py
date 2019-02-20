# Bot Telegram Numbers near Parentesis Exception
# Autor: STNIN, Thiago Yuji
# 29/01/2019

import sys
import re as Regular_Expression

sys.path.append('./MathOperatorBot/Protocols')

from Protocols import *
from CaptureException import *

class NumbersParentesisException():

    def __init__( self, expression ):

        Numbers = Regular_Expression.compile(r"(([0-9]\()|([0-9][ ]+\())|((\)[0-9])|(\)[ ]+[0-9]))")
        validate = Regular_Expression.findall(Numbers, expression)

        if( len(validate) != 0 ):

            self.protocol = Protocol.NUMBERS_EXPRESSION.value

            raise CaptureException( self.protocol )
