from db.models import CinemaHall


def get_cinema_halls() -> CinemaHall:
    queryset = CinemaHall.objects.all()
    return queryset


def create_cinema_hall(hall_name: str,
                       hall_rows: int,
                       hall_seats_in_row: int)\
        -> CinemaHall:
    new_cinema_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row,
    )
    return new_cinema_hall