class Television():
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL


    def power(self):
        """
        Method to toggle the tv power status.
        """
        self._status = not self._status


    def mute(self):
        """
        Method to toggle mute if tv is on
        """
        if self._status:
            self._muted = not self._muted


    def channel_up(self):
        """
        Method to decrease the tv channel.
        """
        if self._status:
            if self._channel < Television.MAX_CHANNEL:
                self._channel += 1
            else:
                self._channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Method to decrease the tv channel.
        """
        if self._status:
            if self._channel > Television.MIN_CHANNEL:
                self._channel -= 1
            else:
                self._channel = Television.MAX_CHANNEL

    def volume_up(self):
        """
        Method to increase the volume of the channel.
        """
        if self._status:
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1
            else:
                self._volume = Television.MAX_VOLUME
            self._muted = False
    def volume_down(self):
        """
        Method to decrease the volume of the channel.
        """
        if self._status:
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1
            else:
                self._volume = Television.MIN_VOLUME
            self._muted = False
    def __str__(self):
        """
        method to show the tv status.
        :return: tv status.
        """
        if self._status:
            self.display_volume = Television.MIN_VOLUME if self._muted else self._volume
        else:
            self.display_volume = self._volume
        return f'Power = {self._status}, Channel = {self._channel}, Volume = {self.display_volume}'




