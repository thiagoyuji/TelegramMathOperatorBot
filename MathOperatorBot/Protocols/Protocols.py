# MathOperatorBot Protocols
# Author STNIN, Thiago Yuji
# 28/01/2019

from enum import Enum

class NoValue(Enum):

    def __repr__( self ):
        return '<%S.%S>' % (self.__class__.__name__, self.name)


class Protocol(NoValue):

    EXPRESSION_EMPTY = 'Expressao Invalida: Expressao Matematica em Branco'
    LETTERS_IN_EXPRESSION = 'Expressao Invalida: Letras na Expressao Matematica'
    PARENTESIS_INVALID = 'Expressao Invalida: Faltando Abertura e/ou Fechamento de Parenteses'
    SYMBOLS_IN_EXPRESSION = 'Expressao Invalida: Simbolos Incorretos na Expressao Matematica'
    DIVISION_BY_ZERO = 'Expressao Invalida: Ha Divisao(oes) por Zero'
    OPERATORS_IN_WRONG_PLACE = 'Expressao Invalida: Operador(es) Perto de Parenteses'
    INVALID_OPERATORS = 'Expressao Invalida: Ha Operadores Errados na Expressao Matematica'
    NUMBERS_EXPRESSION = 'Expressao Invalida: Ha Numeros perto de Parenteses sem Operador(es)'
