
#Mean is what most people mean when they say average.
def mean(numbers):
    sums = 0                                    #placeholder
    sums = sum(numbers)                         #finds the sum
    return sums/(len(numbers))                  #divides the sum by the length of list to find the arithmetic mean and returns the answer

#mode finds the most common value in the list. This finds the first mode. If there are more than 1 modes it will not find the others.
def mode(numbers):
    mode = max(numbers, key = numbers.count)    #Count makes a dictionary of how many of each there are. Max finds the key that has the highest value.          
    return mode                                 #The highest count is the mode. it returns mode

#finds the median. I had trouble with this one. I didn't realize that the sort list function sorts it in place. I thought it returns a sorted list.
def median(numbers):
    #print(numbers)                             #I used this for debugging the list sort function
    numbers.sort()                              
    #print(numbers)                             #Another troubleshooting line
    middle = len(numbers)//2                    #Integer division to find the index in the middle. because index starts at zero integer division gives
    #print(len(numbers))                         #exactly what we need as it is the middle of the list. another debugging line
    #print(middle)

    if len(numbers) % 2 == 0:                   #Eveness check - median equals middle-1 + middle+1 all divided by two.
        median = (numbers[middle]+numbers[middle+1])/2
        return median                           #return median
    else:
        return numbers[middle]                  #if odd return median
    


if __name__ == "__main__":
    
    numbers =[]

    num = int(input("How many numbers do you have? "))

    for x in range(num):
            
        inp = int(input("Next Number Please "))
        numbers.append(inp)
    #print(numbers)
    print(mean(numbers))
    print(median(numbers))
    print(f"{mode(numbers)} is a mode of the list. There may be others.")