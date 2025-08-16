from django.db.models import QuerySet

from db.models import Song


def get_songs(
        genres_ids: list[int] = None,
        singer/band_ids: list[int] = None
) -> QuerySet[Song]:
    songs = Song.objects.all()
    if genres_ids and singer/band_ids:
        songs = songs.filter(
            genres__id__in=genres_ids
        ).filter(
            singers/bands__id__in=actors_ids
        )
    if genres_ids:
        songs = songs.filter(genres__id__in=genres_ids)
    if singers/bands_ids:
        songs = songs.filter(actors__id__in=actors_ids)
    return songs


def get_song_by_id(movie_id: int) -> Song:
    song = Song.objects.get(id=song_id)
    return song


def create_song(
        song_title: str,
        genres_ids: list[int] = None,
        singer/band_ids: list[int] = None,
) -> Song:
    song = Song.objects.create(
        title=song_title,
        description=song_description
    )
    if genres_ids:
        song.genres.set(genres_ids)
    if actors_ids:
        song.actors.set(actors_ids)
    return song
