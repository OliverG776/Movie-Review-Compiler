from map import Map
import streamlit as st
import os
import csv
import re

#READ:

#This is just for testing, this code is legit super slow bc i just wanna test that I can actually mess w/ the map lmao
#Kevin if you see this, please make this faster or we will get a fat 0
# lol got it
# I split into two different with loops so its not super slow, ratings needs to be first
# otherwise you cant get average in 2nd loop
def initializeData():
    
    if 'movieMap' in st.session_state:
        return st.session_state['movieMap']

    script_directory = os.path.dirname(__file__)
    movies_directory = os.path.join(script_directory,"pages/movies.csv")
    ratings_directory = os.path.join(script_directory,"pages/ratings.csv")

    genreCategories = {}
    movieMap = Map()

    #Opens the ratings file for the specific film using dictionary
    ratings = {}
    with open(ratings_directory, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        #Used for tallying score but is wildly inefficient, just used for testing
        for row in reader:
            currentID = row[1]
            score = float(row[2])
            # testing
            print("ID: " + str(currentID) + "Rating: " + str(score))

            # Current ID is key, rating is value, by the end of loop ID should have multiple
            # ratings ready inside value box for averaging
            if currentID not in ratings:
                ratings[currentID] = [score]
            else:
                ratings[currentID].append(score)
        # Testing the list of ratings for that ID
        print(ratings[currentID])


    # Opens movies file
    with open(movies_directory, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        i = 1
        for row in reader:
            #This is used for testing purposes

            #print("Number: " + str(i))
            #print("Film ID: " + str(row[0]))
            i+=1

            currentID = row[0]

            title = row[1]
            # This seperates title and year properly without cutting into title names sometimes
            match = re.match(r"(.*)\s\((\d{4})\)$",title)
            if match:
                movieTitle, movieYear = match.groups()
            else:
                movieTitle = title
                movieYear = "Year not found"
            
            # genre string, not put into list
            genreString = row[2] 
            genreList = genreString.split("|")
            for genre in genreList:
                if genre not in genreCategories:
                    genreCategories[genre] = []
                genreCategories[genre].append(movieTitle)

            # Get ratings average for this movie
            allRatings = ratings.get(currentID, [])
            if(len(allRatings) != 0):
                avgRating = sum(allRatings)/len(allRatings)
            else:
                avgRating = 0

            # Some films have no reviews for some reason so if the total reviews = 0 
            # then we dont wanna divide by 0
            movieMap.insert(movieTitle, genreList, avgRating, movieYear)
            print("Title: " + str(movieTitle) + " - " + str(movieYear))
            print("Average Rating: " + str(avgRating))
            print("Genres: " + str(genreList))
            print()

    st.session_state['genreCategories'] = genreCategories
    st.session_state['movieMap'] = movieMap
    return movieMap
