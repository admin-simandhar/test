
class EmptyStringException(Exception):
    def __init__(self,message):
        self.message = {"value required":message}
        pass