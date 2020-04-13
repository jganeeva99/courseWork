from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # Keywords
        self.lexer.add('SCANF', r'scanf')
        self.lexer.add('INT', r'int')
        self.lexer.add('BOOL', r'bool')
        self.lexer.add('RETURN', r'return')
        self.lexer.add('MAIN', r'main')
        self.lexer.add('VOID', r'void')
        self.lexer.add('IF', r'if')
        self.lexer.add('NULL', r'NULL')
        self.lexer.add('NULLPTR', r'nullptr')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
        self.lexer.add('OPEN_BRACE', r'{')
        self.lexer.add('CLOSE_BRACE', r'}')
        self.lexer.add('ASSIGN', r'=')
        self.lexer.add('OPERATOT_!+', r'!=')
        self.lexer.add('OPERATOR_<<', r'<<')
        self.lexer.add('OPERATOR_->', r'->')
        # Point
        self.lexer.add("POINT", r'\.')

        self.lexer.add("PLUS", r'\+')
        self.lexer.add('COMMA', r'\,')
        self.lexer.add('SEMI_COLON', r'\;')

        # Classes and functions names and variables
        self.lexer.add('CONNECTION_CLASS', r'QSqlQuery')
        self.lexer.add('DB', r'QSqlDatabase')
        self.lexer.add('EXEC_FUNC', r'exec')
        self.lexer.add('CREATE_FUNC', r'QsqlDatabase::addDatabase')
        self.lexer.add('HOST_NAME_FUNC', r'setHostName')
        self.lexer.add('DB_NAME_FUNC', r'setDatabaseName')
        self.lexer.add('USER_NAME_FUNC', r'setUserName')
        self.lexer.add('PASSWORD_FUNC', r'setPassword')
        self.lexer.add('OPEN_FUNC', r'open')
        self.lexer.add('PTR_TYPE', r'[a-zA-z]+\s{0,}\*')
        self.lexer.add('CLASS', r'class')
        self.lexer.add('PUBLIC', r'public\:')
        self.lexer.add('COUT', r'cout')
        self.lexer.add('SIZEOF', r'sizeof')
        self.lexer.add('GET_MEMORY', r'new|malloc')
        self.lexer.add('CLEAR_MEMORY', r'delete|free')
        self.lexer.add('VAR', r'[a-zA-z]+[0-9]{0,}')

        self.lexer.add('STRING', r'\"[\w\%\s\'\,=;!]+\"')
        self.lexer.add('DIGIT', r'[0-9]')
        # Ignore spaces
        self.lexer.ignore(r'\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()


