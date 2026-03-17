class Movie:
    def __init__(self, id, title, release_date, popularity, vote_average, runtime, genre_names):
        # id, title, release_date, popularity, vote_average, runtime, genre_names
        # Alan - ID, title
        self._id = id   # Movie identification number 
        self._title = title # Title of the movie
        # Kener - popularity, runtime
        self._popularity = popularity   # Movie popularity number
        self._runtime = runtime     # Movie runtime
        # Adrian - genre_names, release_date, and vote_average
        self._genre_names = genre_names
        self._release_date = release_date
        self._vote_average = vote_average

    #Getter and setter for ID

    # Author: Alan Pasillas
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        if id.isdigit():
            self._id = id
        elif id == "":
             raise ValueError("ID can not be empty string.") 
        else:
            raise ValueError("ID can not contain any letters.") 

    #Getter and setter for Title

    # Author: Alan Pasillas
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title:
             self._title = title
        else:
            raise ValueError("Title can not be empty string.")  
       
    # Author: Kener - popularity 
    @property
    def popularity(self):
        return self._popularity
        
    @popularity.setter
    def popularity(self, popularity):
        
        if not isinstance(popularity, (int, float)):
            raise ValueError("Popularity value is not a int or float")
        
        if popularity <= 0:
            raise ValueError("Popularity value has to be greater than 0")
        
        self._popularity = float(popularity)
    
    # Author: Kener - runtime
    @property
    def runtime(self):
        return self._runtime
          
    @runtime.setter
    def runtime(self, runtime):
        # TODO: Validate and set the author attribute
        if not isinstance(runtime, int):
            raise ValueError ("Runtime is not an interger")
        if runtime <= 0:
            raise ValueError("Runtime is greater than 0")
     
        self._runtime = runtime

    # Author: Adrian Sandoval-Vasquez
    # Genre names property
    @property
    def genre_names(self):
        return self._genre_names
        
    @genre_names.setter
    def genre_names(self, genre_names):
        if not isinstance(genre_names, (str, list)):
            raise ValueError("genre_names must be a string or a list.")
        
        if genre_names == "":
            raise ValueError("genre_names cannot be empty.")
        self._genre_names = genre_names

    # Author: Adrian Sandoval-Vasquez
    # Release date property
    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        if not isinstance(release_date, str):
            raise ValueError("release_date must be a string.")
        
        if release_date == "":
            raise ValueError("release_date cannot be empty.")
        else:
            self._release_date = release_date
        
    # Author: Adrian Sandoval-Vasquez
    # Vote average property
    @property
    def vote_average(self):
        return self._vote_average

    @vote_average.setter
    def vote_average(self, vote_average):
        if not isinstance(vote_average, (int, float)):
            raise ValueError("vote_average must be a number between 0 and 10.")
        
        if vote_average < 0 > 10:
            raise ValueError("vote_average must be 0-10.")
        
        self._vote_average = vote_average

    #Author: Alan Pasillas
    def __str__(self):
        return f'ID: {self._id}, Title: {self._title}, Popularity: {self._popularity}, Vote Average: {self._vote_average}, Runtime: {self._runtime}, Genre: {self._genre_names}'