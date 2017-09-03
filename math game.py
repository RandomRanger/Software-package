#Computer Programming - Math Challenge by Jacob and Owen

import random
import time

class Math_game(object):

    def __init__(self):

        print("Welcome to the Official Math Game By Jacob and Owen\nYou will have at least five relatively simple questions,\nand up to ten difficult ones.\nGood luck!")
        time.sleep(5)
        x = 3
        while x != 0:
            print("Starting in ",x,"...")
            time.sleep(1)
            x -= 1

        #Above we can see the intro with the time countdown.


        self.tried = 0
        self.correct = 0
        self.easyQuestionsAsked = 0
        self.numCorrect = -1


        #The __init__ method is simply the initiating object. When an object of the class is made, this method/function is automatically called.
        #By automatically declaring all of these objects, we can start keeping track of the number of questions attempted, correct, etc.

    def prob(self, maximum, operators):

        self.maximum = maximum
        self.operators = operators
        self.num_a, self.num_b = [random.randint(1,self.maximum),random.randint(1,self.maximum)]

        #In the above line, we are able to declare two variable values in one, efficient line.

        operators = ['+','-','*']

        self.operator = operators[random.randint(0,int(self.operators))] 

        #The operators parameter of the "prob" method is used to access the list of operators, If only two operators are available to use, a random number
        #chooses between + or -. Otherwise, it will choose between + or - or *.

        if self.maximum < 50:

            if self.num_a <= self.num_b:
                self.num_a = random.randint(1,self.maximum)

        #If it is an easy problem and we are not allowed to use negatives, and the first number is smaller than the second, just default to 25.

        if self.operator== '+':
            self.answer = self.num_a + self.num_b
        elif self.operator == '-':
            self.answer = self.num_a - self.num_b
        else:
            self.num_a, self.num_b = random.randint(-12,12), random.randint(-12,12)
            # If we are using the multiplication operator, set the numbers to max out at 12, or be as low as -12.
            self.answer = self.num_a * self.num_b



        #Above, we use the parameter, userself.answer, and see if the self.answer is correct. Below, we the returned value is whether the user correctly self.answered the question.

        return self.num_a, self.operator, self.num_b


    def isCorrect(self, userInput):

        self.userInput = userInput
        #Simply returning whether the user answer was correct or not.
        return self.userInput == self.answer



game = Math_game()
#Make an object of the  Math_game class.
while game.tried <= 15:
    if game.easyQuestionsAsked <= 5:
        game.prob(25,1)
        game.easyQuestionsAsked += 1
        #While we have not asked 15 questions yet, and while there have been less than 5 easy questions asked, ask another easy question.
    else:
        game.prob(50,2)
    userAnswer = int(input("Problem:  {0} {1} {2}  :  ".format(game.num_a, game.operator, game.num_b)))
    #If we do not HAVE to ask an easy question, feel free to ask a hard one.

    if game.isCorrect(userAnswer):
        game.numCorrect += 1
        print("Correct!")
    else:
        print("Incorrect!")
    game.tried += 1
    #Accumalting questions asked.

if game.numCorrect > 11:
    print("Great job! ({0}/15)".format(game.numCorrect))
else:
    print("Well done, Try again for a better score! ({0}/15)".format(game.numCorrect))
print("This program will automatically close in ten seconds.")

time.sleep(10)
quit()
