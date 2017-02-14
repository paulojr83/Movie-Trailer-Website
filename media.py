import  webbrowser
#Create Movie object#
class Movie():
   """
   Create Movie object
   init the input arguments for Movie
   """
   def __init__(self
                , movie_title
                , movie_storyline
                , poster_image
                , year
                , type
                , rate
                , trailer_youtube):
       self.title = movie_title
       self.storyline = movie_storyline
       self.poster_image_url = poster_image
       self.year = year
       self.type = type
       self.rate = rate
       self.trailer_youtube_url = trailer_youtube



class Serie(Movie):
    """
    Create serie object
    init the input arguments for serie
    """
    def __init__(self
                 , movie_title
                 , movie_storyline
                 , poster_image
                 , year
                 , type
                 , rate
                 , trailer_youtube
                 , episodes):
        """inheritance from Movie to Serie class"""
        Movie.__init__(self
                , movie_title
                , movie_storyline
                , poster_image
                , year
                , type
                , rate
                , trailer_youtube)
        self.episodes = episodes
pass


def show_trailer(self):
    """
    Method to open browser and show trailer of movie or serie
    """
    webbrowser.open(self.trailer_youtube_url)
