#Jasdeep Sidhu
#Hangman Game
#Problem: Throughout quarantine, and when people have free time, they are often bored and seek a challenging and engaging activity to do in their spare time. One way to overcome this problem is to play an engaging game.
import random

#functions part0,part1,part2,part3,part4,part5, and,part6 are simply created to store the hangman images
def part0():
    print("\n[=======]")
    print("|   |")
    print("|")
    print("|")
    print("|")
    print("[=============]")

def part1():
    print("\n[=======]")
    print("|   |")
    print("|   o")
    print("|")
    print("|")
    print("[=============]")

def part2():
    print("\n[=======]")
    print("|   |")
    print("|   o")
    print("|   |")
    print("|")
    print("[=============]")

def part3():
    print("\n[=======]")
    print("|   |")
    print("|   o")
    print("|  /|")
    print("|")
    print("[=============]")

def part4():
    print("\n[=======]")
    print("|   |")
    print("|   o")
    print("|  /|\\")
    print("|")
    print("[=============]")

def part5():
    print("\n[=======]")
    print("|   |")
    print("|   o")
    print("|  /|\\")
    print("|  /")
    print("[=============]")

def part6():
    print("\n[=======]")
    print("|   |")
    print("|   o")
    print("|  /|\\")
    print("|  / \\")
    print("[=============]")

def intro_screen():
    #simple function to print a welcome message to the user
    print("\n****************************************")
    print("****************************************")
    print("          Welcome to Hangman!           ")
    print("****************************************")
    print("****************************************")
    print("Have Fun!")
    print("")

def game(game_continue,loop,z,random_word,word_list,win,victory):
    guessed = []
    #the following 3 lists contain the words that will be guessed by the user depending on which category they choose
    countries = ["canada","india","germany","russia","china","brazil","australia","austria","france"]
    animals = ["lion","tiger","dolphin","crocodile","octopus","kangaroo","dog","bear","turtle","elephant"]
    food = ["broccoli","pizza","oatmeal","watermelon","pineapple","burger"]
    #the while loop before runs while loop is equal to true, thus constantly repeating until, it is set to false (it is set to false if user types in valid input) (repeats until user types valid input)
    while loop == True:
        word = input("Enter your category! [countries/animals/food]: ").lower()
        if word == "countries":
            #loop value updates to false, so loop does not continue to run once valid input is entered
            loop = False
            #at the top of code it says import random, this is so we can select a random number from the list
            random_word = (random.choice(countries))
            #every letter in the word selected gets added to a list, which is later compared with another list that contains the letters guessed by the user
            word_list = list(random_word)
            print("\n------------------------------------------")
            part0()
            length = "_ " * len(random_word)
            print("Word:",length)
            print("Your word has:",len(random_word),"characters")
            print("------------------------------------------")


        elif word == "animals":
            #loop value updates to false, so loop does not continue to run once valid input is entered
            loop = False
            #at the top of code it says import random, this is so we can select a random number from the list
            random_word = (random.choice(animals))
            #every letter in the word selected gets added to a list, which is later compared with another list that contains the letters guessed by the user
            word_list = list(random_word)
            print("\n------------------------------------------")
            part0()
            length = "_ " * len(random_word)
            print("Word:",length)
            print("Your word has:",len(random_word),"characters")
            print("------------------------------------------")


        elif word == "food":
            #loop value updates to false, so loop does not continue to run once valid input is entered
            loop = False
            #at the top of code it says import random, this is so we can select a random number from the list
            random_word = (random.choice(food))
            #every letter in the world selected gets added to a list, which is later compared with another list that contains the letters guessed by the user
            word_list = list(random_word)
            print("\n------------------------------------------")
            part0()
            length = "_ " * len(random_word)
            print("Word:",length)
            print("Your word has:",len(random_word),"characters")
            print("------------------------------------------")
        #if none of the if/elif conditions above are met, this means the user did not enter a valid input, therefore, the loop value will remain true as the user must enter a valid input to continue
        else:
            #error message printed to screen prompting user to enter a valid input
            print("Please enter a valid option! [countries/animals/food]")
    #while loop below is constantly looping until game_continue is equal to False, this value will only be updated once user loses or wins
    while game_continue == True:
        guess = input("\nWhat letter do you think is in this word?: ").lower()
        #if the number the user guessed is not in the list guessed (which is filled with letters that the user already entered) AND the input entered is a letter AND the input entered is less than or equal to 1, then add that letter into the list guessed
        if guess not in guessed and len(guess) == 1 and guess.isalpha() == True:
            guessed.append(guess)
            print("The letters you have already guessed:",guessed)
            #for loop to loop through every digit in the random word, if that letter (x) is in the list of letters guessed by the user then they got the letter correct, and print it in the appropriate spot
            for x in random_word:
                if x in guessed:
                    print(x,end=" ")
                #if the guessed letter is not in the random word, then print _ as they did not guess it correctly.
                else:
                    print(" _ ",end=" ")
            #if the letter guessed by the user is not in the list containing the letters in the random word (word_list) then we know they guessed in correctly
            if guess not in word_list:
                print("\n")
                #everytime wrong letter is guessed z gets increased by 1, thus printing the appropriate hangman image to the screen using the functions containing the images
                z += 1
                if z == 1:
                    part1()
                    print(guess,"is not in the word!")
                    print("\n------------------------------------------")
                elif z ==2:
                    part2()
                    print(guess,"is not in the word!")
                    print("\n------------------------------------------")
                elif z ==3:
                    part3()
                    print(guess,"is not in the word!")
                    print("\n------------------------------------------")
                elif z ==4:
                    part4()
                    print(guess,"is not in the word!")
                    print("\n------------------------------------------")
                elif z ==5:
                    part5()
                    print(guess,"is not in the word!")
                    print("\n------------------------------------------")
                #if user guesses incorrectly 6 times they lose, and the following game over message is printed
                elif z ==6:
                    part6()
                    print(guess,"is not in the word!")
                    print("Hangman!, nice try")
                    print("\n------------------------------------------")
                    print("\n****************************")
                    print("GAME OVER")
                    print("You Lose")
                    print("The correct word was:", random_word)
                    print("****************************")
                    #game_continue value gets updated to False as game is over and should not continue (break while loop)
                    game_continue = False
            #for loop loops through each digit in list that contains each letter in the random word
            for x in word_list:
                #if that digit is in guess, then add 1 to win, if the win value is equal to the length of the random word, then the user has guessed every letter correctly
                if x in guess:
                    win += 1
                if win == len(random_word):
                    #update victory to True, so that the user knows they have won, otherwise victory remains False
                    victory = True
            #once the victory value gets set to True, the following victory message will get printed onto the screen
            if victory == True:
                print("\n****************************")
                print("You Win!")
                print("Great job!")
                print("The correct word was:",random_word)
                print("****************************")
                #game_continue will be updated to False so the loop stops running, thus indicating that the game has ended
                game_continue = False
        #If none of the if statements are met, then the user has entered an invalid statement, so we must print that to screen and ask the user to enter a valid input
        else:
            print("Invalid Input!")
            print("Only enter letters that you have not already guessed / Only single letter inputs!")
#function below asks user if they would like to play another round of hangman, it is called after the game function
def retry(x):
    #while loop runs until the value of x is updated to something other than 1
    while x == 1:
        #
        again = input("Would you like to play again? [Y/N]: ").lower()
        if again == "y":
            game(True,True,0,"temp","temp",0,False)
        elif again == "n":
            print("Thank you for playing!")
            x = 0

if __name__ == "__main__":
    intro_screen()
    game(True,True,0,"temp","temp",0,False)
    retry(1)
