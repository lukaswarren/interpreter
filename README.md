# Interpreter
Ongoing project.  Currently building a interpreter. Current functionality is a calculator.  

# Running 
To run this have Python installed.  In terminal navigate to project directory and run 'python calculator.py'

# Resources
Built by following along with https://ruslanspivak.com/lsbasi-part1/

# Background
This interpreter uses grammars to evaluate expression, some recursive:
    operand :  INTEGER | LPAREN eval RPAREN
    term : operand \(\(MULTIPLY | DIVIDE\) operand\)
    eval : term \(\(PLUS | MINUS\) term\)