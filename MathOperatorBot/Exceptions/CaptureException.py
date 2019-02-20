# Bot Telegram Capture Exception
# Autor: STNIN, Thiago Yuji
# 29/01/2019

class CaptureException( Exception ):

    def __init__( self, protocol ):

        self.protocol = protocol

    def get_protocol( self ):

        return self.protocol
