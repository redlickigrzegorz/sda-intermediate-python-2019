from datetime import datetime
from datetime import timedelta

from src.cinema.projection import Projection
from src.cinema.projection import projection_01
from src.cinema.hall import Hall
from src.cinema.hall import hall_01
from src.cinema.movie import Movie
from src.cinema.movie import movie_01


def add_new_projection(hall: Hall, movie: Movie, projection_start: datetime) -> None:
    if (isinstance(hall, Hall)) and (isinstance(movie, Movie)):
        projection_end = projection_start + timedelta(minutes=movie.movie_lenght_in_minutes)
        count = 0
        for key, value in hall.callendar.items():
            # if not (projection_start > hall.callendar[i - 1][0] or projection_start >= hall.callendar[i - 1][1]) and (
            #         projection_end <= hall.callendar[i - 1][0] or projection_end >= hall.callendar[i - 1][1]):
            start, end = value
            if (projection_start < start or projection_start >= end) and (
                projection_end < start or projection_end >= end
            ):
                count += 1
        if count == len(hall.callendar.keys()):
            hall.callendar[f'{hall.hall_name} {movie.title} {projection_start}'] = (projection_start, projection_end)
            return Projection(hall, movie, projection_start)
        else:
            print('this projection cannot be added')
    else:
        print('Sorry, hall, movie or projection time cannot be implemented.'
              'Please check your data')

def delete_projection(projection):
    if isinstance(projection, Projection):
        del projection
    else:
        print('Sorry, there is no such projection in our cinema system')
        return 'Sorry, there is no such projection in our cinema system'

def buy_ticket(projection: Projection, row_number: int, seat_number: int):
    if (isinstance(projection, Projection)) and(row_number <= projection.hall.number_of_rows and row_number > 0) and (
        seat_number <= projection.hall.number_of_seats_in_a_raw and seat_number > 0) and (
        [row_number, seat_number] not in projection.booked_seats
    ):
            projection.booked_seats.append([row_number, seat_number])
            projection.booked_seats.sort()
    else:
        print('Either row number, seat number is not possible for the hall or the seat is'
              'already booked. Please try with a another input')
        return 'Either row number, seat number is not possible for the hall or the seat is already booked. ' \
               'Please try with a another input'

def return_ticket(projection: Projection, row_number: int, seat_number: int):
    if (isinstance(projection, Projection)) and ([row_number, seat_number] in projection.booked_seats):
        projection.booked_seats.remove([row_number, seat_number])
    else:
        print('Either projection does not exist or the seat was not booked')
        return 'Either projection does not exist or the seat was not booked'

if __name__ == '__main__':
    print('first try')
    projection_04 = Projection(hall_01, movie_01, datetime(2020, 9, 2, 11, 5))
    print('projection_04' in locals())
    del projection_04
    print('projection_04' in locals())

    print('###############')
    print('second try')
    projection_04 = Projection(hall_01, movie_01, datetime(2020, 9, 2, 11, 5))
    print('projection_04' in locals())
    delete_projection(projection_04)
    print('projection_04' in locals())









