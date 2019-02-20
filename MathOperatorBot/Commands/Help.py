# Bot Telegram Command Help
# Author: STNIN, Thiago Yuji
# 28/01/2019

from I_Commands import *

class Help(I_Commands):

    def __init__( self ):

        self.response_message =("Minha Funcao: Fazer Calculos de Expressoes Matematicas\n\n"
                                "/start - Inicializa o Bot\n"
                                "/help - Mostra todos os Comandos\n\n"
                                "/math - Calcula Expressoes Matematicas\n"
                                "[5*5] ou [5 * 5] >> Operadores ['+', '-', '*', '/', '^', '%']")

    def get_response( self ):

        print("[API] Help Message Sent", "\n")

        return self.response_message
