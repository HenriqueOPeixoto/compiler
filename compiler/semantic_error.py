class SemanticError(Exception):
    def __init__(self, message, filename, linenum):            
        super().__init__(message)
        self.message = message
        self.filename = filename
        self.linenum = linenum
    def __str__(self) -> str:
        return 'Erro semântico em {} na linha {}: {}'.format(self.filename, self.linenum, self.message)