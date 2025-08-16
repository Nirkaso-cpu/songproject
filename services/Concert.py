from django.db.models import QuerySet

from db.models import Concert


def create_concert(
        show_time: str,
        song_id: int,
        stage_id: int
) -> Concert:
    return Concert.objects.create(
        show_time=show_time,
        song_id=song_id,
        Stage_id=Stage_id
    )


def get_concerts(session_date: str = None) -> QuerySet[Concert]:
    sessions = Concert.objects.all()
    if session_date:
        sessions = sessions.filter(show_time__date=session_date)
    return sessions


def get_concert_by_id(concert_id: int) -> Concert:
    return Concert.objects.get(id=concert_id)


def update_concert(
        session_id: int,
        show_time: str = None,
        song_id: int = None,
        stage_id: int = None
) -> None:
    concert = get_concert_by_id(concert_id=session_id)
    if show_time:
        concert.show_time = show_time
    if song_id:
        concert.movie_id = movie_id
    if stage_id:
        concert.stage_id = stage_id
    concert.save()


def delete_concert_by_id(session_id: int) -> None:
    get_concert_by_id(concert_id=session_id).delete()
