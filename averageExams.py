"""-------------------------------------------------------------------------------------------------------------------------------------
Name: Sean Casaus
File: averageExams.py
Specification: Part 1: User inputs 3 exams, and the program prints the average of the exams
                    Part 2: User inputs a first, middle and last name, and the program prints the initials
                    Part 3: the user inputs any time in seconds and the program prints in format hours:minutes:seconds
                    For: To practice skills in python
Time Spent: 1 hour-------------------------------------------------------------------------------------------------------------------"""
import math
import decimal

#Calculates and prints the Average of Three Exams inputed by user
print "Task One: Calculate the Average of Three Exams"
print "(Note: For most accurate results enter exam scores to atleast two decimal places)"
score1 = input("Please input the first exam score: ")
score2 = input("Please input the second exam score: ")
score3 = input("Please input the third exam score: ")

average = (score1 + score2 + score3) / 3
average = str('%.5g'%(average))
print "The average of the three exams is: " + average
print " "

#Takes user input for first name, middle name, and last name, finds the initials
print "Task Two: Find the initials of a full name"
firstName = raw_input ("Please input first name: ")
middleName = raw_input ("Please input the middle name: ")
lastName = raw_input ("Please input the last name: ")

initialOne = firstName[0]
initialTwo = middleName[0]
initialThree = lastName[0]
print "Your initals are: " + initialOne + initialTwo + initialThree
print " "

#Takes user input for seconds, and prints out in format hours:minutes:seconds
print "Task Three: Convert Seconds to H:M:S format"
secondsInputed = input ("Please input total seconds: ")
if secondsInputed >= 3600:
    H = math.floor(secondsInputed / 3600)
    M = math.floor((secondsInputed / 60) - (H * 60))
    S = secondsInputed - (H * 3600) - (M * 60)

elif secondsInputed >= 60 and secondsInputed < 3600:
    H = 0
    M = math.floor(secondsInputed / 60)
    S = secondsInputed - (M * 60)

else:
    H = 0
    M = 0
    S = secondsInputed
    
H = str(int(H))
M = str(int(M))
S = str(int(S))

print "The total time (Hours:Minutes:Seconds) is: " + H + ":" + M + ":" + S
print " "

raw_input("Press<enter>")
