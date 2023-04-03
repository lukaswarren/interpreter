from type import TokenType

globals().update(TokenType.__members__)

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
        
    def visit_UnaryOp(self, node):
        if node.op.type == PLUS:
            return self.visit(node.child) 
        elif node.op.type == MINUS:
            return -1 * self.visit(node.child) 

        
    def visit_Num(self, node):
        return node.value
    
    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)
        
