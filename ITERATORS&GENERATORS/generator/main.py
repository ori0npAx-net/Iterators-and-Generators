from fibonacci import Fibonacci

if __name__=="__main__":
    obj=Fibonacci(5)
    
    print("\nnormal fibonacci:")
    print(list(obj.fib_normal(10)))
    
    print("\nby range fibonacci:")
    obj.fib_by_range(20)                        #no need of 'print' cuz the function itself is printing
    
    print("\nmax value fibonacci:")
    print(*obj.fib_by_max_value(10),sep=", ")   #printing without 'list' 
                                                #asterick is for unpacking the sequence, 'sep' separtes the element of the sequence by comma
    print ("\ninfinitoooo:")
    print(list(obj.fib_infinite()))
 

   
   
#obj.fib_by_range(10) 
#yeh is tarhan bhi chaly ga likn print kuch nahi hoga kiune humne function mein kuch print nahi karwaya hai yield ka lafz istemal kuya hai so tou print it all at once we use print ke sath list then function call
"""agar hum function mein print likhty hain then we don't need to print in the main just call the function.
likn iski wajah se comma separate karna is difficult so ya tou hum usko manually cater karenge ya join istemal 
karenge
agar hum function mein yield likhty hain the we have to write print in the main. cuz generator object hai tou 
usko list ka keyword use kar ke bhi likh ya tou * and 'sep' istemal kar ke print kar skty hain.
note that sep ka keyword is used when u have to print the statement once repeated print statements i.e in the 
loop istemal nahi karskty"""













        
