#import random 
#import time
 
#def castDie():
    #input('Press any key to cast the die!')
  #  r = list(range(1, 7))
   # print('Result: ' + str(random.choice(r)))
 
 
   # while True:
      #  time.sleep(1)
       # castDie()
        
import time
name =input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
print("")

#wait for 1 second
time.sleep(1)

print("Start guessing...")
time.sleep(0.5)
word = "vivek"
guesses = ''
turns = 10




while turns > 0:         
    failed = 0             
    for char in word:      
        if char in guesses:    
            print (char)    

        else:
    
            print ("_"),     
       
            failed += 1   
    if failed == 0:        
        print( "You won" ) 

    
        break              

    print

    guess =input("guess a character:") 

    guesses += guess                    


    if guess not in word:  
 
     
        turns -= 1        
 
   
        print ("Wrong")
    
 
    
        print ("You have", + turns, 'more guesses')
 
        if turns == 0:           
    
    
            print( "You Loose")
 