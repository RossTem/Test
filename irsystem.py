#TODO: implement your Information Retrieval Class Here
from movie import Movie
import csv

class MovieIRS:
    # Author: Kener
    def __init__(self):
        # List that stores Movie info
        self.__list_movie = []

    # Author: Kener
    def read_movies(self, filename):
        
        # Opens csv 
        with open(filename,'r', newline= '') as file:
            
            # Reads csv
            reader = csv.reader(file)
            next(reader)
            
            # Loops through file
            for row in reader:
                
                #id,title,release_date,popularity,vote_average,runtime,genre_names
                # Creates Movie objects from csv
                movie = Movie(
                    int(row[0]),         #id
                    row[1],              #title
                    row[2],              #release_date
                    float(row[3]),       #popularity
                    float(row[4]),       #vote_average
                    int(row[5]),         #runtime
                    row[6]               #genre_names
                )

                self.__list_movie.append(movie) 
    
    # Author: Kener
    def compare_movies(self, movie_id1, movie_id2):             
        movie1 = self.search_movies(movie_id1)
        movie2 = self.search_movies(movie_id2)

        print("Comparing movies:")
        print(movie1.title, "Rating -", movie1.vote_average)    
        print(movie2.title, "Rating -", movie2.vote_average)

        if movie1.vote_average > movie2.vote_average:
            print(movie1.title, "has higher vote rating")
        elif movie1.vote_average < movie2.vote_average:
            print(movie2.title, "has higher vote rating")
        else:
            print("Both movies have the same ratings of ", movie1.vote_average)

    # Author - Adrian 
    def search_movies(self, movie_id):
        # Loops through all the movies in the list
        for movie in self.__list_movie:
            if movie.id == movie_id:
                return movie
        # Return None if movie is not found
        return None

    # Author - Adrian    
    def add_movies(self, id, title, release_date, popularity, vote_average, runtime, genre_names):
        # Checks if the movie exists using the search
        if self.search_movies(id):
            print("Movie already exists.")
            return None 

        # Creates a new Movie object with the chosen attributes
        movie = Movie(
            id,             # Movie ID
            title,          # Movie Title
            release_date,   # Release date of the movie
            popularity,     # Popularity score
            vote_average,   # Average vote/rating
            runtime,        # Runtime in minutes
            genre_names     # Genre(s) as string
        )

        # Adds a new movie to the list
        self.__list_movie.append(movie)
        return movie # Returns a recently added movie

    #Author: Alan Pasillas
    def delete_movies(self, movie_id):
        #Loops through the movie list and checks for the ID in order to remove it.
        for movie in self.__list_movie:
            if movie.id == movie_id:
                self.__list_movie.remove(movie) 
            #Confirmation of deletion with movie name
            
                print("Movie deleted successfully. ", movie.title)
                return movie

        #Movie was not found
        print("Movie not found.")
        return None
    
    #Author: Alan Pasillas
    def update_movie(self, movie_id, new_title, new_release_date, new_popularity, new_vote_average, new_runtime, new_genre_names):
        movie = self.search_movies(movie_id)

        if movie is None:
            print("Movie was not found.")
            return None
        
        movie.title = new_title
        movie.release_date = new_release_date
        movie.popularity = new_popularity
        movie.vote_average = new_vote_average
        movie.runtime = new_runtime
        movie.genre_names = new_genre_names

        print("Movie was updated successfully.")
        return None

    #Author: Alan Pasillas
    def get_title(title):
        return movie.title()

    def sort_movie(self, id, title, release_date, popularity, vote_average, runtime, genre_names):
        self.__list_movie.sort(key=get_title)
