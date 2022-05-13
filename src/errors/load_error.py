class LoadError(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.mesage = message
        self.error_type = 'LoadError'