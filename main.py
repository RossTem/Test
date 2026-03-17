from irsystem import MovieIRS
from movie import Movie
import csv

def movie():
    
    print("--- Testing Movie class ---")
    
    # Author: Alan Pasillas
    movie1 = Movie(id="12345",title="The conjuring",release_date="1/2/2005",popularity="1233",vote_average="6.8",runtime="99",genre_names="Horror, Mystery")

    # Author: Alan Pasillas
    try:
        movie1.id = "Banana"
    except Exception as e:
        print("Error: ", e)

    # Author: Alan Pasillas
    try:
        movie1.id = ""
    except Exception as e:
        print("Error: ", e)  

    # Author: Alan Pasillas
    try:
        movie1.title = ""
    except Exception as e:
        print("Error: ", e)

    # Author: Kener Zamora - Testing invalid popularity
    # Popularity as a string input: ValueError
    try:
        movie1.popularity = "movie"
    except ValueError as e:
        print("Caught exception:", e)
    
    # Popularity as a negative number: ValueError
    try:
        movie1.popularity = -32
    except ValueError as e:
        print("Caught exception:", e)    

     # Author: Kener Zamora - Testing invalid runtime
     # Runtime as a string input: ValueError
    try:
        movie1.runtime = "eighty"
    except ValueError as e:
        print("Caught exception:", e)

    # Runtime as a value less than or equal to 0: ValueError
    try:
        movie1.runtime = 0  
    except ValueError as e:
        print("Caught exception:", e)   

    # Author: Kener Zamora - Testing valid popularity and runtime
    # Popularity as a positive interger: No Error
    try:
        movie1.popularity = 2332
        print("No Error in popularity")
    except ValueError as e:
        print("Error:", e)
    
    # Runtime as a positive integer: No Error
    try:
        movie1.runtime = 130
        print("No Error in runtime")
    except ValueError as e:
        print("Error:", e)   

    # Author: Adrian Sandoval-Vasquez - Testing invalid vote average
    # Vote average as a string: Should raise Exception
    try:
        movie1.vote_average = "movie1"
    except Exception as e:
        print("Error:", e)
    
    # Author: Adrian Sandoval-Vasquez - Testing valid vote average
    # Vote average as a float: No Error expected
    try:
        movie1.vote_average = 6.8
        print("No Error:", e)
    except Exception as e:
        print("Error:", e)

    # Author: Adrian Sandoval-Vasquez - Testing invalid genre names
    # Genre names as a non-string (integer): Should raise Exception
    try:
        movie1:genre_names = 123
    except Exception as e:
        print("Error:", e)

    # Author: Adrian Sandoval-Vasquez - Testing valid genre names
    # Genre names as a comma-separated string: No Error expected
    try:
        movie1:genre_names = "Horror, Mystery"
        print("No Error")
    except Exception as e:
        print("Error:", e)

    # Author: Adrian Sandoval-Vasquez - Testing invalid release date
    # Release date as an integer: Should raise Exception
    try:
        movie1.release_date = 20220101
    except Exception as e:
        print("Error:", e)
    
    # Author: Adrian Sandoval-Vasquez - Testing valid release date
    # Release date as a string: No Error expected
    try:
        movie1.release_date = "1/2/2005"
        print("No Error")
    except Exception as e:
        print("Error:", e)   


    system = MovieIRS()

    system.read_movies("horror_movies.csv")

    system.compare_movies(760161,760741)



if __name__ == "__main__":
    pass