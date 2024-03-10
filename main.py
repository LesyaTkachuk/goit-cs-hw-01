from task_2.lexer import Lexer
from task_2.parser_ast import Parser
from task_2.interpreter import Interpreter


def main():
    while True:
        try:
            # ask user to enter math expression
            text = input("Enter mathematical expression or exit: ")

            # if exit breal the cycle and stop programm execution
            if text.lower() == "exit":
                print("Exit the programm")
                break

            # Lexer initialisation - spliting of text onto lexical units -tokens
            lexer = Lexer(text)

            # Parser initialisation - defining programming language instructions from tokens
            parser = Parser(lexer)

            # Interpreter initialisation - processing and interpretation of the AST-tree
            # in real compilators it is the process of machine code formation
            interpreter = Interpreter(parser)
            result = interpreter.interpret()

            # printing the final result of code execution
            print("Result: ", result)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
