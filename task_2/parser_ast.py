from .lexer import Lexer
from .token_type import TokenType
from .ast_nodes import Num, BinOp


class ParsingError(Exception):
    pass


class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise ParsingError("Parsing error!")  # Ошибка синтаксического анализа

    def consume(self, token_type):
        # compare current token with expected one, if they coinside "consume" it and move to the next one
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def term(self):
        # Parser for 'term' gramatic rules - integers in our case
        token = self.current_token

        node = self.factor()

        while self.current_token.type in (TokenType.MUL, TokenType.DIV):
            token = self.current_token
            if token.type == TokenType.MUL:
                self.consume(TokenType.MUL)
            elif token.type == TokenType.DIV:
                self.consume(TokenType.DIV)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def factor(self):
        # Parser for 'factor' gramatic rules
        token = self.current_token

        if token.type == TokenType.INTEGER:
            self.consume(TokenType.INTEGER)
            return Num(token)
        elif token.type == TokenType.LPAREN:
            self.consume(TokenType.LPAREN)
            node = self.expr()
            self.consume(TokenType.RPAREN)
            return node

    def expr(self):
        # Parser for arithmetical expressions
        node = self.term()

        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.consume(TokenType.PLUS)
            elif token.type == TokenType.MINUS:
                self.consume(TokenType.MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def print_ast(self, node, level=0):
        indent = "   " * level
        if isinstance(node, Num):
            print(f"{indent}Num({node.value})")
        elif isinstance(node, BinOp):
            print(f"{indent}BinOp:")
            print(f"{indent}  left: ")

            self.print_ast(node.left, level + 2)
            print(f"{indent}  op: {node.op.type} ")
            print(f"{indent}  right: ")
            self.print_ast(node.right, level + 2)
        else:
            print(f"{indent}Uknown node type: {type(node)}")
