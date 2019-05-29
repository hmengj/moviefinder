#!/usr/bin/python3
from bs4 import BeautifulSoup
from requests import *


class reviewStruct:
    def __init__ (self, movie_url):
        self.url = movie_url
        self.review_list = findReviews(movie_url)

def findReviews(url):
    review_url = 
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    #ASSUMING ALREADY HAVE REVIEWS
    for review in review_list:
