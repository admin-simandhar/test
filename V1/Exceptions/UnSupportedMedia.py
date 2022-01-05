class UnSupportedMedia(Exception):
    def __init__(self,message):
        self.message = "unsupported file: "+message
    pass