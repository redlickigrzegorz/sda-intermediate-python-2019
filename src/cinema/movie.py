class Movie:
    def __init__(self, title: str, projection_type: str, language: str, movie_lenght_in_minutes: int):
        self.title = title
        self.projection_type = projection_type
        self.language = language
        self.movie_lenght_in_minutes = movie_lenght_in_minutes

movie_01 = Movie('A Rainy Day in New York', '2D', 'ENG', 92)
movie_02 = Movie('Toy Story 4', '2D', 'PL', 100)
movie_03 = Movie('Maiden', '2D', 'ENG', 97)

