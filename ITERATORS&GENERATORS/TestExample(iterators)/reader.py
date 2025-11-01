"""
ITERATOR CLASS 
"""
import time

class Reader:
    def __init__(self,pages,name):
        self.pages=pages
        self.name=name
        self.index=0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.pages):
            raise StopIteration
        
        page=self.pages[self.index]
        print(f"{self.name} reads: {page}")
        self.index+=1
        time.sleep(0.5)
        return page
        
    
        