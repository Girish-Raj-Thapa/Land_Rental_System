def landData():

    # Docstring for specification of function 
    """
    Read LandInfoList text file and stores it into a 2d list then print it in to dislay

    Returns:
        landData (list) : The 2d list generated from extracting the data from land list text file 
    """

    # Opening LandInfoList text file in reading mode
    file = open("LandInfoList.txt","r")

    # 2d list to store text file data
    landData = []

    # Converting the opened text file into 2d list 
    for line in file.readlines():
    
        line = line.replace("\n","").split(",")

        # Storint each line of text file into landData 2d list 
        landData.append(line)

    # Closing the landInfoList file
    file.close()

    # Returning the landData value extracted from the Text file
    return landData
