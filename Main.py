#Created By - ApTr13
#apurvatripathi13@gmail.com
#---------------------
#This file must be made to Run on your device to generate fresh_tomatoes.html
#---------------------

import Media
import fresh_tomatoes

# 6 Movies with their Title, Storyline, Poster & Trailer....

#1.Justice League (2017)
justice = Media.Movie("Justice League",
                      "Heores of DC united to fight the biggest enemy of humankind, Dark Reid",
                      "http://orig08.deviantart.net/d09f/f/2016/087/a/0/justice_league_2017_concept_movie_poster_by_megomagdy15-d9wu92n.jpg",
                      "https://www.youtube.com/watch?v=fIHH5-HVS9o")

#2.Suicide Squad (2016)
ss = Media.Movie("Suicide Squad",
                 "An squad of extraordinary superhumans that are turned into villains by a mad clown",
                 "http://cdn.collider.com/wp-content/uploads/2016/01/suicide-squad-movie-poster-first.jpg",
                 "https://www.youtube.com/watch?v=CmRih_VtVAs")

#3.Batman - The Kiling Joke (2016)
joke = Media.Movie("Batman - The Killing Joke",
                   "Batman must save Gordon from the Joker's twisted quest to make him insane",
                   "http://images.fandango.com/r101.1.1/ImageRenderer/300/0/redesign/static/img/noxsquare.jpg/118972/images/masterrepository/fandango/193474/batman_250x375_r5.jpg",
                   "https://www.youtube.com/watch?v=iC8NdK2Cwd4")

#4.Batman vs Superman - Dawn Of Justice (2016)
dawn = Media.Movie("Batman v Superman",
                   "The biggest battle in history; Batman vs Superman, and the Dawn of Justice league.",
                   "http://orig10.deviantart.net/83aa/f/2015/277/6/b/batman_v_superman__2016____theatrical_poster_by_camw1n-d93o9wa.jpg",
                   "https://www.youtube.com/watch?v=Cle_rKBpZ28")

#5.Wonder Woman (2017)
wonder = Media.Movie("Wonder Woman",
                     "The story of the immortal demigoddess, Princess Diana and her heroics in World War-1",
                     "http://s3.birthmoviesdeath.com/images/made/Wonder-Woman-Poster_1200_1778_81_s.jpg",
                     "https://www.youtube.com/watch?v=5lGoQhFb4NM")

#6.Man Of Steel - Superman(2013)
steel = Media.Movie("Man Of Steel",
                    "The Story about the origin and rise of the Man Of Steel - Superman",
                    "http://orig13.deviantart.net/4674/f/2013/124/3/b/man_of_steel_by_visuasys-d6431v4.jpg",
                    "https://www.youtube.com/watch?v=T6DJcgm3wNY")

#Array Of All the Movies
movies = [justice, ss, joke, dawn, wonder, steel]

#Calling Function to generate fresh_tomatoes.html page 
fresh_tomatoes.open_movies_page(movies)
