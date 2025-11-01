class Fibonacci:
    def __init__(self,number):
        self.number=number
        #self.count=0
        #self.a,self.b=0,1   
        #self  bhi istemal kiya ja sakta tha but we did not take that approach kiunke a and b ki values nae sirey se chahiyen thi
        #agar hum self istemal karty tou a and b ki values yaad rehti
        #we needed the fresh values of a and b i.e 0 and 1 agar hum self likhty to we wouldn't be using 0 and 1 instead last state wali istemal ho rahi hoti.  
        
        """ VERSION: 1"""                       #FOCUSES ON THE COUNT
    def fib_normal(self,num): # generates sequence treating the given number as the count (yani kitney number print karny hain sequence ke)
       a,b=0,1
       count=0
       while count<num:     #condition fixed to stop at the count if it becomes greater than the number
           yield a
           a,b=b,a+b
           count+=1
        
        
    """VERSION:2""" 
    def fib_by_range(self,num): #uses range 
        a,b=0,1
        for i in range(num):
            if i == num - 1:    #manually handling the comma problem 
                print (a)
            else:
                print(a, end=", ")
            a,b=b,a+b
            
    """VERSION:3"""                           #FOCUSES ON DATA
    def fib_by_max_value(self, max_value):    #gives sequence upto the maximum value(yani us number tak sequence deta hai jo number argument mein pass karwainge)
        a,b=0,1
        while a<=max_value:
            yield(a)
            a,b=b,a+b
               
    """VERSION:4"""
    def fib_infinite(self):    #prints infinite values we stop the function using if condition 
        a,b=0,1
        while True:
            yield a 
            a,b=b,a+b
            if a>50:
                break
            
    def __str__(self):         #for this code str is not used explicitly anywhere cuz it was not required 
        return str(self.number)


