# Homework 5: Numeric Processing
# Program By: Landon Scott
# File Name: H5_Num_Process.py
# Function: This program reads and writes to files



# Change this to your specific relative path
filePath = "Random.txt"



def readFile(directory, list):
    '''Reads the file from directory and outputs it to the inputted list variable '''
    # Check if the file exists
    try:
        # Open the random file in read mode
        file = open(directory, "r")
    except FileNotFoundError:
        print("No file was found, exiting program...")
        exit(1)
        
    for line in file:
        list.append(int(line))
    
    # Close the File
    file.close()
    return

def numberFun(list, newFileName):
    '''First prints the numbers in numbers, then tells the user the cool facts and writes those to the file'''

    quantity = 0
    numberSum = 0
    
    # Prints out the numbers and gets the details
    for num in list:
        print(num)
        
        numberSum += num
        quantity += 1
        
    print("There are " + str(quantity) + " numbers within the file")
    print("The sum of all numbers in the file is " + str(numberSum))
    print("The average of all numbers in the file is " + str(numberSum / quantity))
    
    # Open the new file in write mode
    file = open(newFileName, "w")
    
    # Writes the statments to the file
    file.write("There are " + str(quantity) + " numbers within the file\n")
    file.write("The sum of all numbers in the file is " + str(numberSum) + "\n")
    file.write("The average of all numbers in the file is " + str(numberSum / quantity) + "\n")
    
    # Closes the file
    file.close()
    
    print("The results have been written to file " + str(newFileName)) 
    return


# --- Execution ---
numbers = []
readFile(filePath, numbers)
numberFun(numbers, "Results.txt")
