#Created By - ApTr13
#apurvatripathi13@gmail.com

import webbrowser

#Building Movie class for repeative use
class Movie():
    #Defining __init__ function to allocate space for a movie
    def __init__(self,title,storyline,poster,trailer):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer

    #Defining function to show trailer of a movie
    def show(self):
        webbrowser.open(self.trailer)
