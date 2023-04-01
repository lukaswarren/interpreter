# Interpreter
Ongoing project.  Currently building a interpreter. Current functionality is a calculator.  

# Running 
To run this have Python installed.  In terminal navigate to project directory and run 'python calculator.py'

# Resources
Built by following along with https://ruslanspivak.com/lsbasi-part1/

# Background
This interpreter uses grammars to evaluate expression, some recursive:
    
<ul>
<li> operand :  INTEGER | LPAREN eval RPAREN </li> 
<li> term : operand ((MULTIPLY | DIVIDE) operand) </li> 
<li> eval : term ((PLUS | MINUS) term) </li> 
</ul>