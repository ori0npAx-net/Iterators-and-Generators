from iterable import PowerOfTwoIterable
from iterator import PowerOfTwoIterator

print ("=== DEMO:PowerOfTwoIterator ===")

if __name__=="__main__":
    powers = PowerOfTwoIterator(4)
    power_2=PowerOfTwoIterable(3)
  
"""USING ITERATOR CLASS (with reset)"""   

print("\n----Using Reset Function----\n")
print ( "\n FIRST ITERATION:" )
for num in powers:
    print(num, end=" ")
 
print ("\n SECOND ITERATION:")
for num in powers:
    print(num, end=" ")
print ("No output since iterator is exhausted")

print( "\n THIRD ITERATION:")  
print ("resetting the counter.....")  
powers.reset()
for num in powers:
    print(num, end=" ")

"""USING ITERABLE CLASS (without reset)"""

print ("\n\n----Using Iterable Class----\n")
print ( "\n FIRST ITERATION:" )
for num in power_2:
    print (num,end=" ")
    
print ("\n SECOND ITERATION:")    
for num in power_2:
    print (num,end=" ")

print( "\n THIRD ITERATION:")  
for num in power_2:
    print (num,end=" ")

print ("\n=== DEMO SUCCESSFUL ===")

