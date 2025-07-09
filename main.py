from operations import rentLand, returnLand

def main():

    ## Docstring for the specification of the function
    """
    Main function to control the Land Management System
    Has three options to choose from 
        1. Rent Land
        2. Return Land
        3. Exit System
    """
    
    # Design for user interface in terminal
    print("\n\n\t\t\t\t-------------------------------------")

    print("\t\t\t\t\tTECHNO PROPERTY NEPAL")
    
    print("\t\t\t\t\tDHAPAKHEL, LALITPUR")

    print("\t\t\t\t-------------------------------------")

    print("\n\nChoose the task you want to perform")
    
    print("======================================")

    # Flag to control loop for Land Rental System
    keepRunning = True

    # Loop for running Land Rental System
    while keepRunning:
    
        print("Type 1: Rent Land")
    
        print("Type 2: Return Land")
    
        print("Type 3: Exit System")
        
        # Flag to check valid choice as input by user
        validChoice = True

        # Loop for validation of Choice 
        while validChoice:
    
            try:
                
                # Variable to store choice via user input 
                userChoice = int(input("Choose the option: "))

                # value Validations
                if userChoice in [1,2,3]:
    
                    validChoice = False # Set flag to false to exit the loop
    
                else:
    
                    print("!!Enter valid input (Only 1, 2 or 3)!!!")  # Display message when invalid input is entered  
    
            except Exception as ValueError:
    
                print("!!!Please enter a numeric value!!!") # Display message when error occurs

        # To check when user choice is one
        if (userChoice == 1):
    
            rentLand() # Calling rentLand() Function for renting of the lands
        
        # To check when user choice is two
        elif (userChoice == 2):
    
            returnLand() # Calling returnLand() Funtion for returning of rented lands

        # To check when user choice is three
        elif (userChoice == 3):
            
            # Design to display message
            print(" -------------------------------------------")

            print("|                                           |")

            print("| THANK YOU FOR USING TECHNO PROPERTY NEPAL |")

            print("|          !!PLEASE VISIT AGAIN!!           |")

            print("|                                           |")

            print(" -------------------------------------------")
    
            keepRunning = False # Set Flag to false to exit the loop

# Calling main function to run the program
main() 
 