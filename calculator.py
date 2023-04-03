from lexer import Lexer
from parsers import Parser
from interpreters import Interpreter

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

    