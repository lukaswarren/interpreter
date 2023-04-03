# Interpreter
Ongoing project.  Currently building a interpreter. Current functionality is a calculator.  

# Running 
To run this have Python installed.  In terminal navigate to project directory and run 'python calculator.py'

# Resources
Built by following along with https://ruslanspivak.com/lsbasi-part1/

# Background
This Parser uses grammars to parse the expression correctly, some recursive:
    
<ul>
<li> operand : (PLUS|MINUS) operand | INTEGER | LPAREN eval RPAREN </li> 
<li> term : operand ((MULTIPLY | DIVIDE) operand) </li> 
<li> eval : term ((PLUS | MINUS) term) </li> 
</ul>

Result of the parser is an syntax tree. Currently a version of type of binary tree. The tree ensures that order of operations is enforced.  Evaluation/interpretation is then calculated by visiting the nodes of the tree. 