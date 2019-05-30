#!/usr/bin/python3
from bs4 import BeautifulSoup
from requests import *
from classHeader import profile



def findReviews(url):
    for i in range(1,5):
        review_page_url = "https://letterboxd.com" + url + "reviews/by/activity/page/" + str(i)
        response = get(review_page_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            for list_element in soup.findAll("li", {"class": "film-detail"}):
                for review in list_element.findAll("meta", itemprop="ratingValue"):
                    rating = review["content"]
                    print(rating)
                for metadata in list_element.find("strong", {"class": "name"}):
                    curr_metadata = metadata["href"]
                    reviewer_name = metadata.text
        except:
            print("out of reviews: \n" + review_page_url)



findReviews("/film/inception/")
