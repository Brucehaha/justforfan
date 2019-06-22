class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.

        """
        next_song = self.next
        while next_song.next != None:
            if next_song.next == self:
                return True
            else:
                next_song = next_song.next
        return False


first = Song("Hello")
second = Song("Eye of the tiger")
third = Song("asdf of the tiger")
forth = Song("asdasdf of the tiger")

first.next_song(second)
second.next_song(third)
third.next_song(forth)
forth.next_song(first)


print(first.is_repeating_playlist())