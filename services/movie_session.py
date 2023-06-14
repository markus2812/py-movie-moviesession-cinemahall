from datetime import datetime

from db.models import MovieSession, Movie


def create_movie_session(movie_show_time, movie_id: int, cinema_hall_id: int):
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=cinema_hall_id,
        movie=movie_id,
    )
    return new_movie_session


def get_movies_sessions(session_date: str = None):
    queryset = MovieSession.objects.all()
    if session_date:
        queryset = queryset.filter(show_time__date=session_date)
    return queryset


def get_movie_session_by_id(movie_session_id: int):
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int,
                         show_time: str = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None):
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        movie = MovieSession.objects.get(movie=movie_id)
        movie_session.movie = movie

    if cinema_hall_id:
        cinema_hall = MovieSession.objects.get(cinema_hall=cinema_hall_id)
        movie_session.cinema_hall = cinema_hall

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()

