class SyntaxTree(object):
    pass

class BinaryOp(SyntaxTree):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class UnaryOp(SyntaxTree):
    def __init__(self, op, child):
        self.token = self.op = op
        self.child = child

class Num(SyntaxTree):
    def __init__(self, token):
        self.token = token
        self.value = token.value