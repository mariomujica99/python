class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        '''
        Method to set default instance variables.
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        '''
        Method to turn the tv on and off.
        :return: power status.
        '''
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        '''
        Method to mute and unmute the tv.
        :return: mute status.
        '''
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            else:
                self.__previous_volume = self.__volume
                self.__muted = True
                self.__volume = Television.MIN_VOLUME
            return self.__muted

    def channel_up(self) -> None:
        '''
        Method to increase the tv channel value.
        :return: channel value.
        '''
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        '''
        Method to decrease the tv channel value.
        :return: channel value.
        '''
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        '''
        Method to increase the tv volume.
        :return: volume value.
        '''
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Method to decrease the tv volume.
        :return: volume value.
        '''
        if self.__status:
            if self.__muted:
                self.mute()
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        '''
        Method to show the tv status.
        :return: tv status.
        '''
        return (f'Power = {self.__status}, '
                f'Channel = {self.__channel}, '
                f'Volume = {self.__volume}')