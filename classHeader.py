#!/usr/bin/python3

class reviewer:
    def __init__(self, name, link, initial_rating):
        self.name = name
        self.link = link
        self.weight = initial_rating
        self.movie_list = [] #movie tuples with rating, title, and link



class titlelinkTuple:
    def __init__(self, title, link):
        self.title = title
        self.link = link

class profile:
    def __init__(self, name = "anonymous", movie_list = []):
        self.name = name
        self.movie_list = movie_list
        self.reviewer_dict = {}
        self.movie_dict = {}
