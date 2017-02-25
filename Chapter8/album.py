def make_album(artist_name, album_title, number_tracks=''):
    """Returns a Music Album dictionary"""
    album = {'artist': artist_name, 'album': album_title}
    return album

music_album1 = make_album('snoop dogg', 'dog')
music_album2 = make_album('parokya', 'harana', '10')
music_album3 = make_album('franco', 'soul')
print(music_album1, music_album2, music_album3)
