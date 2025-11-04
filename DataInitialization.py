from map import Map
import os
import csv

script_directory = os.path.dirname(__file__)
movies_directory = os.path.join(script_directory,"pages/movies.csv")
ratings_directory = os.path.join(script_directory,"pages/ratings.csv")

movieMap = Map()

#READ:

#This is just for testing, this code is legit super slow bc i just wanna test that I can actually mess w/ the map lmao
#Kevin if you see this, please make this faster or we will get a fat 0

with open(movies_directory, newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    i = 1
    for row in reader:
        print("Number: " + str(i))
        print("Film ID: " + str(row[0]))
        i+=1
        #print(row[0])
        #print(row[1])
        #print(row[2])

        currentID = row[0]
        totalReviews = 0.0
        scoreTotal = 0.0

        with open(ratings_directory, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)


            for row in reader:
                if currentID == row[0]:
                    scoreTotal += float(row[2])
                    totalReviews += 1
        print("scoreTotal: " + str(scoreTotal))
        print("totalReviews: " + str(totalReviews))
        if(totalReviews != 0):
            print("Net Review: " + str(scoreTotal/totalReviews) + "\n")

        if(totalReviews != 0):
            movieMap.insert(row[1], row[2], scoreTotal/totalReviews)
