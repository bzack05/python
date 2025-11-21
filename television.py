

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__chanel = self.MIN_CHANNEL

    def power(self):
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        if self.__status:
            if self.__muted: #Look at this later
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self):
        if self.__status:
            self.__chanel += 1
            if self.__chanel > self.MAX_CHANNEL:
                self.__chanel = self.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            self.__chanel -= 1
            if self.__chanel < self.MIN_CHANNEL:
                self.__chanel = self.MAX_CHANNEL

    def volume_up(self):
        if self.__status:
            self.__muted = False
            if self.__volume == self.MAX_VOLUME:
                return
            else:
                self.__volume += 1

    def volume_down(self):
        if self.__status:
            self.__muted = False
            if self.__volume == self.MIN_VOLUME:
                return
            else:
                self.__volume -= 1

    def __str__(self):
        if self.__muted:
            return f"Power - {self.__status}, Channel - {self.__chanel}, Volume - {0}."
        else:
            return f"Power - {self.__status}, Channel - {self.__chanel}, Volume - {self.__volume}."

def main():
    pass

if __name__ == "__main__":
    main()