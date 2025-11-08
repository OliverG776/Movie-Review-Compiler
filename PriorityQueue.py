#Gameplan:
#Implement a list of the top 100 films, which includes the film's ranking, film title, release year, and overall rating score

class PriorityQueue:
    def __init__(self):
        self.heapContainer = [None] * 10
        self.size = 0


    #Was Really Redundant Using These, Cleaner Without Them, Kept in Case You Need Them For UI
    # def getParent(self, index):
    #     if (int)((index-1)/2) < 0:
    #         return None
    #     else:
    #         return self.heapContainer[(int)((index-1)/2)]
    #
    # def getLeftChild(self, index):
    #     if 2*index+1 >= self.size:
    #         return None
    #     else:
    #         return self.heapContainer[2*index+1]
    #
    # def getRightChild(self, index):
    #     if 2*index+2 >= self.size:
    #         return None
    #     else:
    #         return self.heapContainer[2*index+2]

    def resize(self):
        oldContainer = self.heapContainer
        newSize = len(self.heapContainer)*2
        self.heapContainer = [None]*newSize
        for i in range(len(oldContainer)):
            self.heapContainer[i] = oldContainer[i]


    def insert(self, title, rating):
        if self.size == len(self.heapContainer):
            self.resize()
        self.heapContainer[self.size] = (title, rating)
        self.size += 1
        self.heapifyUp()

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

    def pop(self):
        if self.size == 0:
            return None
        self.heapContainer[0] = self.heapContainer[self.size-1]
        self.heapContainer[self.size-1] = None
        self.size -= 1
        self.heapifyDown(0)

    def top(self):
        return self.heapContainer[0]

    def getTopThousand(self):
        topThousand = []
        for i in range(1000):
            topThousand.append(self.top())
            self.pop()
        return topThousand
