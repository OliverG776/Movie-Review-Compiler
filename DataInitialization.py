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

#Opens movies file
with open(movies_directory, newline="", encoding="utf-8") as csvfile:

    reader = csv.reader(csvfile)
    next(reader)
    i = 1
    for row in reader:

        #This is used for testing purposes

        #print("Number: " + str(i))
        #print("Film ID: " + str(row[0]))
        i+=1
        #print(row[0])
        #print(row[1])
        #print(row[2])

        currentID = row[0]
        totalReviews = 0.0
        scoreTotal = 0.0

        #Opens the ratings file for the specific film

        with open(ratings_directory, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)

            #Used for tallying score but is wildly inefficient, just used for testing

            for row in reader:
                if currentID == row[0]:
                    scoreTotal += float(row[2])
                    totalReviews += 1
        #print("scoreTotal: " + str(scoreTotal))
        #print("totalReviews: " + str(totalReviews))
        # if(totalReviews != 0):
        #     #print("Net Review: " + str(scoreTotal/totalReviews) + "\n")

    #Splitting title up from year, idk if this actually works but it did for my SearchResults
    title = row[1].split("(")
    title[0] = title[0][:-1]



    #Some films have no reviews for some reason so if the total reviews = 0 then we dont wanna divide by 0
    if(totalReviews != 0):
        movieMap.insert(title, row[2], scoreTotal/totalReviews)
    else:
        movieMap.insert(title, row[2], 0)

    print("Title: " + str(title) + " Genres: " + str(row[2]))