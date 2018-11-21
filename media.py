import webbrowser


class Movie():
    """Movie class that can identify movies by
    * title
    * poster
    * trailer
    * directors
    * release date"""

    def __init__(self, title, poster_image_url,
                 trailer_youtube_url, director, release):
        """Movie constructor"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.director = director
        self.release = release

    def show_trailer(self):
        """Method to show movies trailers"""
        webbrowser.open(self.trailer_youtube_url)
