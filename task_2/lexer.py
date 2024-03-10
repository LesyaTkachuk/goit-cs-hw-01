from .token_type import Token, TokenType


class LexicalError(Exception):
    pass


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def advance(self):
        # move pointer to the next char in the initial string
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # the end of the initial string
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        # skip whitespaces in the initial string
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        # return integer gathered from consequent digits
        result = ""
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        # lexical analyser that splits initial string into tokens
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(TokenType.INTEGER, self.integer())

            if self.current_char == "+":
                self.advance()
                return Token(TokenType.PLUS, "+")

            if self.current_char == "-":
                self.advance()
                return Token(TokenType.MINUS, "-")

            if self.current_char == "*":
                self.advance()
                return Token(TokenType.MUL, "*")

            if self.current_char == "/":
                self.advance()
                return Token(TokenType.DIV, "/")

            if self.current_char == "(":
                self.advance()
                return Token(TokenType.LPAREN, "(")

            if self.current_char == ")":
                self.advance()
                return Token(TokenType.RPAREN, ")")

            raise LexicalError("Lexical analysis error!")

        return Token(TokenType.EOF, None)
