# Homework 3: User Login
# Program By: Landon Scott
# File Name: H3_Login.py
# Function: This program will authenticate user access

# Accounts dictonary, in the form of 
# username: [password, adminBooln, userID]
# (UserID was an afterthought, not changing it)
accounts = {
    'Mikey': ['pizzatime', 0, 1],
    'Donny': ['halfshell', 0, 2],
    'Ralph': ['shredhead', 0, 3],
    'Leo': ['cowabunga', 1, 4]
}
# If the username was found
usernameFound = False

#print(accounts['Mikey'][0])
#accounts['newvalue'] = ['password', 0]

# Ask if the user has an accountt
print("Hello!\nDo you have an account? Y/N")
hasAccount = input('>')

# If the user doesn't have an account
if hasAccount.lower() == "n":
    print("Please enter your desired username:")
    newUsername = input('>')
    
    print("Please enter your desired password:")
    newPassword = input('>')
    
    # Add their account to the dictonary
    accounts[newUsername] = [newPassword, 0]
    
    print("Thank you, your information has been stored.")

# If the user has an account
elif hasAccount.lower() == "y":
    print("Please enter your username:")
    givenUsername = input('>')
    
    print("Please enter your password:")
    givenPassword = input('>')
    
    # Find if their username matches
    for username in accounts:
        if username == givenUsername:
            usernameFound = True
    
    # Find if their password matches
    if usernameFound and givenPassword == accounts[givenUsername][0]:
        print("\nThank you, your information was found!")
    else:
        print("\nSorry, your information was NOT found!")
        quit()
    
print("\nWelcome to the Secret Sewer System!")

# If the found user was an admin, print all the user's info
accountRoles = ['standard', 'admin']
if usernameFound and accounts[givenUsername][1]:
    
    print()
    print('UserID\t\tUsername\t\tPassword\t\tRole')
    for index in accounts:
        # Its beautiful
        print(accounts[index][2], '\t\t', index, '\t\t\t', accounts[index][0], '\t\t', accountRoles[accounts[index][1]])