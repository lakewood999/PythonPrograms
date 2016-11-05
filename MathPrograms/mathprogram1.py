'''
Created by: Steven
Program: mathprogram1.py

This is a math program that asks the user to add a certain
number of hundreds, tens, and ones.  The questions come in sets
of 5, and one points is awarded to the user for each correct
answer on the first try.  The user must get a question correct
to continue!
'''

import random

points = 0
questionsAnswered = 0
global numberHundreds, numberTens, numberOnes
numberHundreds = 0
numberTens = 0
numberOnes = 0

def generateNumbers():
	global numberHundreds, numberTens, numberOnes
	numberHundreds = random.randint(1, 9)
	numberTens = random.randint(1, 20)
	numberOnes = random.randint(1, 100)

print("Please answer the questions.  You will receive one points for getting the question correct the first time!")
print()

while True:
	for eachPass in range(5):
		userCorrect = False
		generateNumbers()

		global answer
		answer = numberHundreds*100 + numberTens*10 + numberOnes*1
		
		while answer >= 1000:
			generateNumbers()
			answer = numberHundreds*100 + numberTens*10 + numberOnes*1
		
		print("What is the sum of", str(numberHundreds),"hundreds",str(numberTens),"tens and",str(numberOnes),"ones?")
		userAnswer = int(input("Answer: "))
		if userAnswer == answer:
				userCorrect = True
				points += 1
				print("Correct!\n")
		else:
			print("Sorry, incorrect!  Try again!")
	
		while userCorrect == False:
			userAnswer = int(input("Answer: "))
			
			if userAnswer == answer:
				userCorrect = True
				print("Correct!\n")
			else:
				print("Sorry, incorrect!  Try again!")
	
	questionsAnswered += 5
	userContinue = input("Would you like to answer 5 more questions? (y/n): ")
	print()
	if userContinue == 'n':
		break

score = points / questionsAnswered
print("Your score is:", str(score))
print("You answered", str(questionsAnswered),"and got", str(points),"questions correct the first time for you score!")
