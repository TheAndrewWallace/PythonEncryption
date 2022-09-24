#The last digit of student ID is: 2



#########################################################################################################################################################################################################################################################################################################################################################

#These are variables that have been decleared for the global code.
quit = False							#This will determine if the loop will continue. Starts as False so that the main code contained within the while loop will run.
quitconfirm = str("Error")				#Use to determine if the user wants to confirm that they have quit.
option = 0								#Changes to which option the user enters. If it is changed to a valid option it will satisfy the requirements of a particular if or elif statement.
validoption = False						#Confirms if the option enters was valid. If it stays as False then an error message will print. Will be changed to True if it is valid. Starts as False so it has to be changed if it is valid.
personnumber = str("000000")			#This will obtain the personnumber as a string. If it was an integer then if a number entered has zeros at the start they will disappear.
separate = False						#Initialised as False but after the first time passing through the while loop before returning to main menu it will be set True.
personnumberaccepted = False			#If the person number is accepted then this is set to True.
correct = True							#This is used to tell if the message input is valid and able to be encrypted.
number1 = None							#Stores the first number of the person number.
number2 = None							#Stores the second number of the person number.
number3 = None							#Stores the thrid number of the person number.
number4 = None							#Stores the fourth number of the person number.
number5 = None							#Stores the fifth number of the person number.
number6 = None							#Stores the sixth number of the person number.
message = None							#Stores the message that has been entered to be either encrypted or decrypted.

#Character List - This contains all of the valid characters that are valid and can be used in the encryption.
characterlist = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "."]

#########################################################################################################################################################################################################################################################################################################################################################



#################################################################################################################################################
#Function - verify																																#
#Description - The verify function is used to check that the message input into the program to be encrypted is valid and does not contain		#
#any characters that are not in the character list. If it does then it will output a correct = False which will prevent							#
#the prograqm from using the encrypt function.																									#
#Output variables - It will return correct as True if the message does not contain any invalid characters.										#
#					It will return correct as False is the message does contain any invalid characters.											#
#################################################################################################################################################
def verify(y):
	#local variables used in the function
	global correct					#Set to global so that it will change the variable outside of the loop
	correct = True					#Assumes it is True. It will be changed to False if the message contains invalid characters.
	limittest = len(y)				#This is changed to the length of characters in the message and tells the function how many characters to check.
	charactertest = 0				#Refers to the current character being tested. Will increase by 1 after loop.
	lettertest = None				#The character that is being tested is assigned to this variable.
	
	
	#This will try to run the following code.
	try:
		
		#While the charactertest (which increased every time is passes through the loop) is smaller than the limittest it will run the code. Conditions will no longer be valid after all characters have been checked.
		#A while loop has been used because this needs to run repeatedly until all the characters have been tested.
		while (charactertest < limittest):
		
			#This gets the character that it is testing and attempts to assign lettertest to its place in the list. If it is not there it will cause an error.
			lettertest = str(y[charactertest])
			lettertest = (int(characterlist.index(lettertest)))
			
			#If it is there then charactertest will increase by 1 and the loop will move onto the next character to be tested.
			charactertest = (charactertest + 1)
	
	#This code will run if there is a value error within the try section.
	except ValueError:
		#If the code has any errors then we know that the message is invalid. This will change the correct variable to False and print a list of characters that the user is not allowed to use.
		correct = False
		print ("Error: Do not include characters such as ! £ $ % ^ & * ( ) _ - + = { } [ ] ¬ ` : ; @ ' ~ # < , > ? / | ")
	
	
	
	
	
	
	
#################################################################################################################################################
#Function - encryption																															#
#Description - This function is used to encrypt the message that the user inputs.																#
#Output variables - It will return correct as True if the message does not contain any invalid characters.										#
#					It will return correct as False is the message does contain any invalid characters.											#
#################################################################################################################################################
def encryption(x):
	#local variables used in the function
	limit = len(x)									#The limit is set to the length of the message.
	idcharacter = 1									#This will determine which character in the person number is used for the math to encrypt the message.
	character = 0									#This will determine which character of the message is currently being encrypted.
	encryptedmessage = ("Encrypted message: ")		#Sets encrypted message to "Encrypted message: ". Encrypted characters will be added to this string to be printed out.
	letter = None									#The character will be assigned to this and then it will be used for the encryption process.



	#This if function is used to check if it should run the encrypt process. If option is set to 2 then they user must have entered the encrypt option.
	#An if function is used because it only needs to run once and does not rely on any others not passing first.
	if (option == 2):
	
		encryptedmessage = ("Encrypted message: ")			#Changes the string to this so that it will appear before the message.
		
		#A while loop has been used because the loop needs to repeat until it has encrypted all of the characters. It will stop once the character is higher than the limit.
		while (character < limit):
			
			#This will find the number of the character in the list and adds 1 to it because arrays start at zero.
			letter = str(x[character])
			letter = (int(characterlist.index(letter)) + 1)
			
			#An if has been used to check if the current character part of the person number that is being used is the first. If so, it will use that number in the math to encrypt the character in the message.
			#An if condition has been used because it does not rely on any other conditions not passing to be used.
			if (idcharacter == 1):
				#This takes the number assigned to letter and adds the first number of the person number.
				letter = (letter + number1)
				
			#An elif has been used to check if the current character part of the person number that is being used is the second. If so, it will use that number in the math to encrypt the character in the message.
			#An elif has been chosen because if one of the possibilities have already passed then it will not need to be used this time.
			elif (idcharacter == 2):
				#This takes the number assigned to letter and adds the second number of the person number.
				letter = (letter + number2)
				
			#An elif has been used to check if the current character part of the person number that is being used is the third. If so, it will use that number in the math to encrypt the character in the message.
			#An elif has been chosen because if one of the possibilities have already passed then it will not need to be used this time.
			elif (idcharacter == 3):
				#This takes the number assigned to letter and adds the second number of the person number.
				letter = (letter + (number2 * number3))
				
			#An elif has been used to check if the current character part of the person number that is being used is the fourth. If so, it will use that number in the math to encrypt the character in the message.
			#An elif has been chosen because if one of the possibilities have already passed then it will not need to be used this time.
			elif (idcharacter == 4):
				#This takes the number assigned to letter and adds the second number of the person number.			
				letter = (letter - number4)

			#An elif has been used to check if the current character part of the person number that is being used is the fifth. If so, it will use that number in the math to encrypt the character in the message.
			#An elif has been chosen because if one of the possibilities have already passed then it will not need to be used this time.
			elif (idcharacter == 5):
					#This takes the number assigned to letter and adds the second number of the person number.		
				letter = (letter - number5)
				
			#An elif has been used to check if the current character part of the person number that is being used is the sixth. If so, it will use that number in the math to encrypt the character in the message.
			#An elif has been chosen because if one of the possibilities have already passed then it will not need to be used this time.
			elif (idcharacter == 6):
					#This takes the number assigned to letter and adds the second number of the person number.		
				letter = (letter - number6)	
				
			#If the number is lower than 1 then it will be out of the list limits.
			if (letter < 1):
				#This is used to create a round robin to turn a number that would be out of the limits back into an acceptable number by adding 64.
				#An if statement has been used because it does not rel any any previous if or elif statements.
				letter = (letter + 64)
				
			#If the number is higher than 64 then it will be out of the list limits. This implementts a round robin to stop that from happening.
			#An elif condition has been used because it will not need to run if the previous if statement has already passed.
			elif (letter > 64):
				#This is used to create a round robin to turn a number that would be out of the limits back into an acceptable number by subtracting 64.
				letter = (letter - 64)
				
			###############	
				
			#This will subtract 1 from letter because arrays start at zero and then find what character is in that place in the list
			letter = (letter - 1)
			letter = str(characterlist[letter])
			
			#This adds 1 to both the character and the idcharacter so that it will change which letter it is encrypting and what part of the person number it is using to the next one.
			character = (character + 1)
			idcharacter = (idcharacter + 1)
			
			#Once the character that is being used to encrypt the person number has reached 7 this will run.
			#An if statement has been used because it does not depend on any other previous if or elifs passing.
			if (idcharacter == 7):
			#This will reset it to 1 as there is no 7th number for it to use to encrypt.
				idcharacter = 1
				
			#This will add the enrypted character to the full message every time a character is encrypted.
			encryptedmessage = encryptedmessage + letter
			
		#This will print the encrypted message in full once the while loop has completed.
		print(encryptedmessage)
		
		
	#This elif function is used to check if it should run the decrypt process. If option is set to 3 then they user must have entered the decrypt option.
	#An elif function is used because it only needs to run once and does not need to run if the if statement has run.
	elif (option == 3):
	
		encryptedmessage = ("Decrypted message: ")			#Changes the string to this so that it will appear before the message.
		
		#A while loop has been used because the loop needs to repeat until it has decrypted all of the characters. It will stop once the character is higher than the limit.
		while (character < limit):
			
			#This will find the number of the character in the list and adds 1 to it because arrays start at zero.
			letter = str(x[character])
			letter = (int(characterlist.index(letter)) + 1)			
			
			#An if has been used to check if the current character part of the person number that is being used is the first. If so, it will use that number in the math to decrypt the character in the message.
			#An if condition has been used because it does not rely on any other conditions not passing to be used.
			if (idcharacter == 1):
				letter = (letter - number1)

			#An elif has been used to check if the current character part of the person number that is being used is the second. If so, it will use that number in the math to decrypt the character in the message.
			#An elif has been chosen because if one of the possibilities have already passed then it will not need to be used this time.
			elif (idcharacter == 2):
				letter = (letter - number2)
				
			#An elif has been used to check if the current character part of the person number that is being used is the third. If so, it will use that number in the math to decrypt the character in the message.
			#An elif has been chosen because if one of the possibilities have already passed then it will not need to be used this time.
			elif (idcharacter == 3):
				letter = (letter - (number2 * number3))
				
			#An elif has been used to check if the current character part of the person number that is being used is the fourth. If so, it will use that number in the math to decrypt the character in the message.
			#An elif has been chosen because if one of the possibilities have already passed then it will not need to be used this time.
			elif (idcharacter == 4):
				letter = (letter + number4)

			#An elif has been used to check if the current character part of the person number that is being used is the fifth. If so, it will use that number in the math to decrypt the character in the message.
			#An elif has been chosen because if one of the possibilities have already passed then it will not need to be used this time.
			elif (idcharacter == 5):
				letter = (letter + number5)

			#An elif has been used to check if the current character part of the person number that is being used is the third. If so, it will use that number in the math to decrypt the character in the message.
			#An elif has been chosen because if one of the possibilities have already passed then it will not need to be used this time.
			elif (idcharacter == 6):
				letter = (letter + number6)

			#If the number is lower than 1 then it will be out of the list limits.
			if (letter < 1):
				#This is used to create a round robin to turn a number that would be out of the limits back into an acceptable number by adding 64.
				#An if condition has been used because it does not rel any any previous if or elif statements.
				letter = (letter + 64)
				
			#If the number is higher than 64 then it will be out of the list limits. This implementts a round robin to stop that from happening.
			#An elif condition has been used because it will not need to run if the previous if statement has already passed.
			elif (letter > 64):
				#This is used to create a round robin to turn a number that would be out of the limits back into an acceptable number by subtracting 64.
				letter = (letter - 64)
				
				#This will subtract 1 from letter because arrays start at zero and then find what character is in that place in the list
			letter = (letter - 1)
			letter = str(characterlist[letter])
			
			#This adds 1 to both the character and the idcharacter so that it will change which letter it is encrypting and what part of the person number it is using to the next one.
			character = (character + 1)
			idcharacter = (idcharacter + 1)
			
			#Once the character that is being used to encrypt the person number has reached 7 this will run.
			#An if statement has been used because it does not depend on any other previous if or elifs passing.
			if (idcharacter == 7):
				#This will reset it to 1 as there is no 7th number for it to use to encrypt.
				idcharacter = 1
				
			#This will add the enrypted character to the full message every time a character is encrypted.
			encryptedmessage = encryptedmessage + letter
			
		#This will print the encrypted message in full once the while loop has completed.
		print(encryptedmessage)
		
		
		
		
		
		
		
#########################################
#This is the main block of code.		#
#It is all contained within a			#
#while loop					.			#
#########################################
		
#The main block of code is contained within the while loop. While used because it will need to repeat until the user quits which will turn quit to True and stops the loop.
while (not quit):
	
	#If condition used because it does not rely on any others not yet passing. Will pass if variable does not equal 0.
	if (option != 0):
		#Sets option to 0
		option = 0
	
	#If condition used because it does not rely on any others not yet passing. Will pass if valid option does not equal False.
	if (validoption != False):
		#sets validoption to False
		validoption = False
	
	#The first time the loop is passed this should not be passed but at the end of the loop seperate will be set to True so it will pass every time after.
	#If used because it does not rely on previous conditions passing or not.
	if (separate == True):
		#This will then print a blank line before the menu so that it appears organized.
		print ("\n")
	
	#Will print the menu with list of options. Will print options on different lines.
	print ("Encryption and Decryption Program Menu.\nPlease select an option.\n1. Set Person Number\n2. Encrypt a message\n3. Decrypt a message\n4. Quit")
	
	#Try used to test for Value Errors
	try:
		#Gets integer from user and assigns it to option.
		option = int(input("Enter an integer between and inclusive of 1 and 4: "))
	#Passes if there is value error. This will also mean that the option was not valid
	except ValueError:
		#Validoption is set to False. Will cause an error message to be output to user.
		validoption = False
		
		
		
	#################################
	#Option 1: Set Person Number	#
	#################################
	#Passes if the user has input a 1 integer. Will begin the code used to enter a person number.
	#if used because it should always pass if conditions are met.
	if (option == 1):
	
		#Assumes personnumberaccepted variable is False and will change it if the input is valid.
		personnumberaccepted = False
		
		#Print instructions to the user
		print ("Enter a six digit number between and inclusive of 000000 and 999999.")
		
		#Gets the person number as a string. This will prevent it losing characters like it would if it was an integer.
		#This will cause the number "000000" to remain as that rather than it losing characters and turning into "0".
		#This will also cause any previous person number entered to be removed.
		personnumber = str(input("Enter a six digit student number: "))
		
		#Try used to test for Value Errors as a result of the numbers not being integers.
		try:
			#If condition passes if the length of the number entered is 6 character. if used because it should always pass if the conditions are met.
			if (len(personnumber) == 6):
				#This seperates the different characters of the person number and will assign each to a variable 
				number1 = int(personnumber[0])
				number2 = int(personnumber[1])
				number3 = int(personnumber[2])
				number4 = int(personnumber[3])
				number5 = int(personnumber[4])
				number6 = int(personnumber[5])
				
				#if condition will pass if all the characters are valid.
				#if used because it should always pass if the condition is passed.
				if ((0 <= number1 <= 9) and (0 <= number2 <= 9) and (0 <= number3 <= 9) and (0 <= number4 <= 9) and (0 <= number5 <= 9) and (0 <= number6 <= 9)):
					#Will set variable to True so that the encrypt and decrypt options will run. Also prevents  it printing error message. Then prints an accepted message and then the number that has been accepted.
					personnumberaccepted = True
					print ("Person Number Accepted: " + personnumber)
					
		#Will run if there is a value error.
		except ValueError:
			#Will set variable to False so that it will activate the error message.
			personnumberaccepted = False
			
		#If condition will pass if the number entered by user was not valid.
		#if condition used bcause it should always pass if the condition are met.
		if (personnumberaccepted == False):
			#Prints error message to the user.
			print ("Error: Invalid input. You have been returned to the menu. If you have previously entered a user number it has been removed.")
			
		#variable set to true to prevent an error message being printed near the end of the while loop
		validoption = True

	#################################
	#Option 2: Encrypt a message	#
	#################################
	#Passes if the user has input a 2 integer. Will begin the code used to encrypt a message
	#elif used because the condition should pass if conditions are met but if the previous condtion statement already has one that has passed then this one can not.
	elif (option == 2):
	
		#Will pass if the user has already entered a valid person number. if used because it should always pass if the conditions are met
		if (personnumberaccepted == True):
			#Gets message from user to be encrypted and stores it in variable.
			message = str(input("Enter message to be encrypted: "))
		
			#Runs the function to verify the message.
			verify(message)
		
			#If function verifys that the message does not contain any invalid characters then it then the condition is passed.
			if (correct == True):
				#Runs the function and encrypts the message
				encryption(message)
			
		else: #An else statement has been chosen because the only condition that matters in relation to if this should run is if the associated if statement has not run.
			#Prints an error message.
			print ("Error: You have not yet set a person number.")
		
		#Sets valid option to true to avoid it running through the error message at the end of the while loop.
		validoption = True
		
	#################################
	#Option 3: Decrypt a message	#
	#################################
	#Passes if the user has input a 3 integer. Will begin the code used to decrypt a message.
	#elif used because the condition should pass if conditions are met but if the previous condtion statement already has one that has passed then this one can not.
	elif (option == 3):
		
		#Will pass if the user has already entered a valid person number. if used because it should always pass if the conditions are met
		if (personnumberaccepted == True):
			#Gets message from user to be encrypted and stores it in variable.
			message = str(input("Enter message to be decrypted: "))
			
			#Runs the function to verify the message.
			verify(message)
			
			
			#If function verifys that the message does not contain any invalid characters then it then the condition is passed.
			if (correct == True):
				#Runs the function and decrypts the message.
				encryption(message)
		
		else: #An else statement has been chosen because the only condition that matters in relation to if this should run is if the associated if statement has not run.
			#Prints an error message.
			print ("Error: You have not yet set a person number.")
		
		#Sets valid option to true to avoid it running through the error message at the end of the while loop.
		validoption = True
		
	#################################
	#Option 4: Quit					#
	#################################
	#Passes if the user has input a 4 integer. Will begin the code used to quit the program.
	#elif used because the condition should pass if conditions are met but if the previous condtion statement already has one that has passed then this one can not.
	elif (option == 4):
		
		#Prints a message to the user to tell them to confirm if they want to quit.
		print ("Are you sure that you want to quit? (Options not case-sensitive)")
		
		#Gets a string from the use which is then assigned to variable.
		quitconfirm = str(input("Enter Y to quit or N to cancel: "))
			
		#If either "Y" or "y" is entered by user this condition should run. if condition used because it should always run if conditions are met.
		if (quitconfirm == str("Y") or (quitconfirm == str("y"))):
			#Sets quit to true which will prevent the while loop from repeating. This will allow the program to reach the end and quit.
			quit = True
		
		#If either "N" or "n" is entered then this condition should run. elif condtion used because it should always run if the conditions are met but if the previous if has already passed then this will not.
		elif (quitconfirm == str("N") or (quitconfirm == str("n"))):
			#Will print a message to tell user they have been returned to the menu.
			print("You have been returned to menu.")
		
		#This condition has been used because the code needs to run if neither of the previous if or elif conditions have been met. This would mean that the input was not valid.
		else:
			#Will now print an error message explaining how to use correctly before returning them to menu.
			print ("Error: Enter Y to quit or N to cancel (it is not case sensititve). You have been returned to the menu.")
		
		#Sets variable to True to avoid it running through the error message at the end of the while loop.
		validoption = True
		
	#If the user entered a valid integer then this should not run. Will pass if input was invalid.
	if (validoption == False):
		#Prints an error message to the user explaing how to use correctly before returning to menu.
		print ("Error Invalid input. Please enter an integer between and inclusive of 1 and 4")
		
	#If this is the first time that the while loop has been used then this will be False. If so it will be changed to True so that it will pass the conditions near the top of the while loop.
	if (separate == False):
		#Will change variable to True so that the condition at the start of the while loop will pass.
		separate = True