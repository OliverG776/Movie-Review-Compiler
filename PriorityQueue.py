#Gameplan:
#Implement a list of the top 100 films, which includes the film's ranking, film title, release year, and overall rating score

class PriorityQueue:
    # A Max-Heap–based priority queue for storing movies
    # by their rating score.

    # Each element is a tuple:
    #     (title, rating)

    # The highest-rated movie is always at the top of the heap
    
    def __init__(self):
        #initializes an array with 10 elements to start
        self.heapContainer = [None] * 10
        self.size = 0 #Number of elements currently in the heap

    # Doubles the heap's capacity when full.
    # Copies all existing elements into the new larger container.
    
    def resize(self):
        oldContainer = self.heapContainer
        newSize = len(self.heapContainer)*2
        self.heapContainer = [None]*newSize
        for i in range(len(oldContainer)):
            self.heapContainer[i] = oldContainer[i]

    # Inserts a new (title, rating) pair into the heap.
    #  If the heap is full, it resizes automatically.
    def insert(self, title, rating):
        if self.size == len(self.heapContainer):
            self.resize()
        self.heapContainer[self.size] = (title, rating)
        self.size += 1
        self.heapifyUp()
        
   # Restores the heap property after insertion by moving the
   # newly added node upward as long as it's larger than its parent
    def heapifyUp(self):
        index  = self.size-1
        while index > 0:
            parentIndex = (int)((index-1)/2)
            if self.heapContainer[index][1]>self.heapContainer[parentIndex][1]:
                temp = self.heapContainer[index]
                self.heapContainer[index] = self.heapContainer[parentIndex]
                self.heapContainer[parentIndex] = temp
                index = parentIndex
            else:
                break

    # Restores the heap property after removing the top element
    # by moving the element at 'index' down until it is in the correct position.
    def heapifyDown(self, index):
        leftIndex = 2*index+1
        rightIndex = 2*index+2
        largestIndex = index
        if leftIndex < self.size and  self.heapContainer[leftIndex][1]>self.heapContainer[largestIndex][1]:
            largestIndex = leftIndex
        if rightIndex < self.size and self.heapContainer[rightIndex][1]>self.heapContainer[largestIndex][1]:
            largestIndex = rightIndex

        if largestIndex != index:
            temp = self.heapContainer[index]
            self.heapContainer[index] = self.heapContainer[largestIndex]
            self.heapContainer[largestIndex] = temp
            self.heapifyDown(largestIndex)

    
    # Replaces the root with the last element, decreases size,
    #  and restores the heap property
    def pop(self):
        if self.size == 0:
            return None
        self.heapContainer[0] = self.heapContainer[self.size-1]
        self.heapContainer[self.size-1] = None
        self.size -= 1
        self.heapifyDown(0)

    #  Returns the movie with the highest rating without removing it
    def top(self):
        return self.heapContainer[0]


    #Retrieves the top 1000 movies from the heap in order of rating
    def getTopThousand(self):
        topThousand = []
        for i in range(1000):
            topThousand.append(self.top())
            self.pop()
        return topThousand
