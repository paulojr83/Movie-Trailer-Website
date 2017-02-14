import  webbrowser

#Create Movie object#
class Movie():
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


#Create serie object#
class Serie(Movie):
    def __init__(self
                 , movie_title
                 , movie_storyline
                 , poster_image
                 , year
                 , type
                 , rate
                 , trailer_youtube
                 , episodes):
        #Inheritance from Movie#
        Movie.__init__(self
                , movie_title
                , movie_storyline
                , poster_image
                , year
                , type
                , rate
                , trailer_youtube)
        self.episodes = episodes

    #Method to open browser and show trailer of movie or serie#
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)