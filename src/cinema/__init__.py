from datetime import datetime
from datetime import timedelta

from src.cinema.projection import Projection
from src.cinema.hall import Hall
from src.cinema.hall import hall_01
from src.cinema.movie import Movie
from src.cinema.movie import movie_01


def add_new_projection(hall: Hall, movie: Movie, projection_start: datetime) -> None:
    if (isinstance(hall, Hall)) and (isinstance(movie, Movie)):
        projection_end = projection_start + timedelta(minutes=movie.movie_lenght_in_minutes)
        count = 0
        for i in hall.callendar:
            if not (projection_start > hall.callendar[i - 1][0] or projection_start >= hall.callendar[i - 1][1]) and (
                    projection_end <= hall.callendar[i - 1][0] or projection_end >= hall.callendar[i - 1][1]):
                count += 1
        if count > 0:
            Projection(hall, movie, projection_start)
            hall.callendar[f'{hall.hall_name} {movie.title} {projection_start}'] = (projection_start, projection_end)
    else:
        print('Sorry, hall, movie or projection time cannot be implemented.'
              'Please check your data')


if __name__ == '__main__':
    print(hall_01.callendar)
    add_new_projection(hall_01, movie_01, datetime(2019, 9, 1, 11, 00))
    print(hall_01.callendar)
    for i in range(0, len(hall_01.callendar)-1):
        if not (datetime(2019, 1, 1) > hall_01.callendar[i - 1][0] or datetime(2019, 1, 1) >= hall_01.callendar[i - 1][1]) and (
                        datetime(2019, 1, 1) <= hall_01.callendar[i - 1][0] or datetime(2019, 1, 1) >= hall_01.callendar[i - 1][1]):
            print('ok')

