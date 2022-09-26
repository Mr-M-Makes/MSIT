#program 1 part 1
def helloWorld():                           # I was torn on the naming of this function. 
                                            #I felt like the PEP8 style suggested hello_world but descriptive 
                                            #naming practices gave HelloWorld... so you got helloWorld
    """HelloWorld prints \"HelloWorld\" and 
    returns nothing."""                     #I am not sure how to use doc strings and actually get them to show
    print("HelloWorld")                     #in an IDE.

                                            #I would normally just let my comments extend a litte farther instead of using these
                                            #"multi-line" comments but I am trying to fit it all in a screen shot.
# Program 2 part 2
variable_global = 42                        #Global Variable

def variable_fun():
    lv = variable_global *2                 # Local Variable

    #sum_of_vars = lv + variable_global     #Alternate method that would make a local varible that would be useful if we needed to return it
    #print(sum_of_vars)

    print(lv + variable_global)             #print variable addition


if __name__ == "__main__":                  #this will run these two commands if this file is run. They will not be run if the file is imported as a module.
    helloWorld()                            #module. This lets us test the functions outside of having to call them in file through an
    variable_fun()                          #when we are creating a module or library.