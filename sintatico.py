class SyntaxAnalyzer:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.index = -1
        self.advance()

    def advance(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]
        else:
            self.current_token = None

    def consume(self, token_type):
        if self.current_token and self.current_token['type'] == token_type:
            self.advance()
        else:
            raise SyntaxError(f"Expected {token_type} but found {self.current_token['type']}")

    def factor(self):
        if self.current_token['type'] == 'INTEGER':
            self.consume('INTEGER')
        elif self.current_token['type'] == 'LPAREN':
            self.consume('LPAREN')
            self.expr()
            self.consume('RPAREN')
        else:
            raise SyntaxError("Invalid syntax in factor")

    def term(self):
        self.factor()
        while self.current_token and self.current_token['type'] in ('MULT', 'DIV'):
            if self.current_token['type'] == 'MULT':
                self.consume('MULT')
            elif self.current_token['type'] == 'DIV':
                self.consume('DIV')
            self.factor()

    def expr(self):
        self.term()
        while self.current_token and self.current_token['type'] in ('PLUS', 'MINUS'):
            if self.current_token['type'] == 'PLUS':
                self.consume('PLUS')
            elif self.current_token['type'] == 'MINUS':
                self.consume('MINUS')
            self.term()

    def parse(self):
        self.expr()
        if self.current_token is not None:
            raise SyntaxError("Unexpected token at the end of expression")

# Exemplo de uso:
if __name__ == "__main__":
    # Suponha que os tokens já tenham sido identificados e classificados
    tokens = [
        {'type': 'INTEGER', 'value': 3},
        {'type': 'PLUS'},
        {'type': 'INTEGER', 'value': 5},
        {'type': 'MULT'},
        {'type': 'LPAREN'},
        {'type': 'INTEGER', 'value': 2},
        {'type': 'PLUS'},
        {'type': 'INTEGER', 'value': 4},
        {'type': 'RPAREN'}
    ]

    try:
        analyzer = SyntaxAnalyzer(tokens)
        analyzer.parse()
        print("A expressão é válida!")
    except SyntaxError as e:
        print(f"A expressão é inválida: {str(e)}")
 