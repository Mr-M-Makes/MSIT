List1 =[1,2,3,4]; print(List1)  # Initialize a list and print it
List1.pop();List1.pop();print(List1) #Pop off the last two indices on the list and print it

tuple1 = (1,2,3,4,5,6,7,8);print(tuple1[2]);print(tuple1[-3]) # Initialize a tuple and print the 3rd and 3rd from last index
tuple_var1 = ("a", "b", "c", "d","e", "f", "g", "h", "i", "j")
print(tuple_var1[:6]);print(tuple_var1[1:8:2]);print(tuple_var1[-1:-4:-2]) #Print the 7th index then every other index between 1-8, then every other index going backwards between i-g
tuple_var2 = ("t", "u", "r", "i", "a", "l", "s", "p", "o","i", "n", "t")
print(tuple_var2[1:]);print(tuple_var2[:2]);print(tuple_var2[5:12]);print(tuple_var2[::5]) #print everything after the first index, everything before the 3rd, then between 6-13, and skip by 5s

numTuple = (11,22,33,44,55,66,77,88,99,100)
print(numTuple[2:4]);print(numTuple[4:]);print(numTuple[:6]);print(numTuple);print(numTuple[-5:-2])#print 3-5, everything after 5, before 7,all, and 66-88

list_swap = [1,2,3] #initialize a list
temp_swap = list_swap.pop(0);temp_swap2 = list_swap.pop() #make temp variable and pop the first index into it, then make second one and pop the end into it
list_swap.append(temp_swap);list_swap.insert(0,temp_swap2) # add the previous begining to end and the previous end to the begining
print(list_swap) # print the list

unknownset = [1,2,3];unknownset2 = (4,5,6)  # make a list and a tuple
new_list = list(unknownset2);unknownset.append(new_list);print(tuple(unknownset))#convert the tuple to a list. Append the list to the initial list. Convert back to a tuple. Print result
set1=(3,4);set2=[1,2];set3=list(set1) #in case you meant add each item from the list into the tuple as a new item in the list instead of adding the list to the tuple.
for i in range(len(set3)):x=set3[i];set2.append(x)#I was having trouble understanding what was requested, rather than having trouble coding it.
set4=tuple(set2);print(set4)
