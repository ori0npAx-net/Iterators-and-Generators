"""
ITERABLE CLASS
"""
from reader import Reader

class Book:
    def __init__(self,title,pages):
        self.title=title
        self.pages=pages
        
    def new_reader(self,name):
        return Reader(self.pages,name)
        