# MathOperatorBot Main
# Author STNIN, Thiago Yuji
# 27/01/2019

import sys

sys.path.append('./MathOperatorBot/Controller')

from Telegram import *

if __name__ == '__main__':

    telegram = Telegram()

    telegram.message_loop()

    while True:

        pass
