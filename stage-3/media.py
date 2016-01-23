class Movie():
    '''This class provides a way to store movie related information'''

    # Initialize instance of class Movie
    def __init__(self, movie_title, poster_image, trailer_youtube,
                 movie_review, movie_rating):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.review = movie_review
        self.rating_image_url = movie_rating
