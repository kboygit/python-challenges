def make_album(artist_name, album_title, number_tracks=''):
    """Returns a Music Album dictionary"""
    album = {'artist': artist_name, 'album': album_title}
    full_album = ("\nArtist:" + artist_name + ", Title:" + album_title + ", Tracks:" + number_tracks)
    return full_album

while True:
    print("\nType 'q' to stop")

    artist = input("Input Artist Name: ")
    if artist == 'q':
        break

    title = input("Input Album Title: ")
    if title == 'q':
        break

    tracks = input("Input Number of Tracks: ")
    if tracks == 'q':
        break

    music_album = make_album(artist,title,str(tracks))
    print(music_album)
