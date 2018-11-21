import media
import fresh_tomatoes


def generate_movies_list():
    movie1 = media.Movie("Mr. Bean's Holiday",
                         "http://www.gstatic.com/tv/thumb/"
                         + "v22vodart/163151/p163151_v_v8_ac.jpg",
                         "https://www.youtube.com/watch?v=VgcVv93GjeQ",
                         "Steve Bendelack",
                         "March 24, 2007")
    movie2 = media.Movie("Rush Hour",
                         "http://www.gstatic.com/tv/thumb/"
                         + "v22vodart/21702/p21702_v_v8_ab.jpg",
                         "https://www.youtube.com/watch?v=UuHf24GhINc",
                         "Brett Ratner",
                         "September 18, 1998")
    movie3 = media.Movie("Avengers: Infinity War",
                         "http://www.gstatic.com/tv/thumb/v22vodart"
                         + "/12863030/p12863030_v_v8_ae.jpg",
                         "https://www.youtube.com/watch?v=6ZfuNTqbHE8",
                         "Anthony Russo, Joe Russo",
                         "April 23, 2018")
    movie4 = media.Movie("Black Panther",
                         "http://www.gstatic.com/tv/thumb/v22vodart/"
                         + "12878741/p12878741_v_v8_ac.jpg",
                         "https://www.youtube.com/watch?v=dxWvtMOGAhw",
                         "Ryan Coogler",
                         "January 29, 2018 ")
    movie5 = media.Movie("Deadpool 2",
                         "http://www.gstatic.com/tv/thumb/v22vodart/"
                         + "12854824/p12854824_v_v8_bb.jpg",
                         "https://www.youtube.com/watch?v=D86RtevtfrA",
                         "David Leitch",
                         "May 15, 2018 ")
    movie6 = media.Movie("Incredibles 2",
                         "http://www.gstatic.com/tv/thumb/v22vodart/"
                         + "13446354/p13446354_v_v8_ag.jpg",
                         "https://www.youtube.com/watch?v=i5qOzqD9Rms",
                         "Brad Bird",
                         "June 5, 2018")

    movies = [movie1, movie2, movie3, movie4, movie5, movie6]
    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    generate_movies_list()
