class titlelinkTuple:
    def __init__(self, title, link):
        self.title = title
        self.link = link

class profile:
    def __init__(self, name = "anonymous", movie_list = []):
        self.name = name
        self.movie_list = movie_list
        self.reviewer_dict = {}
