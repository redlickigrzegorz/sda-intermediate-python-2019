import typing


class Hall:
    def __init__(self,hall_name: str, number_of_rows: int, number_of_seats_in_a_raw: int) -> typing.List:
        self.hall_name = hall_name
        self.number_of_rows = number_of_rows
        self.number_of_seats_in_a_raw = number_of_seats_in_a_raw
        self.callendar = {}

hall_01 = Hall('Hall_01', 10, 15)
hall_02 = Hall('Hall_02', 8, 10)
hall_03 = Hall('Hall_03', 12, 10)
