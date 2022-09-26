import functools

some_pirate_list = [1,2,3,4,5,6]                    #this is the "variable outside the function"

def sum_pirates_list(*args):                        #Feeding in the *args
    pirate_list =list(args)                         #converting the tuple into a list
    sum_of_list = sum(pirate_list)                  #finding the sum
   #print(sum_of_list)                              #I couldn't tell if the instructions want us to print from inside the
    return sum_of_list


#Feeding the iterable "some_pirate_list" into the function "sum_pirates_list" and 
#some_pirate_list = sum_pirates_list(*some_pirate_list) #setting that equal to some_pirate_list to replace a list with it's sum.
#print(some_pirate_list)                             #Print the output of that above.
print(sum_pirates_list(*some_pirate_list))          #Same thing less lines

#Now I will do it will the map function and lambda. I just usually use *interable in my code. I have never used map until this class.
#pirates_map = functools.reduce(lambda x,y : x+y , some_pirate_list)
print(functools.reduce(lambda x,y : x+y , some_pirate_list))

