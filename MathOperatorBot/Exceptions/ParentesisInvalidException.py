# Bot Telegram Parentesis Invalid in Expression Exception
# Autor: STNIN, Thiago Yuji
# 29/01/2019

import sys

sys.path.append('./MathOperatorBot/Protocols')

from Protocols import *
from CaptureException import *

class ParentesisInvalidException():

    def __init__( self, expression ):

        Stack = []

        for simbol in expression:
            if(simbol == '('):
                Stack.append('(')
            elif(simbol == ')'):
                if(len(Stack) > 0):
                    Stack.pop()
                else:
                    Stack.append(')')
                    break;

        if(len(Stack) != 0):

            self.protocol = Protocol.PARENTESIS_INVALID.value

            raise CaptureException( self.protocol )
