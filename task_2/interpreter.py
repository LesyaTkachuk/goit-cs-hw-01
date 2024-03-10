from .token_type import TokenType
from .parser_ast import Parser
from .ast_nodes import Num, BinOp


class Interpreter:
    def __init__(self, parser: Parser):
        self.parser = parser

    # to process BinOp node
    def visit_BinOp(self, node: BinOp):
        if node.op.type == TokenType.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.op.type == TokenType.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.op.type == TokenType.MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif node.op.type == TokenType.DIV:
            return self.visit(node.left) / self.visit(node.right)
        else:
            return "Unsupported operation"

    # to process Num node
    def visit_Num(self, node: Num):
        return node.value

    # to start AST tree interpretation (processing)starting from the root node
    def interpret(self):
        tree = self.parser.expr()
        self.parser.print_ast(tree)
        return self.visit(tree)

    # call correspondent to each node visit method dynamically
    def visit(self, node):
        method_name = "visit_" + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    # generate an exception for unexisting node type
    def generic_visit(self, node):
        raise Exception(f"Method visit_{type(node).__name__} doesn't exist")
