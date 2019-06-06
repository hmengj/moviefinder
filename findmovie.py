#!/usr/bin/python3


import tempfile
from bs4 import BeautifulSoup
from requests import *
import classHeader
from movieDataHandler import findReviews
from classHeader import titlelinkTuple, profile
import threading


movie_list = []
in_table_building = True

def printMovieOptions(movie_list):
    i = 1
    for movie in movie_list:
        print(str(i) + " " + movie.title + " : " + movie.link)
        i+=1
        if(i > 10):
            break

def addToMovieList(in_movie_list, movie):
    in_movie_list.append(movie)
    print("fetching reviews for " + movie.title + "\n")


def makeMovieOptions(title, url):
    movie_options = []
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        for list_element in soup.find("ul", {"class": "results"}):
            for film in soup.findAll('div', {"class": "film-poster"}):
                if(film.has_attr('data-film-name')):
                    if title.lower() in film['data-film-name'].lower():
                        movie_options.append(titlelinkTuple(film['data-film-name'], film['data-film-link']))
    except:
        movie_options = []
    return movie_options


def appendMovieList(name, url):
    movie_options = makeMovieOptions(name, url)
    if(len(movie_options) < 1):
        print("No options available. Please check your spelling and try again.")
        tableBuilder()
    if(len(movie_options) == 1):
        movie_list.append(movie_options[0])
        print("adding " + movie_options[0].title + " to profile...\n")
        tableBuilder()
    if(len(movie_options) > 1):
        print("/n Possible Movies:\n")
        printMovieOptions(movie_options)
        choice = input("choose one by typing it's number/press enter to cancel:")
        if(choice == ""):
            tableBuilder()
        else:
            movie_list.append(movie_options[int(choice)-1])
            print("adding " + movie_options[int(choice)-1].title + " to profile...\n")
            tableBuilder()




def tableBuilder():
    name = input("Enter a movie you like, or press enter to continue:")
    if(name == ""):
        pass
    else:
        movie_url = "https://letterboxd.com/search/" + name
        print(movie_url)
        appendMovieList(name, movie_url)


if __name__ == "__main__":
    name = input("Enter the name of a movie you like:")#Get one movie
    movie_url = "https://letterboxd.com/search/" + name
    appendMovieList(name, movie_url)

    print("building user profile...")
    threads = []
    for item in movie_list:
        print("adding " + item.title + " to profile..." + "\n")
        curr = threading.Thread(name = item.title, target = findReviews, args = (item.link,),)
        threads.append(curr)
        curr.start()
    for thread in threads:
        print("joining " + thread.name)
        thread.join()
