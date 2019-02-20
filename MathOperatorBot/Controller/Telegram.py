# MathOperatorBot Telegram Controller
# Author STNIN, Thiago Yuji
# 27/01/2019

import sys
import os
import telepot

sys.path.append('./MathOperatorBot/')
sys.path.append('./MathOperatorBot/Commands')

from Data import *
from Events import *

class Telegram():

    def __init__( self ):

        self.bot_token = os.environ["CHAVE_TELEGRAM_BOT"]

        self.bot = telepot.Bot( self.bot_token )

    def request( self, json_info ):

        print("[API] Message Request Received", json_info['text'])

        separate_data = Data( json_info['text'] )

        evt = Events( separate_data )
        result = evt.get_response()

        self.response( json_info, result )

    def response( self, json_info, response_message ):

        chat_id = json_info['chat']['id']
        self.bot.sendMessage(chat_id, response_message)

    def message_loop( self ):

        self.bot.message_loop( self.request )
