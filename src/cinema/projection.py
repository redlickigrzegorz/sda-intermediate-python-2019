import typing

from datetime import datetime
from datetime import timedelta

from src.cinema.hall import Hall
from src.cinema.hall import hall_01
from src.cinema.hall import hall_02
from src.cinema.hall import hall_03
from src.cinema.movie import Movie
from src.cinema.movie import movie_01
from src.cinema.movie import movie_02
from src.cinema.movie import movie_03

class Projection:
    def __init__(self, hall: Hall, movie: Movie, projection_start: datetime) -> None:
        self.hall = hall
        self.movie = movie
        self.projection_start = projection_start
        self.projection_end = projection_start + timedelta(minutes=movie.movie_lenght_in_minutes)
        self.booked_seats = []

projection_01 = Projection(hall_01, movie_01, datetime(2019, 9, 2, 11, 00))
projection_02 = Projection(hall_02, movie_02, datetime(2019, 9, 2, 11, 00))

if __name__ == '__main__':
    print(projection_01)



