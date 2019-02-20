# Bot Telegram Interceptor
# Autor: STNIN, Thiago Yuji
# 29/01/2019

from CaptureException import *

from EmptyExpressionException import *
from LettersExpressionException import *
from ParentesisInvalidException import *
from SymbolsExpressionException import *
from DivisionZeroException import *
from OperatorsWrongPlaceException import *
from InvalidOperatorsException import *
from NumbersParentesisException import *

class Interceptor():

    def __init__( self, expression ):

        try:

            EmptyExpressionException( expression )
            LettersExpressionException( expression )
            SymbolsExpressionException( expression )
            OperatorsWrongPlaceException( expression)
            InvalidOperatorsException( expression )
            NumbersParentesisException( expression )
            ParentesisInvalidException( expression )
            DivisionZeroException( expression )            

        except CaptureException as exception:

            raise CaptureException( exception.get_protocol() )
