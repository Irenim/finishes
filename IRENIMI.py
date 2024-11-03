def interger_array(figures): # defining my function with a parameter
 odd=0 
 even=0  #} declaring  empty variables
 total=0
 for numbers in  figures: # looping through number/ reassigning figures to numbers 
    total+=numbers # adding the total numbers in the array together
    if numbers % 2==0: # checking for even numbers 
     even+=numbers  # adding the even numbers together
    if numbers % 2==1: # checking for odd numbers
     odd+=numbers # checking for the total of odd numbers 
 outcome=odd*even-total # checking for the outcome
 return outcome # returning the outcome to the function for the program to work
figures=[1,2,3,4,5,6,7,8,9,10] # declaring my array 
result=interger_array(figures)# calling my function with a literal
print(result) # end of the programdef interger_array(figures): # defining my function with a parameter
 