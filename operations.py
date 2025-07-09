import read
import write

def displayLandList():

    # Docstring for specificatio of the function
    """
    Function to display Land Data List
    """

    # Call function landData() to store the land details of "LandListInfo" text file
    landData = read.landData()

     # Displaying Land List Data
    print("=====================================================================================================")

    print("KITTA NO       CITY                LAND-FACED          ANNA           PRICE          AVAILABILITY")

    print("=====================================================================================================")

    # Displaying landData
    for line in landData:

        # Print each land's details formatted neatly
        print(line[0] + " " * (15 - len(line[0])) + line[1]+" " * (20 - len(line[1])) + line[2] + " " * (20 - len(line[2])) + line[3] + " " * (15 - len(line[3])) +line[4] + " " * (15 - len(line[4])) + line[5])
        
        print("-----------------------------------------------------------------------------------------------------")

    # Skipping a line
    print("\n")

def customerInfo():
   
    # Docstring for specification of the function
    """
    Function that ask customer their basic information
    Name, Address, PhoneNumber

    Returns:
        name(str): Name of the Customer
        address(str): Address of the Customer
        phoneNumber (str): Phone Number of the Customer
    """
    # Asking the user to input their name and validate it using the userValidation function
    name = userValidation(input("Please enter your name :"), "name")

    # Asking the user to input their address and validate it using the userValidation function
    address = userValidation(input("Please enter your address :"), "address")

    # Asking the user to input their name and validate it using the userValidation function
    phoneNumber = userValidation(input("Please enter your phone number :"), "phoneNumber")

    # Returning the validated name, address, and phone number.
    return name, address, phoneNumber

def userValidation(userInput, inputType):
    
    # Docstring for function specifications
    """
    Function to validate user's basic information
    Name, Address, PhoneNumber

    Arguments:
        userInput(input): input prompt from customerinfo(function)
        inputType(str): Specifying what type of input is to be performed

    Return:
        userInput(str): Validated user input         
    """

    # Flag to control User Input Validation
    validInput = True

    # Loop for User Input Validation
    while validInput:

        if (userInput.strip()): # Check if userInput is not empty 
            
            # Name Validation 
            if(inputType == "name"):
            
                if (userInput.replace(" ", "").isalpha()): # Check if name only contains alphabet 
            
                    validInput = False # Set flag to false to exit loop  
            
                else:
            
                    print("INVALID NAME \nNAME MUST ONLY CONTAIN ALPHABETS.") # Display message for invalid name

            # Phone Number Validation
            elif(inputType == "phoneNumber"):

                if(userInput.isdigit() and len(userInput) == 10): # Check if phone number contains only number and is 10 digits
                
                    validInput = False  # Set flag to false to exit loop
                
                else:
                
                    print("INVALID PHONE NUMBER \nPHONE NUMBER SHOULD BE A 10-DIGIT NUMBER") # Display message for invalid phone number
            
            # Address Validation
            elif(inputType == "address"):
            
                validInput = False # Set flag to false to exit loop

        else:

            print("!!!Empty Field Found!!!") # Display message for empty user input


        # if user input is not valid ask user to enter their input again
        if validInput: 

            userInput = input("Please enter your " + inputType + " again :")

    return userInput # Return valid input

def kittaNumAndMonthValidation(message, inputType):
    
    # Docstring for function specifications
    """
    Function to validate Kitta No, Rent Month and Return Month
    To check if they are valid input and a non negative 
    For Kitta No also call another function to check availability Status

    Arguments:
        message(str): prompt to specifiy user input which is "Kitta No" or "Rent Month" or "Return Month"
        inputType(str): specifying what type of user input "Kitta No" or "Rent Month" or "Return Month"
    
    Returns:
        userInput(str): Validated user entered "Kitta No" or "Rent Month" or "Return Month"
        landinfo(list): Land Details of the validated Kitta No
    """

    # Intially assigning unavailability as none
    availability = None

    # Set Flag to control User Input Validation
    validInput = True

    # Loop for Kitta No or Month Validation
    while validInput:

        try:

            # Variable to store "Kitta No" or "Rent Month" or "Return Month" via user input
            userInput = int(input(message))
            
            # Check if the input is a positive integer
            if (userInput > 0):
                
                # If the input type is "Kitta No Return"
                if(inputType == "Kitta No Return"):
                    
                    # Call function to check kitta staus is unavailability and if not available also the land data of the kitta No
                    availability, landInfo = kittaReturning(userInput)

                    # If kitta status is not available, set flag to False to exit the loop
                    if availability:
        
                        validInput = False

                # If the input type is "Kitta No Rent"
                elif(inputType == "Kitta No Rent"):

                    # Call function to check kitta staus is Availability and if available also the land data of the kitta No
                    availability, landInfo = kittaRenting(userInput)

                    # If kitta status is Available, set flag to False to exit the loop
                    if availability:
        
                        validInput = False

                # If the input type is not "Kitta No" (i.e., "Rent Month" or "Return Month")
                else:

                    validInput = False

            # If the input is 0
            elif (userInput == 0):

                print("!!! ", inputType.upper(), " SHOULD BE GREATER THAN ZERO!!!")

            # If the input is negative
            else:

                print("!!! ", inputType.upper(), " MUST BE NON-NEGATIVE!!!")

        # If a non-integer value is entered  
        except ValueError:

            print("!!!Please enter valid Integer for ", inputType, " !!!")   

    # Return the validated input and associated land information if kitta is unavailable; otherwise, return None
    return userInput, landInfo if availability else None

def kittaRenting(kittaNum):

    """
    Function to check the availability of the Renting lands

    Arguments:
        kittaNum(int): User provided kitta number of the land to be rented

    Returns:
        Boolean: True or false as per the validation of Kitta number
        updatingLandList(list): Land Details of the validated kitta number
    """

    # Calling landData() function from read module to store land list details
    landData = read.landData()

    # List to store the details of the land whose kitta number is validated
    updatingLandList = []

    # Set Flag to cheecking entered kitta no is true
    validKitta = True

    # Loop for handling kitta number validation
    while validKitta:

        # Variable to check if the Kitta number is found or not:
        kittaFound = False

        # Loop through each land's information to find a match with the entered kitta number
        for landInfo in landData:    

            # Check if the entered kitta number matches with any land's kitta number in list
            if (int(landInfo[0]) == kittaNum):

                kittaFound = True
        
                # Checking if the matched kitta no is available for rent
                if (landInfo[-1].lower() == "available"):
                
                    validKitta = False # Set flag to false to exit the loops

                   # Storing details of returned land to the List
                    updatingLandList.extend([landInfo[0], landInfo[1], landInfo[2], landInfo[3], landInfo[4], landInfo[5]])

                    # Break the program when desired output is obtained
                    break
        
                # Displaying message if Kitta no is not available 
                else:
                    
                    print("!!!Land with kitta no: ", kittaNum, " is not available!!! \n!!!Please look for land with Available status!!!")

                    # Returning False and none when kitta number is not available
                    return False, None

        # Displaying message if provided kitta number does not exist   
        if not kittaFound: 
            
            print("!!! Kitta number ", kittaNum, " not found !!! \n!!! Please enter a valid kitta number !!!") # Displaying message when kitta number is not available
 
            # Returning False and None when invalid kitta number is entered
            return False, None
    
    # Returning True and Land Details of Validated Kitta number 
    return True, updatingLandList

def kittaReturning(kittaNum):

    """
    Function to check the Unavailability of the Returning lands
    Args:
        kittaNum(int): User provided kitta number of the land to be returned

    Returns:
        Boolean: True or false as per the validation of Kitta number
        updatingLandList(list): Land Details of the validated kitta number
    """
    
    # Calling landData() function from read module to store land list details
    landData = read.landData()

    # List to store details of each land
    updatingLandList = []

    # Set Flag to cheecking entered kitta no is true
    validKitta = True

    # Loop for handling kitta number validation
    while validKitta:

        # Variable to check if the Kitta number is found or not:
        kittaFound = False

        # Loop through each land's information to find a match with the entered kitta number
        for landInfo in landData:    

            # Check if the entered kitta number matches with any land's kitta number in list
            if (int(landInfo[0]) == kittaNum):

                kittaFound = True #Set True when user entered kita is found
        
                # Checking if the matched kitta no is available for rent
                if (landInfo[-1].lower() == "not available"):
                
                    validKitta = False # Set flag to false to exit the loops

                   # Storing details of returned land to the List
                    updatingLandList.extend([landInfo[0], landInfo[1], landInfo[2], landInfo[3], landInfo[4], landInfo[5]])

                    # Break the program when desired output is obtained
                    break
        
                # Displaying message if Kitta no is not available 
                else:
                    
                    print("!!!Land with kitta no: ", kittaNum, " is available!!! \n!!!Please look for land with Not Available status!!!")

                    # Returning False and None when invalid kitta number is not available
                    return False, None

        # Displaying message if provided kitta number does not exist   
        if not kittaFound: 
            
            print("!!! Kitta number ", kittaNum, " not found !!! \n!!! Please enter a valid kitta number !!!")

            # Returning False and None when invalid kitta number is entered
            return False, None
    
    # Returning True and Land Details of Validated Kitta number 
    return True, updatingLandList

def rentLand():
    """
    Function to rent land

    """

    # List to store rented land by user 
    rentedLandList = []

    # Design 
    print("\n\n\t\t======================================")
    print("\t\t\tLand Renting Interface")
    print("\t\t======================================\n\n")


    # Calling function to ask Customer Information and store it in a list
    customerInformation = customerInfo()
        
    print("\n") # Skipping a line


    # Flag to control the loop for renting lands
    keepRunning = True

    # Loop for renting lands
    while keepRunning:

        # Calling function to display details of Land
        displayLandList()

        print("\n")  # Skipping a line

        # List to store details of land rented by the user one at a time
        updatingLandList = []


        # Calling function to Ask Kitta Number and store it in a variable
        kittaNum, updatingLandList = kittaNumAndMonthValidation("Please enter kitta number of the land for renting :", "Kitta No Rent")


        # Calling function to Ask Rent Month and store it in a variable
        rentMonth, extra = kittaNumAndMonthValidation("How many months would you like to rent the land? Please enter the duration: :", "Rent Month")

        del(extra) # Deleting extra as it is not needed in the program

        # Displaying message that land has been rented
        print("Land is rented successfully")


        # Updating the Land Satus to "Not Available" for Rented Lands
        write.updateLandStatus(kittaNum, "Rent")


        # Adding rent month and returnMonth to the updatingLandList
        updatingLandList.append(rentMonth)


        # Main list to store all the returned lands
        rentedLandList.append(updatingLandList)


        # Ask the user if they want to rent more lands
        rentMoreLand = input("Do you want to rent more lands? Please enter yes(y) / No(n):")
        

        # Check if the user wants to rent more lands, if not, exit the loop
        if(rentMoreLand.lower() != "y"):
      
            keepRunning = False # Set flag to false to exit loop


    # Generate a rental invoice using the rentInvoice function from the write module,
    rentBill = write.rentInvoice(customerInformation, rentedLandList)

    # Print the generated invoice.
    print(rentBill)   

def returnLand():
    """
    Function to Return land
    """

    # Print heading for land returning interface
    print("\n\n\t\t======================================")
    print("\t\t\tLand Returning Interface")
    print("\t\t======================================\n\n")

    # List to store details of returned land 
    returnedLandList = []

   # Calling functio to ask Customer Information and store it in a list
    customerInformation = customerInfo()

    print("\n") # Skipping a line


    # Flag to control loop for returning lands
    keepRunning = True

    # Loop for returning lands
    while keepRunning:

        # Calling Function to display details of all Lands
        displayLandList()

        print("\n")  # Skipping a line

        # List to upadte the status to "Available" in landData 
        updatingLandList = []

        # Calling function to Ask Kitta Number and store it in a variable
        kittaNum, updatingLandList = kittaNumAndMonthValidation("Please enter kitta number of the land for returning :", "Kitta No Return")


        # Calling function to Ask Rent Month and store it in a variable
        rentMonth, extra = kittaNumAndMonthValidation("How many months did you rent the land? Please enter the duration :", "Rent Month")


        # Calling function to Ask Return Month and store it in a variable
        returnMonth, extra = kittaNumAndMonthValidation("After how many months did you return the land? Please enter the duration: ", "Return Month") 

        del(extra) # Deleting it since it has no use

        # Displaying message that land has been returned 
        print("Land Returned Succesfully.")

        
        # Updating the Land Satus to "Available" for Returned Lands
        write.updateLandStatus(kittaNum, "Return")


        # Adding rent month and returnMonth to the updatingLandList
        updatingLandList.extend([rentMonth, returnMonth])


        # Main list to store all the returned lands
        returnedLandList.append(updatingLandList)


        # Asking user if they want to Return more lands
        returnMoreLands = input("Do you want to return more lands? Please enter yes(y) / No(n):")


        # Check user if they want to return more lands
        if(returnMoreLands.lower() != "y"):
      
            keepRunning = False # Set flag to false to exit loop


    # Generate a Return invoice using the rentInvoice function from the write module,   
    returnBill = write.returnInvoice(customerInformation, returnedLandList)
    
    # Print the Return Invoice
    print(returnBill)  
