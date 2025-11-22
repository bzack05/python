class Television:
    """
    This is a class named Television that simulates power, channel, volume and mute functions.
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int= 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Sets a Television object with default settings.
        -Power off
        -Not muted
        -Volume set to MIN_VOLUME
        -Channel set to MIN_Channel
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggle the TV's power status.
        If TV is on it turns it off, if off it turns it on
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Toggle the TV's mute setting.
        Works if TV is powered on.
        Does not change the stored volume value. 
        """
        if self.__status:
            if self.__muted: #Look at this later
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self) -> None:
        """
        Increase the channel by 1.
        If trying to go past MAX_CHANNEL, it wraps around to MIN_CHANNEL.
        Works if TV is powered on.
        """
        if self.__status:
            self.__channel += 1
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decrease the channel by 1.
        If trying to go past MIN_CHANNEL, it wraps around to MAX_CHANNEL.
        Works if TV is powered on.
        """
        if self.__status:
            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increase the volume by 1.
        Volume will not go past MAX_VOLUME.
        Unmutes the TV if it was muted.
        Works if the TV is powered on.
        """
        if self.__status:
            self.__muted = False
            if self.__volume == self.MAX_VOLUME:
                return
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the volume by 1.
        Volume will not go past MIN_VOLUME.
        Unmutes the TV if it was muted.
        Works if the TV is powered on.
        """
        if self.__status:
            self.__muted = False
            if self.__volume == self.MIN_VOLUME:
                return
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return a string representation of the TV status, including:
        - Power state
        - Channel
        - Volume (0 if muted)
        """
        if self.__muted:
            return f"Power - {self.__status}, Channel - {self.__channel}, Volume - {0}."
        else:
            return f"Power - {self.__status}, Channel - {self.__channel}, Volume - {self.__volume}."

def main() -> None:
    pass

if __name__ == "__main__":
    main()
