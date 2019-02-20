# Bot Telegram Invalid Operators Exception
# Autor: STNIN, Thiago Yuji
# 29/01/2019

import sys
import re as Regular_Expression

sys.path.append('./MathOperatorBot/Protocols')

from Protocols import *
from CaptureException import *

class InvalidOperatorsException():

    def __init__( self, expression ):

        InvalidOperators = Regular_Expression.compile(r"(((\+\*)[+,\-,*,\/,%]+|(\+\/)[+,\-,*,\/,%]+|(\+\%)[+,\-,*,\/,%]+)|((\-\*)[+,\-,*,\/,%]+|(\-\/)[+,\-,*,\/,%]+|(\-\%)[+,\-,*,\/,%]+)|((\*.)[+,\-,*,\/,%]+)|((\/.)[+,\-,*,\/,%]+)|([%][+,\-,*,/,%]*))|((([+,\-][*,/,^,%])|(([+,\-][ ]+[*,/,^,%])))|(([*][+,\-,/,%])|([/][+,\-,*,%])|([*][ ]+[+,\-,/,%])|([/][ ]+[+,\-,*,%]))|(([%][+,\-,*,/,%])|([%][ ]+[+,\-,*,/,%])))")
        validate = Regular_Expression.findall(InvalidOperators, expression)

        if( len(validate) != 0 ):

            self.protocol = Protocol.INVALID_OPERATORS.value

            raise CaptureException( self.protocol )
