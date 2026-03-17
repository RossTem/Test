from irsystem import MovieIRS



def movie_irs():

    system = MovieIRS()

    system.read_movies("horror_movies.csv")

    system.compare_movies(760161,760741)

    movie = print(system.search_movies(760161)) 
        
    print("\nTesting Update")
    system.update_movie(760161, "New Title", "1/1/2000", 100, 6.7,120, "Horror")
    movie = system.search_movies(760161) 
    print(movie)

    print("\nTesting Delete")
    system.delete_movies(760161)

if __name__ == "__main__":
    movie_irs()