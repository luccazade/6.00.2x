def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """
    # Initialise chosen list and current size
    list_chosen = []
    current_size = 0

    # Helper function to check remaining space
    def remaining_space(current_list):
        """
        :arg current_list: list of songs in tuple form

        :param max_size: maximum allowed size

        :returns: amount of remaining space
        """
        current = 0
        for i in current_list:
            current += i[2]
        remaining = max_size - current
        return remaining

    # Helper function to check if song fits

    def song_fit(song):
        """
        :arg song: a song to be tested (tuple)

        :param max_size: maximum song from parent function
        :return: Bool of whether song fits
        """
        if song in list_chosen:
            return False
        remaining = remaining_space(list_chosen)
        if song[2] <= remaining:
            return True
        else:
            return False

    # Helper function to extract names of songs

    def extract_names(list):
        """
        :param list of tuples, ('song_name', song_len, song_size)
        :return: list of names of the songs in list
        """
        names_chosen = []
        for i in list:
            names_chosen.append(i[0])
        return names_chosen

    # Helper function to find smallest song

    def smallest_song(list):
        """
        :arg list: list of songs in tuples

        :returns: song tuple of smallest size
        """
        minimum = min(list, key=lambda t: t[2])
        if minimum in list_chosen:
            list.remove(minimum)
            smallest_song(list)
        return minimum

    # Check first song fits and end program if not

    if song_fit(songs[0]) is False:
        return []

    # Duplicate list
    songs_copy = songs[:]

    # Add first song to list and remove
    list_chosen.append(songs[0])
    songs_copy.remove(songs[0])

    # Loop over all songs
    for i in range(len(songs)):
        try:
            song_to_check = smallest_song(songs_copy)
        except ValueError:
            break
        else:
            if song_fit(song_to_check) is True:
                list_chosen.append(song_to_check)
                songs_copy.remove(song_to_check)
            else:
                break

    songs_chosen = extract_names(list_chosen)

    return songs_chosen


# TESTS

songs2 = [('Roar', 4.4, 4.0), ('Sail', 3.5, 7.7), ('Timber', 5.1, 6.9), ('Wannabe', 2.7, 1.2)]
max_size = 12.2

print(song_playlist(songs2, max_size))

songs3 = [('Roar', 4.4, 4.0), ('Sail', 3.5, 7.7), ('Timber', 5.1, 6.9), ('Wannabe', 2.7, 1.2)]
max_size = 11

print(song_playlist(songs3, max_size))

print(song_playlist([('a', 4.4, 4.0), ('b', 3.5, 7.7), ('c', 5.1, 6.9), ('d', 2.7, 1.2)], 20))

print(song_playlist([('a', 4.0, 4.4), ('b', 7.7, 3.5), ('c', 6.9, 5.1), ('d', 1.2, 2.7)], 20))

print(song_playlist([('a', 1.4, 4.0)], 20))
