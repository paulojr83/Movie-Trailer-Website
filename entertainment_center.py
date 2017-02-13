import media
import fresh_tomatoes
beetlejuice = media.Movie("Beetlejuice"
                    , "Early Tim Burton is creepy, dark fun for tweens and teens."
                    , "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUwODE3MDE0MV5BMl5BanBnXkFtZTgwNTk1MjI4MzE@._V1_SY1000_CR0,0,675,1000_AL_.jpg"
                    , "https://youtu.be/GuyNP-XyFHs")

john_wick = media.Movie("John Wick: Chapter 2"
                    , "After returning to the criminal underworld to repay a debt, John Wick discovers that a large bounty has been put on his life."
                    , "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI4NjU3MTU0N15BMl5BanBnXkFtZTgwNjk5NzkzMTI@._V1_SY1000_CR0,0,674,1000_AL_.jpg"
                    , "https://youtu.be/XGk2EfbD_Ps")

labyrinth = media.Movie("Pan's Labyrinth"
                    , "In the falangist Spain of 1944, the bookish young stepdaughter of a sadistic army officer escapes into an eerie but captivating fantasy world."
                    , "http://www.gstatic.com/tv/thumb/movieposters/162074/p162074_p_v8_ab.jpg"
                    , "https://youtu.be/M09mCcVgrsA")


movies =[beetlejuice,john_wick,labyrinth]

fresh_tomatoes.open_movies_page(movies)