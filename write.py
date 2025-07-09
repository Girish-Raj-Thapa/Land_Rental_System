import datetime
import read

def updateLandStatus(kittaNum, updateType):
    """
    Function to upadte Availability Status of Land

    Args:
        kittaNum(int): Kitta number of the land to update status
        upadateType(str): Variable to check if to upadte to Available or not Available
    """

    landData = read.landData()    
    # Update the availability status of the returned lands to "Available" in the landData list
    for land in landData:

        if land[0] == str(kittaNum):

            if (updateType == "Rent"):

                land[-1] = "Not Available"
            
            elif(updateType == "Return"):
                
                land[-1] = "Available"

    # Rewriting the Text file --> LandListInfo
    file = open("LandInfoList.txt", "w")

    for land in landData:

        for i in range(len(land)):

            file.write(str(land[i]))

            if i < len(land) - 1:  # Add comma if it's not the last element

                file.write(",")

        file.write("\n")

    file.close()

def invoiceHeader(customerInformation, invoiceType):
    """
    Generate the common header for both rent and return invoices.

    Arguments:
    - customerInformation (list): List containing customer name, address, and phone number.
    - invoiceType (str): Type of invoice (e.g., "RENT" or "RETURN").
    
    Returns:
    - header (str): The generated header string.
    - invoiceId (str): The generated invoice ID.
    """
    
    header = ""
    
    # Storing current date and time when land is rented 
    currentDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Generate unique invoice ID using hour, minute, second, and microsecond
    invoiceId = str(datetime.datetime.now().hour) + str(datetime.datetime.now().minute) + str(datetime.datetime.now().second) + str(datetime.datetime.now().microsecond)

    header += "\n\n" + invoiceType + " INVOICE\n"
    
    header += "-------------------------------------------------------------------------------------------------------------\n"
    
    header +=  "\t" * 5 + "Techno Property Nepal\n" + "\t" * 5 + "Kamal Pokahari, Kathmandu\n\n\n"

    header += "Invoice ID: " + invoiceId + "\n"
    
    header += "Name of Customer: " + customerInformation[0] + "\n"
    
    header += "Address: " + customerInformation[1] + "\n"
    
    header += "Phone Number: " + customerInformation[2] + "\n"
    
    header += "Date and Time of Rent: " + currentDateTime + "\n\n"


    return header, invoiceId

def rentInvoice(customerInformation, rentedLandList):
    """
    Generate an invoice for the rented lands.
    
    Args:
    - customerInformation (list) : Customer details --> name, address, phone number
    - rentedLandList (list): List of rented lands, each containing details as a list. also has rentMonth

    Returns:
        rentInvoive(str): Rent Invoice for the rented lands by user
    """

    totalAmount = 0.0 # Declaring total amount as float type  

    # Calling invoiceHeader() function to make header part of invoice
    headerAndInvoiceId = invoiceHeader(customerInformation, "RENT")

    # Storing the header part in the variable
    rentInvoice = headerAndInvoiceId[0]

    # Storing the Invoice Id part in the Variable
    invoiceId = headerAndInvoiceId[1]    

    rentInvoice += "Details of Rented Land:\n"

    rentInvoice += "=============================================================================================================\nKITTA NO    CITY        LAND-FACED    ANNA    PRICE(P/M)     RENT_MONTHS          TOTAL\n=============================================================================================================\n"

    # For loop Rent Invoice
    for land in rentedLandList:
        
        amount = float((land[4])) * land[6] # Calculating amount for the rented land
        
        totalAmount += amount # adding amount of each land to the total amount 
        
        rentInvoice += str(land[0]) + " " * (12 - len(land[0])) # Kitta Number
        
        rentInvoice += land[1] + " " * (12 - len(land[1])) # City
        
        rentInvoice += land[2] + " " * (14 - len(land[2])) # Land Faced
        
        rentInvoice += str(land[3]) + " " * (8 - len(land[3])) # ANNA
        
        rentInvoice += str(land[4]) + " " * (15 - len(land[4])) # Price
        
        rentInvoice += str(land[6]) +  " " * (21 - len(str(land[6]))) # Duration of Rent
        
        rentInvoice += str(amount) + "\n"# Total Price

    rentInvoice += " " * 75 +"Grand Total = " +  str(totalAmount) + "\n\n\n" # Displaing total amount 
    
    rentInvoice += "-------------------------------------------------------------------------------------------------------------\n"

    # Creating Text file and Storing the Land Rented Invoice
    file = open(customerInformation[0] + "_" + invoiceId + ".txt", "w")
    
    # Writing the rentInvoice into the Text File
    file.write(rentInvoice)

    # Closing the text file
    file.close()

    # Returning the genreated Rent Invoice
    return rentInvoice

def returnInvoice(customerInformation, returnedLandList):
    """
    Generate Invoice for the rented lands returned

    Args:
    - customerInformation (list) : Customer details --> name, address, phone number
    - returnedLandList (list): List of Returned lands, each containing details as a list, also has rent month and return month

    Returns:
        returnInvoice(str): Return Invoice for the returned of the rented lands by user
    """

    totalAmount = 0.0 # Declaring total amount as float type   

    # Calling function to generate header part of Invoice and Invoice Id 
    headerAndInvoiceId = invoiceHeader(customerInformation, "RETURN")

    # Storing the header part in the variable
    returnInvoice = headerAndInvoiceId[0]

    # Storing the Invoice Id part in the Variable
    invoiceId = headerAndInvoiceId[1]    


    returnInvoice += "Details of Returned Land:\n"

    returnInvoice += "=================================================================================================================================\nKITTA NO    CITY        LAND-FACED    ANNA    PRICE(P/M)    RENT_MONTHS    RETURN_MONTHS    OVERDUE    FINE         TOTAL\n=================================================================================================================================\n"

    # For loop for Return Invoice
    for land in returnedLandList:

        returnInvoice += str(land[0]) + " " * (12 - len(land[0])) # Kitta Number

        returnInvoice += land[1] + " " * (12 - len(land[1])) # City

        returnInvoice += land[2] + " " * (14 - len(land[2])) # Land Faced

        returnInvoice += str(land[3]) + " " * (8 - len(land[3])) # ANNA

        returnInvoice += str(land[4]) + " " * (14 - len(land[4])) # Price

        returnInvoice += str(land[6]) +  " " * (15 - len(str(land[6]))) # Duration of Rent

        returnInvoice += str(land[7]) +  " " * (17 - len(str(land[7]))) # Duration of Return

        # Checking for imposing fine to the Customer --> 10% of Rented lands Price
        # When return month is more than the rent month
        if (land[7] > land[6]):

            overdueMonth = land[7] - land[6] # Calculating overdue month

            fine = overdueMonth * int(land[4]) + (overdueMonth * int(land[4])) * 0.1 # Calculation fine

            returnInvoice += str(overdueMonth) +  " " * (11 - len(str(overdueMonth)))# Overdue Month

            returnInvoice += str(fine) + " " * (13 - len(str(fine))) # fine Imposed

            amount = int(land[4]) * land[6] # Calaulating amount 

            totalAmount += amount # Adding amount of each land to total amount

            returnInvoice += str(amount + fine) + "\n"# Total Price    
        
        # when rent month and return month are equal
        elif (land[7] == land [6]):
            
            overdueMonth = 0 # Setting overdueMonth as zero

            fine = 0 # Settin fine as zero

            returnInvoice += "-" +  " " * (11 - len(str(overdueMonth))) # Overdue Month

            returnInvoice += "-" + " " * (13 - len(str(fine))) # fine Imposed

            amount = int(land[4]) * land[6] # Calculation the amount 

            totalAmount += amount # Adding the amount to the total amount

            returnInvoice += str(amount) + "\n"# Total Price
        
        # When return month is less than rent month
        elif (land[7] < land[6]):
            
            overdueMonth = 0 # Setting overdue month as zero

            fine = 0 # Setting fine as zero

            returnInvoice += "-" +  " " * (11 - len(str(overdueMonth))) # Overdue Month

            returnInvoice += "-" + " " * (13 - len(str(fine))) # fine Imposed

            amount = int(land[4]) * land[7] # Calclating Amount as per the Return Month

            totalAmount += amount # Adding amount to the total amount

            returnInvoice += str(amount) + "\n"# Total Price



    returnInvoice += " " * 100 +"Grand Total = " +  str(totalAmount) + "\n\n\n"

        
    returnInvoice += "---------------------------------------------------------------------------------------------------------------------------------\n"

    # Creating Text file and Storing the Land Returned Invoice
    file = open(customerInformation[0] + "_" + invoiceId+".txt", "w")

    # Writing the returnInvoice into the Text File
    file.write(returnInvoice)

    # Closing the text file
    file.close()

    # Returning the genreated Return Invoice
    return returnInvoice