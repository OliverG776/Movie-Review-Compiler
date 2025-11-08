from map import Map
import streamlit as st
import os
import csv
import re

# initializes all the data from the csv files into the appropriate data structures
# Parses through movie titles, release years, genres, and ratings and stores them  
def initializeData():
    
    # Check if data inside the map is already loaded
    # if it is dont load again, otherwise continue
    if 'movieMap' in st.session_state:
        return st.session_state['movieMap']
    
    # Define file paths
    script_directory = os.path.dirname(__file__)
    movies_directory = os.path.join(script_directory,"pages/movies.csv")
    ratings_directory = os.path.join(script_directory,"pages/ratings.csv")

    # Each movie ID key gets all its attributed ratings as its values using dictionary
    ratings = {}

    # This usese a dictionary with each listed genre as a key and all the movie names as their values
    genreCategories = {}

    # This uses our custom Map class to store movie title, genre list, average rating, and release year
    movieMap = Map()

    with open(ratings_directory, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        #Used for tallying score but is wildly inefficient, just used for testing
        for row in reader:
            currentID = row[1]
            score = float(row[2])
            # testing
            # print("ID: " + str(currentID) + "Rating: " + str(score))

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
            # This uses re, python standard like regex
            match = re.match(r"(.*)\s\((\d{4})\)$",title)
            if match:
                movieTitle, movieYear = match.groups()
            else:
                movieTitle = title
                movieYear = "Year not found"
            
            # split genre string into multiple genre tags to add to genreList
            genreString = row[2] 
            genreList = genreString.split("|")
            
            # for each genre as a key add the movie title as a value to the genreCategories dictionary
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

            # Testing output
            print("Title: " + str(movieTitle) + " - " + str(movieYear))
            print("Average Rating: " + str(avgRating))
            print("Genres: " + str(genreList))
            print()

    # Stores the parsed genre dictionary and custom movieMap for use across any page 
    st.session_state['genreCategories'] = genreCategories
    st.session_state['movieMap'] = movieMap
    return movieMap
