from nested_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please enter album number:")

    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}. {} by {}, {}".format(index + 1, title, artist, year))

    user_album = int(input())

    if user_album < 1 or user_album > len(albums[3]):
        break

    print("Choose song you want to play:")
    songs_list = albums[user_album - 1][SONGS_LIST_INDEX]

    for (number, song) in songs_list:
        print("{}. {}".format(number, song))

    user_song = int(input())

    if user_song < 1 or user_song > len(songs_list):
        print("=" * 30)
        continue
    else:
        print("Playing - {}".format(songs_list[user_song - 1][SONG_TITLE_INDEX]))

    print("=" * 30)
