# Bot Telegram # Enum Commands
# Author: STNIN, Thiago Yuji
# 28/01/2019

from enum import Enum

class NoValue(Enum):

    def __repr__( self ):
        return '<%S.%S>' % (self.__class__.__name__, self.name)


class CommandsEnum(NoValue):

    start = '/start'
    help = '/help'
    math = '/math'
