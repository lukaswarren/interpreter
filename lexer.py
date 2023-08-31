from type import TokenType
from tokens import Token
#Here
globals().update(TokenType.__members__)

class Lexer(object):
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')
    
    def get_integer(self, text, character):
        result = character
        self.position +=1
        while self.position <= len(text)-1:
            character = text[self.position]
            if character.isdigit():
               result += character
               self.position +=1
            else:
               return result
        return result
             
    def get_next_token(self):
        text = self.text

        if self.position > len(text)-1:
            return Token(EOF, None)
        
        character = text[self.position]

        while character.isspace():
            self.position += 1
            if self.position <= len(text)-1:
                character = text[self.position]
            else:
                return Token(EOF, None)
            
        if character == '+':
            self.position +=1
            return Token(PLUS, "+")
        elif character == '-':
            self.position += 1
            return Token(MINUS, "-")
        elif character == '*':
            self.position += 1
            return Token(MULTIPLY, "*")
        elif character == '/':
            self.position += 1
            return Token(DIVIDE, "/")
        elif character == '(':
            self.position += 1
            return Token(LPAREN, "(")
        elif character == ')':
            self.position += 1
            return Token(RPAREN, ")")
        elif character.isdigit():
            result =  self.get_integer(text, character)
            return Token(TokenType.INTEGER, int(result))
        
        self.error()   
