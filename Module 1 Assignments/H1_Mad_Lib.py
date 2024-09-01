# Homework 1: Mad Lib
# Program By: Landon Scott
# File Name: H1_Mad_Lib.py
# Function: This program will create a Mad Lib from user input

# Variables
noun1 = ""
noun2 = ""
properNoun1 = ""
properNoun2 = ""
verb1 = "" # Must be past tense
verb2 = "" # must be present tense
adverb1 = ""
adverb2 = ""
adjective1 = ""
adjective2 = ""

# Print the title
print("A Fun Coincidence")

print("")

# Give Instructions to the user

print("This is a Mad Lib, a prewritten \nchoose-your-own-adventure story that you write\nby inputting words of your choice.") 
print("We will ask for a few diffrent words\nand we will do the rest.")

print("")

# Get Variable Values

noun1 = input("Input a noun: ")
noun2 = input("Input another noun: ")

print("")

properNoun1 = input("Input a proper noun: ")
properNoun2 = input("Input another proper noun: ")

print("")

verb1 = input("Input a past-tense verb: ")
verb2 = input("Input a present-tense verb:")

print("")

adverb1 = input("Input an adverb: ")
adverb2 = input("Input another adverb: ")

print("")

adjective1 = input("Input an adjective: ")
adjective2 = input("Input another adjective: ")

print("")

# Print out the story, each print statement is a different like
print("One day long ago, there was a ", noun1, " named ", properNoun1, ".", sep='')
print(properNoun1, " was a ", adjective1, " ", noun1, ".", sep='')
print("Since ", properNoun1, " was ", adjective1, ", ", properNoun1, " decided to visit the ", noun2, ".", sep='')
print(properNoun1, " ",adverb1, " ",verb1, " to the ", noun2, ".", sep='')
print("When ", properNoun1, " got to the ", noun2, ", ", properNoun1, " was ", adjective2, " to see another ", noun1, " named ", properNoun2, ".", sep='')
print("In the end, ", properNoun1, " decided to ", verb2, " with ", properNoun2, ".", sep='')
print("\nThe End")