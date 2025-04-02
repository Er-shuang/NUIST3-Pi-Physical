# Author: Nie Yujin
# Date: 2/4/25
# A quiz game where user answers questions and the quiz respond with a Green Light for every correct answer and a Red Light for every incorrct answer..


import RPi.GPIO as GPIO
import time

# NUIST Quiz Game in Python
def quiz():
    print('Welcome to the Python Quiz!')
    print('Answer the following questions: ')

# Qusetions and Answers
    questions = [
        "1) Which of the following is NOT a python data type?: a) int, b) float, c) rational, d) string, e) bool",
	"2) Which of the following is NOT a built-in operation in Python?: a) +, b) %, c) abs(), d) sqrt()",
	"3) In a mixed-type expression involving ints and floats, Python will convert: a) floats to ints, b) ints to strings, c) floats and ints to strings, d) ints to floats",
        "4) The best structure for implementing a multi-way decision in Python is: a) if, b) if-else, c) if-elif-else, d) try",
        "5) What statement can be executed in the body of a loop to cause it to terminate?: a) if, b) exit, c) continue, d) bresk"
    ]
    answers = [
	"rational",
	"sqrt()",
	"ints to floats",
        "if-elif-else",
        "break"
    ]
    score = 0

# Ask questions and ligth LED
    for i in range(len(questions)):
        user_answer=input(questions[i]).strip().lower()
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        if user_answer==answers[i]:
            print('Correct!')
            GPIO.setup(17,GPIO.OUT)
            GPIO.output(17,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(17,GPIO.LOW)
            score+=1
        else:
            print("Incorrect!")
            GPIO.setup(18,GPIO.OUT)
            GPIO.output(18,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(18,GPIO.LOW)
            score+=1

# Provide final score
    print('\nQuiz completed!')
    print(f'You get {score}/{len(questions)} questions correct.')

# Run the quiz function
quiz()
