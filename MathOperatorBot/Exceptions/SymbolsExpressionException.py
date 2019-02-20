# Bot Telegram Symbols in Expression Exception
# Autor: STNIN, Thiago Yuji
# 29/01/2019

import sys
import re as Regular_Expression

sys.path.append('./MathOperatorBot/Protocols')

from Protocols import *
from CaptureException import *

class SymbolsExpressionException():

    def __init__( self, expression ):

        Symbols = Regular_Expression.compile(r"[@,#,$,_,&,\",\',!,?,\,,~,\{,\},\[,\],;,:,|,\\,>,<,=,´,`,^]")
        validate = Regular_Expression.findall(Symbols, expression)

        if( len(validate) != 0 ):

            self.protocol = Protocol.SYMBOLS_IN_EXPRESSION.value

            raise CaptureException( self.protocol )
