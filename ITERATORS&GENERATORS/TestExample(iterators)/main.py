from book import Book

if __name__=="__main__":
     
     novel=Book("Python tales",["intro","lists","loops"])
     
     r1=novel.new_reader("ayesha")
     r2=novel.new_reader("bilal")
     
     next(r1)
     next(r1)
     next(r2)
     
     maria=novel.new_reader("maria")
     shaheer=novel.new_reader("shaheer")
     
     for i, page in enumerate(maria):       #enumeration wala loop
         if i==1:
             novel.pages.append("functions")
             
     print("shaheer reads now")
     
     for page in shaheer:
         pass

        
        