#import type
INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, LPAREN, RPAREN, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'LPAREN', 'RPAREN','EOF'

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
        elif character == '(':
            self.position += 1
            return Token(LPAREN, "(")
        elif character == ')':
            self.position += 1
            return Token(RPAREN, ")")
        elif character.isdigit():
            result =  self.get_integer(text, character)
            return Token(INTEGER, int(result))
        
        self.error()   

class SyntaxTree(object):
    pass

class BinaryOp(SyntaxTree):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class Num(SyntaxTree):
    def __init__(self, token):
        self.token = token
        self.value = token.value

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

class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_BinaryOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == MULTIPLY:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == DIVIDE:
            return self.visit(node.left) / self.visit(node.right)
        
    def visit_Num(self, node):
        return node.value
    
    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)
        


def main():
    while True:
        try:
            expression = input('calc> ')

        except EOFError:
            break
        if not expression:
            continue
        lexer = Lexer(expression)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        print(result)

if __name__ == '__main__':
    main()

    