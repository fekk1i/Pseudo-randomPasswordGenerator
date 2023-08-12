#imports the 'sys' built in function in order to use sys.exit at the end if neither inputs were correct
import sys
#asks the user to input either trn or pseudo to decide the code going to be used
initial = str(input("Please choose whether you want a TRN, a pseudo-generator, or file by entering 'TRN', 'pseudo', and 'file': "))
#initalizes the first if condition that determines which code to use depending on the users input
if (initial=='TRN'):
    #Imports the time function
    import time
    #This returns the number of seconds passed since the start of the program as an int
    seconds = time.time()
   #Outputs the number of the seed which in this case is the time
    print("This is the time value", seconds)
    #Defines the Seed LCG
    def seedLCG(initVal):
        #Sets the "rand" as a global function
        global rand
        #sets rand as the initial val, as initial val is later set as the seconds value
        rand = initVal
    #defines the numbers of the random equation
    def lcg():
        a = 1140671485
        c = 128201163
        m = 2**24
        #sets rand as a global function 
        global rand
        #Sets rand = the equation of the random number
        rand = (a*rand + c) % m
        #returns rand over the modulus parameter
        return rand/m
    #Sets the rand as the system time
    seedLCG(seconds)
    #Sets the iterations of random numbers resulted
    xi=int(input("How many lines of random numbers do you want?: "))
    for i in range(xi):
        #Prints the initially defined function above
        print(lcg())
    '''    
    M = Modulus parameter
    A= Multiplier term
    C= Increment term
    Rand= Seed
    '''
#sets an elif function where the user inputs the pseudo code
elif (initial=='pseudo'):
    #same as the code above defines the initial function to be called upon later
    def seedLCG(initVal):
        #sets the rand as a global function
        global rand
        #sets the rand as initial value which is later changed to the seed inputed by the user
        rand = initVal
        #defines the second function which is the equation itself
    def lcg():
        a = 1140671485
        c = 128201163
        m = 2**24
        #sets rand as a global function in the second lcg
        global rand
        #sets rand = the lcg equation
        rand = (a*rand + c) % m
        #returns rand over the modulus 
        return rand/m
    #asks the user to input a number to be used as the seed
    seedinput=int(input("Please enter a seed number: "))
    #sets the seedLCG which is also the initval which has been set to rand as the seed
    seedLCG(seedinput)
    #asks the user for the number of lines he/she wants
    xii=int(input("How many lines of random numbers do you want?: "))
    for i in range(xii):
        #prints the lines of random numbers
        print(lcg())
    '''    
    M = Modulus parameter
    A= Multiplier term
    C= Increment term
    Rand= Seed
    ''' 
#starts the file code
elif (initial=='file'):
    #ask the user to choose a file name from the 'seed.txt','seed2.txt','seed3.txt'
    file_name = str(input("Please choose a file to read the seed from 'seed.txt', 'seed2.txt', 'seed3.txt','seed4.py', and 'seed5.py': "))
    #sets the seed as an initial zero
    seed=0
    #defines the file_window function
    def file_window():
    #sets the identifier file_name as a global one
     global file_name
     #the file name open file function
     file_name=seed.askopenfilename() 
     
    #same as the code above defines the initial function to be called upon later
    def seedLCG(initVal):
        #sets the rand as a global function
     global rand
        #sets the rand as initial value which is later changed to the seed inputed by the user
     rand = initVal
        #defines the second function which is the equation itself
    def lcg():
        a = 1140671485
        c = 128201163
        m = 2**24
        #sets rand as a global function in the second lcg
        global rand
        #sets rand = the lcg equation
        rand = (a*rand + c) % m
        #returns rand over the modulus 
        return rand/m
    #the main open command, with the r defining as read
    with open(file_name,"r")as file:
        #sets the seedlcg as an int readline
     seedLCG(int(file.readline()))
   
    #asks the user for the number of lines he/she wants
    xiii=int(input("How many lines of random numbers do you want?: "))
    #sets the number of lines the user wants
    for i in range(xiii):
        #prints the lines of random numbers
        print(lcg())
    '''    
    M = Modulus parameter
    A= Multiplier term
    C= Increment term
    Rand= Seed
    ''' 

else:
    #uses the else command to tell the user to enter one of specified strings and terminates the code
    print("Please enter a valid string")
    #terminates the code/ exits
    sys.exit()
