from type import TokenType
from syntaxtrees import *

globals().update(TokenType.__members__)

class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
        
    def advance(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def operand(self):
        #Grabs the operand and advances the token returning the operand
        token = self.current_token

        if token.type == LPAREN:
            self.advance(LPAREN)
            node = self.parse()
            self.advance(RPAREN)
            return node
        elif token.type == PLUS:
            self.advance(PLUS)
            return UnaryOp(token, self.operand())
        elif token.type == MINUS:
            self.advance(MINUS)
            return UnaryOp(token, self.operand())
        else:
            self.advance(INTEGER)
            return Num(token)

    def term(self):
        node = self.operand()
        while self.current_token.type in (MULTIPLY, DIVIDE):
            token = self.current_token
            if token.type == MULTIPLY:
                self.advance(MULTIPLY)                
            elif token.type == DIVIDE:
                self.advance(DIVIDE)               
            node = BinaryOp(node, token, self.operand())
        return node


    def parse(self):
        
        node = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.advance(PLUS) #Moves past the plus
            elif token.type == MINUS:
                self.advance(MINUS)
            node = BinaryOp(node, token, self.term())
        return node
