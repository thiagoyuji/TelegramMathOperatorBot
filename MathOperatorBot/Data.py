# MathOperatorBot Separate Data Info
# Author STNIN, Thiago Yuji
# 28/01/2019

class Data():

    def __init__( self, message ):

        texts = message.split( ' ' )
        self.command = texts[0]

        text = message.replace( self.command, '' )
        self.parameter = text

    def get_command( self ):

        return self.command

    def get_parameter( self ):

        return self.parameter
