#!/usr/bin/python3
from bs4 import BeautifulSoup
from requests import *
from classHeader import profile, reviewer
import threading
import queue



def findReviews(url):
    for i in range(1,10):
        print(url + " " + str(i))
        review_page_url = "https://letterboxd.com" + url + "reviews/by/activity/page/" + str(i)
        response = get(review_page_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        try:
            current_movie_reviewer_list = []
            for list_element in soup.findAll("li", {"class": "film-detail"}):
                for review in list_element.findAll("meta", itemprop="ratingValue"):
                    rating = review["content"]
                    print(rating)
                for metadata in list_element.find("strong", {"class": "name"}):
                    reviewer_page_url = metadata["href"]
                    name = metadata.text
                current_movie_reviewer_list.append(reviewer(name, reviewer_page_url, rating))
        except:
            print("out of reviews: \n" + review_page_url)

    return current_movie_reviewer_list
