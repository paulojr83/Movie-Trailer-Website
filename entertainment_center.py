import media
import fresh_tomatoes

beetlejuice = media.Movie("Beetlejuice"
                    , "Early Tim Burton is creepy, dark fun for tweens and teens."
                    , "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUwODE3MDE0MV5BMl5BanBnXkFtZTgwNTk1MjI4MzE@._V1_SY1000_CR0,0,675,1000_AL_.jpg"
                    , "1988"
                    , "Fantasy/Fantasy"
                    , "7.5/10"
                    , "https://youtu.be/GuyNP-XyFHs")

john_wick = media.Movie("John Wick: Chapter 2"
                    , "After returning to the criminal underworld to repay a debt, John Wick discovers that a large bounty has been put on his life."
                    , "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI4NjU3MTU0N15BMl5BanBnXkFtZTgwNjk5NzkzMTI@._V1_SY1000_CR0,0,674,1000_AL_.jpg"
                    , "2017 "
                    , "Crime film/Thriller"
                    , "8.5/10"
                    , "https://youtu.be/XGk2EfbD_Ps")

labyrinth = media.Movie("Pan's Labyrinth"
                    , "In the falangist Spain of 1944, the bookish young stepdaughter of a sadistic army officer escapes into an eerie but captivating fantasy world."
                    , "http://www.gstatic.com/tv/thumb/movieposters/162074/p162074_p_v8_ab.jpg"
                    , "2006"
                    , "Fantasy/Drama"
                    , "8.2/10"
                    , "https://youtu.be/M09mCcVgrsA")

resident_evil = media.Movie("Resident Evil: The Final Chapter"
                    , "The T-virus unleashed by the evil Umbrella Corp. has spread to every corner of the globe, infesting the planet with zombies, demons and monsters. Alice (Milla Jovovich), a former Umbrella employee turned rogue warrior, joins her friends on a last-chance mission to storm the company's headquarters located deep underneath what used to be Raccoon City. But the Red Queen (Ever Anderson) knows that Alice is coming, and the final battle will determine if the rest of mankind lives or dies."
                    , "http://t0.gstatic.com/images?q=tbn:ANd9GcQso5P8NaHjpqTQpL8NEqvYlgKEeAyGOg5wXt_pgxmjF2PnDbPf"
                    , "2016"
                    , "Fantasy/Science"
                    , "6.2/10"
                    , "https://youtu.be/79Sd4GtOXuI")

xXx = media.Movie("xXx: Return of Xander Cage"
                    , "After coming out of self-imposed exile, daredevil operative Xander Cage (Vin Diesel) must race against time to recover a sinister weapon known as Pandora's Box, a device that controls every military satellite in the world. Recruiting a new group of thrill-seeking cohorts, Xander finds himself entangled in a deadly conspiracy that points to collusion at the highest levels of government."
                    , "http://t1.gstatic.com/images?q=tbn:ANd9GcRPU0p7mNLVCK-s7fWgMgse9z_ScH_GZ_yu4VYTMyx6YkqAnwpf"
                    , "2017"
                    , "Fantasy/Drama"
                    , "5.6/10"
                    , "https://youtu.be/-ziu6JzJTZ0")

rings = media.Movie("Rings"
                    , "A young woman becomes worried about her boyfriend when he explores a dark subculture surrounding a mysterious videotape said to kill the watcher seven days after he has viewed it. She sacrifices herself to save her boyfriend and in doing so makes a horrifying discovery: there is a movie within the movie that no one has ever seen before."
                    , "https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/Rings-poster.jpg"
                    , "2017"
                    , "Fantasy/Drama"
                    , "4.5/10"
                    , "https://youtu.be/uukQ_6szDm8")

stranger_things = media.Serie("Stranger Things"
                    , "This thrilling Netflix-original drama stars award-winning actress Winona Ryder as Joyce Byers, who lives in a small Indiana town in 1983 -- inspired by a time when tales of science fiction captivated audiences. When Joyce's 12-year-old son, Will, goes missing, she launches a terrifying investigation into his disappearance with local authorities. As they search for answers, they unravel a series of extraordinary mysteries involving secret government experiments, unnerving supernatural forces, and a very unusual little girl."
                    , "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEzMDAxOTUyMV5BMl5BanBnXkFtZTgwNzAxMzYzOTE@._V1_.jpg"
                    , "2017"
                    , "Science Fiction, Supernatural fiction, Horror fiction, Mystery, Historical period drama"
                    , "9/10"
                    , "https://youtu.be/XWxyRG_tckY"
                    , 8)

#Create list of movies and series#
movies =[beetlejuice,john_wick,labyrinth,resident_evil,xXx,rings,stranger_things]

fresh_tomatoes.open_movies_page(movies)