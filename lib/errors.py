class BlogError(Exception):

    reason: str

    def __init__(self, reason: str = ''):
        self.reason = reason


class CompileError(BlogError):

    def __init__(self, reason: str = ''):
        super(CompileError, self).__init__(reason)


class ParseError(BlogError):

    def __init__(self, reason: str = ''):
        super(ParseError, self).__init__(reason)
