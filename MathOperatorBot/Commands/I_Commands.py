# MathOperatorBot Interface Commands
# Author STNIN, Thiago Yuji
# 28/01/2019

from abc import ABCMeta, abstractmethod

class I_Commands( object ):

    @abstractmethod
    def get_response( self ): pass
