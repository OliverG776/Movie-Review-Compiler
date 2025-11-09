class Map:
    # A hash map implementation that takes in 4 values
    
    # (movieTitle, genreList, averageRating, year)
    #     with the movie title being the keys
    
    # The load factor of this map is 0.7

    def __init__(self):
        #Initializes an array with size 10
        self.mapContainer = [None] * 10
        self.load_factor = 0.0
        self.buckets = 0 #Number of slots that have been used so far

    
    #     Allows for syntax such as 
    #     map["Toy Story"] = (["Children's, Comedy], 3.9, 19999)

    def __setitem__(self, title, values):
        genres, rating, year = values
        self.insert(title, genres, rating, year)

    #   Allows for syntax such as 
    #   map["Toy Story"] to retrive the tuple containing all 4 values
    
    def __getitem__(self, key):
        index = self.search(key)
        if index == -1:
            return False
        else:
            return self.mapContainer[index]

    #Hashes the key values by the sum of their characters by powers of 27"
    
    def hash(self, key):
        pow = 0
        sum = 0
        for i in str(key):
            sum += ord(i)*27**pow
            pow+=1
        return sum%len(self.mapContainer)


    # Quadratic probing to resolve hash collisions.
    # Finds the next available slot using (index + i^2) % table_size
    
    def probe(self, index):
        pow = 1
        newIndex = index
        while not(self.mapContainer[newIndex] is None):
            newIndex = (index + pow**2) % len(self.mapContainer)
            pow += 1
        return newIndex
    
    # Insertion into map here using tuple:
    # (movie title, genre list, average rating, release year)
    def insert(self, title, genres, rating, year):
        keyHash = self.hash(title)
        if self.mapContainer[keyHash] is None:
            self.mapContainer[keyHash] = (title,genres,rating,year)
            self.buckets += 1
        else:
            keyHash = self.probe(keyHash)
            self.mapContainer[keyHash] = (title,genres,rating,year)
            self.buckets+=1

        self.load_factor = self.buckets / len(self.mapContainer)
        if self.load_factor > 0.7:
            self.resize()

     # Doubles the table size and reinserts all existing elements
    
    def resize(self):
        oldMap = self.mapContainer
        newSize = len(self.mapContainer)*2
        self.mapContainer = [None]*newSize
        self.buckets = 0
        for i in oldMap:
            if i:
                self.insert(i[0],i[1],i[2],i[3])
        self.load_factor = self.buckets/len(self.mapContainer)

     # Searches for a movie title in the map using quadratic probing
    
    def search(self, key):
        keyHash = self.hash(key)
        power  = 0
        index = keyHash
        while power<len(self.mapContainer) and not(self.mapContainer[index] is None):
            if self.mapContainer[index][0]==key:
                print(self.mapContainer[index][0])
                return index
            power += 1
            index = (keyHash + power**2) % len(self.mapContainer)
        return -1

     # Returns a list of movie titles that contain the given genre

    def searchByGenre(self, genre):
        newList = []
        for i in range(len(self.mapContainer)):
            if genre in self.mapContainer[i][1]:
                newList.append(self.mapContainer[i][0])
        return newList

