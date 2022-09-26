"""What are your thoughts on multi-line comments?
    I tell my students not to use them without a good reason... but I am not very good with rules."""
quit = 0
#Welcome
print("Hello Dr. Garlington")
while quit != 1:
    print("Would you like to play a game?\n") # Did you like the movie war games?

    #Hook the audience with a gag
    game = input("yes/no\n")
    if game == "yes" or game=="Yes":
        print("TOO BAD... we are here to work!") # since I didn't include a binary menu here you could put in whatever with no error.

    #I think I want a menu... not sure why I don't just submit different files... 
    print("Choose a program please")

    choice = int(input("1,2, or 3?\n"))
    if choice == 1:
        # Actual Program 1 : I had a weird day at work and I am taking it out on this program it seems
        numbero = int(input("Choose an integer\n"))         #typecast the input into an int from string - can get an error here if input isn't castable
        if numbero % 2 == 1:                                #Check for oddness with modulo 
            print(f"That's easy, {numbero} is odd!")
        elif numbero % 2 == 0:                              #Check for eveness with modulo 
            print(f"That's easy, {numbero} is even!")
        else:
            print("WHAAAATTTT!!!! You picked an integer that isn't even or odd?! Call the nobel committee")
    elif choice == 2:
        #program 2 - average of integers
        listymclistface=[]                  #Empty list to hold ints
        loops = 0
        sums = 0
        length_of_list = int(input("How many numbers you got there man?\n"))
        #l=length_of_list                   #I was going to do something here, but changed my mind. Kept it in case I change it back.
        for i in range(length_of_list):
            numberss = int(input("Number?  "))
            listymclistface.append(numberss)        #At first i thought this was var += var.append(var2)
            loops += 1
            sums += numberss
            avg_so_far = sums/loops
            print(f"I have looped {loops} times and the running total is {sums}. The Avg so far is {avg_so_far}")
        print(f"Final average is {avg_so_far}")

    #program 3
    elif choice == 3:
        h = float(input("Enter the height from which the ball is dropped: "))
        b = float(input("Enter the bounciness index of the ball: "))
        if b > 1:
            print("This ball would bounce away to the moon if you gave it enough bounces!")
        time = int(input("Enter the number of times the ball is allowed to continue bouncing: "))
        distance = 0
        new_height = 0
        #for loop running for time times
        for t in range(time):
            distance = distance + (h)
            new_height = h*b #this is redundant - but I like how the variable does the work of a comment as it is so well named 
            h = new_height
        print("Total distance traveled is: " + str(distance) + " units.") #I can do it the hard way too


    else:
        print("So you aren't good at following directions either? or just doing edge testing for me?\n\nI wish python just had real switch cases")

    again = int(input(" Do you want to go again? \nyes = 0\nno = 1 \n"))
    
    if again == 1:    #Close it all
        break