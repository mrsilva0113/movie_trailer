import csv
import fresh_tomatoes
import media

movies = []

# Read CSV file; each line has a movie's content
with open('favorite_movies.csv', 'rb') as filehandler:
    fileparser = csv.reader(filehandler)
    for row in fileparser:
        movie = media.Movie(row[0], row[1], row[2], row[3])
        movies.append(movie)    # Create a list of movie objects
fresh_tomatoes.open_movies_page(movies)