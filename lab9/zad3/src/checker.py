from lab9.zad3.src.environment import Class

class Checker:
    def __init__(self, obj: Class):
        self.env = Class()
        self.fileWasPlayed = False


    def remainder(self, file):
        self.fileWasPlayed = False
        hour = self.env.getTime().hour
        if hour >= 17:
            self.env.playWavFile(file)
            self.fileWasPlayed = True

