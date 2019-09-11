import unittest
from datetime import datetime

from src.cinema.movie import movie_01
from src.cinema.movie import movie_02
from src.cinema.hall import hall_01
from src.cinema import  add_new_projection
from src.cinema import  delete_projection
from src.cinema import  buy_ticket
from src.cinema import  return_ticket
from src.cinema.projection import Projection
from src.cinema.projection import projection_01
from src.cinema.projection import projection_02


class TestHall(unittest.TestCase):
    def test_add_new_projection(self):
        # Check 01 - does the hall callendar is updated corretly when data are correct:
        # Given (already available by importing)

        # When
        projection_test_01 = add_new_projection(hall_01, movie_01, datetime(2019, 9, 1, 11, 0))

        #Then
        self.assertEqual(hall_01.callendar['Hall_01 A Rainy Day in New York 2019-09-01 11:00:00'],
                         (datetime(2019, 9, 1, 11, 0), datetime(2019, 9, 1, 12, 32)))

        # Check 02 - does the function correctly do not add a projection when the projection time clash with other ones:
        # Given (already available by importing)

        # When
        add_new_projection(hall_01, movie_02, datetime(2019, 9, 1, 10, 0))
        self.assertEqual(False, 'Toy Story 4 2019-09-01 10:00:00' in hall_01.callendar)

    def test_delete_projection(self):
        # Check 01 - is the projection deleted from the system
        # Given
        projection_00 = Projection(hall_01, movie_02, datetime(2019, 12, 24, 18, 00))

        # When
        # delete_projection(projection_00)
        del projection_00

        # Then
        print('projection_00' in locals())

        # self.assertEqual(True, 'projection_03' in globals()))


    def test_buy_ticket(self):
        # Check 01 - does the fuction correclty add booked seats to a projection booked_seats list:
        # Given (already available by importing)

        # When
        buy_ticket(projection_01, 2, 2)

        # Then
        self.assertEqual(True, [2, 2] in projection_01.booked_seats)

        # Check 02 - will be the seat booked if the seat was booked erlier?:
        # Given (already available by importing and the check 01

        # When
        test_result = buy_ticket(projection_01, 2, 2)

        # Then
        self.assertEqual('Either row number, seat number is not possible for the hall or the seat is already booked. ' \
               'Please try with a another input', test_result)

        # Check 03 - is it possible to book a seat which does not exist and is the message correct?:
        # Given (already available by importing)

        # When
        test_result_02 = buy_ticket(projection_01, 100, 2)

        # Then
        self.assertNotIn([100, 2], projection_01.booked_seats)
        self.assertEqual('Either row number, seat number is not possible for the hall or the seat is already booked. ' \
                         'Please try with a another input', test_result_02)

    def test_return_ticket(self):
        # Check 01 - is the booked ticket unbooked after using function:
        # Given
        buy_ticket(projection_02, 7, 7)
        buy_ticket(projection_02, 8, 8)

        # When
        return_ticket(projection_02, 8, 8)

        # Then
        self.assertEqual([[7, 7]], projection_02.booked_seats)

        # Check 02 - is it possible to return a ticket that has not been bought:
        # Given (already available from import and Check 01:

        # When
        test_result = return_ticket(projection_02, 8, 8)

        # Then
        print(projection_02.booked_seats)
        print(test_result)
        self.assertEqual('Either projection does not exist or the seat was not booked', test_result)



