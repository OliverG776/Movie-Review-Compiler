
# Creating a priority queue using binary max-heap
# highest review value is at root
# top ten will be first 10 in queue
class PriorityQueue:

    # Constructor creates list
    def __init__(self):
        self.heap = []

    # Array representation for a Heap (0-indexed)
    def parent(self, i):
        return (i-1) // 2

    def leftChild(self, i):
        return 2*i+1

    def rightChild(self,i):
        return 2*i+2

    # Heapify
    def heapifyUp(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)
    
    # Heapify down whenever you need to dequeue
    def heapifyDown(self,i):
        left = 2*i+1
        right = 2*i+2
        parent = i

        if left < len(self.heap) and self.heap[left] > self.heap[parent]:
            temp = self.heap[left]
            self.heap[left] = self.heap[parent]
            self.heap[parent] = temp

        if right < len(self.heap) and self.heap[right] > self.heap[parent]:
            temp = self.heap[right]
            self.heap[right] = self.heap[parent]
            self.heap[parent] = temp

        if parent != i:
            print("swapped parent and child, swap again")
            self.heapifyDown(parent)


    # Functions
    # Insert new rating elements with tuple (rating, movie)
    # position of rating element matters
    # If we want the actors inside we can add to the tuple here
    def insert(self, rating, movie):
        self.heap.append((rating, movie))
        self.heapifyUp(len(self.heap)-1)

    # Pop an item from top (dequeue)
    def pop(self):
        if self.isEmpty():
            return
        secondLast = len(self.heap)-1
        temp = self.heap[0]
        self.heap[0] = self.heap[secondLast]
        self.heap[secondLast] = temp

        # Vector pop not recursive call
        topValue = self.heap.pop()
        # Heapify down at root
        self.heapifyDown(0)
        return topValue
    
    # Peek at top value
    def peek(self):
        if self.isEmpty():
            return
        return self.heap[0]

    # Print out the entire heap in a list
    def display(self):
        print(self.heap)

    # Check if heap is empty
    def isEmpty(self):
        return len(self.heap) == 0

    # Get the top ten rated movies
    def getTopTen(self):
        stack = []

        for i in range(10):
            popped = self.pop()
            if popped is None:
                break
            stack.append(popped)

        topTen = stack

        for insertBack in stack:
            self.insert(insertBack[0], insertBack[1])


        return topTen


# main function will REMOVE later
if __name__ == "__main__":
    pq = PriorityQueue()

    print(pq.peek())

    pq.insert(2.0, "Jumanji")
    pq.insert(4.0, "A New Hope")
    pq.insert(3.5, "The Grinch")
    pq.display()

    pq.pop()
    pq.insert(5.0, "War of the Worlds")
    pq.insert(4.5, "aksdjfnaadsfjkn")
    pq.insert(1.0, "Matrix")
    pq.insert(1.5, "Interstellar")
    pq.display()

    print(pq.peek())

    topTen = pq.getTopTen()
    for i in topTen:
        print(i)
