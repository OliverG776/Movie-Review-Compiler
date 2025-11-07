class Map:
    def __init__(self):
        self.mapContainer = [None] * 10
        self.load_factor = 0.0
        self.buckets = 0

    def __setitem__(self, title, values):
        genres, rating, year = values
        self.insert(title, genres, rating, year)

    def __getitem__(self, key):
        index = self.search(key)
        if index == -1:
            return False
        else:
            return self.mapContainer[index]


    def hash(self, key):
        pow = 0
        sum = 0
        for i in str(key):
            sum += ord(i)*27**pow
            pow+=1
        return sum%len(self.mapContainer)

    def probe(self, index):
        pow = 1
        newIndex = index
        while not(self.mapContainer[newIndex] is None):
            newIndex = (index + pow**2) % len(self.mapContainer)
            pow += 1
        return newIndex
    
    # Insertion into map here using tuple:
    # (movie title, genre list, average rating,
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

    def resize(self):
        oldMap = self.mapContainer
        newSize = len(self.mapContainer)*2
        self.mapContainer = [None]*newSize
        self.buckets = 0
        for i in oldMap:
            if i:
                self.insert(i[0],i[1],i[2],i[3])
        self.load_factor = self.buckets/len(self.mapContainer)


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


    def searchByGenre(self, genre):
        newList = []
        for i in range(len(self.mapContainer)):
            if genre in self.mapContainer[i][1]:
                newList.append(self.mapContainer[i][0])
        return newList
