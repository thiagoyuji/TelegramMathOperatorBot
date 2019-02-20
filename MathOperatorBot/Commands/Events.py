# MathOperatorBot Commands React
# Author STNIN, Thiago Yuji
# 27/01/2019

from Start import *
from Help import *
from Math import *
from CommandsEnum import *

class Events():

    def __init__( self, data ):

        self.data = data

        expression = self.data.get_parameter()

        self.commands_event = {CommandsEnum.start.value: Start(),
                               CommandsEnum.help.value: Help(),
                               CommandsEnum.math.value: Math( expression )}

        self.response = ""

    def get_response( self ):

        command = self.data.get_command()

        self.response = self.commands_event[command]

        del self.commands_event

        return self.response.get_response()
