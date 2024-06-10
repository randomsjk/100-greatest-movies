# no LLMs were used for this assignment

from bs4 import BeautifulSoup # imports BeautifulSoup library
import requests # imports requests library

html_text = requests.get("https://www.empireonline.com/movies/features/best-movies-2/").text # .get method grabs html text from web page
souped_html = BeautifulSoup(html_text,'lxml') # creates beautiful soup object from html text using lxml

movies = souped_html.find_all('h3', class_="listicleItem_listicle-item__title__BfenH") # find_all method grabs all elements with defined conditions and puts them in ResultSet object
movies.reverse() # reverses the order of elements in ResultSet object, which acts a bit like a list
movies_list = [] # initialises a normal list variable

for movie in movies: # iterates through ResultSet elements in ResultSet object 'movies'
    movies_list.append(movie.text.strip()) # builds list of strings from ResultSet
for i in range(len(movies_list)): # iterates through list allowing for editing of list elements in the loop
   movies_list[i] = movies_list[i][movies_list[i].find(" ")+1:].strip() # formats strings so it is only the movie names, uses string splicing

with open("greatest_movies.txt", "w", newline="", encoding="utf-8") as txtfile: # opens text file in write mode
  for i in range(len(movies_list)): # iterates through list in a way which keeps track of the number for numbering list
    txtfile.write(f"{str(i+1)}) {movies_list[i]}\n") # writes each movie in the list to the text file, numbering them
