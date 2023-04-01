#import type
INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE','EOF'

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(type= self.type, value = repr(self.value))
    
    def __repr__(self) -> str:
        return self.value.__str__()

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
        elif character.isdigit():
            result =  self.get_integer(text, character)
            return Token(INTEGER, int(result))
        
        self.error()   

class Interpreter(object):
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
        self.advance(INTEGER)
        return token.value

    def term(self):
        result = self.operand()
        while self.current_token.type in (MULTIPLY, DIVIDE):
            token = self.current_token
            if token.type == MULTIPLY:
                self.advance(MULTIPLY)
                result = result * self.operand()
            elif token.type == DIVIDE:
                self.advance(DIVIDE)
                result = result / self.operand()
        return result


    def eval(self):
        
        evaluation = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.advance(PLUS) #Moves past the plus
                evaluation += self.term() #Returns the value of the next operand AND advances
            elif token.type == MINUS:
                self.advance(MINUS)
                evaluation -= self.term()
        return evaluation
    
def main():
    while True:
        try:
            expression = input('calc> ')

        except EOFError:
            break
        if not expression:
            continue
        lexer = Lexer(expression)
        interpreter = Interpreter(lexer)
        result = interpreter.eval()
        print(result)

if __name__ == '__main__':
    main()

    