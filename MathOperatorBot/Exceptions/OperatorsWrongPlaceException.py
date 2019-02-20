# Bot Telegram Operators in wrong Place in Expression
# Autor: STNIN, Thiago Yuji
# 29/01/2019

import sys
import re as Regular_Expression

sys.path.append('./MathOperatorBot/Protocols')

from Protocols import *
from CaptureException import *

class OperatorsWrongPlaceException():

    def __init__( self, expression ):

        InvalidNumberParentesis = Regular_Expression.compile(r"((\([*,/,%])|(\([ ]+[*,/,%]))|(([+,\-,*,/,%]\))|([+,\-,*,/,%][ ]+\)))")
        validate = Regular_Expression.findall(InvalidNumberParentesis, expression)

        if( len(validate) != 0 ):

            self.protocol = Protocol.OPERATORS_IN_WRONG_PLACE.value

            raise CaptureException( self.protocol )
