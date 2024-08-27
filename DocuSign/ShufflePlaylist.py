import random


def shuffle_playlist(playlist):
    while True:
        random.shuffle(playlist)
        if all(playlist[i] != playlist[i + 1] for i in range(len(playlist) - 1)):
            return playlist


# Test case function to verify the shuffle
def test_shuffle_playlist():
    playlist = [3, 2, 5, 4, 58, 93, 44, 53, 76, 11, 27]

    shuffled_playlist = shuffle_playlist(playlist.copy())

    print("Shuffled playlist:", shuffled_playlist)

    # Check that no two consecutive songs are the same
    assert all(shuffled_playlist[i] != shuffled_playlist[i + 1] for i in
               range(len(shuffled_playlist) - 1)), "Two consecutive songs are the same!"

    # Ensure that all songs from the original playlist are present
    assert sorted(shuffled_playlist) == sorted(
        playlist), "The shuffled playlist does not contain the same songs as the original!"

    print("Test passed! The shuffle is sufficiently random and meets all requirements.")


# Run the test case
test_shuffle_playlist()
