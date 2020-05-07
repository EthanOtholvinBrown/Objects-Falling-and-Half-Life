# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 10:33:23 2020

@author: Ethan
"""
import math
def main():
    userChoice = -1
    while (userChoice != 0):
        print("Welcome to assignment 2!")
        userChoice = int(input("Enter which part you would like to do[1 or 2, 0 to exit]: "))
        if(userChoice == 1):
            displayResults()
        elif(userChoice == 2):
            openFile = open("C:/Users/Ethan/Documents/Python Scripts/McMaster/Object Falling and Half Life/Example_File.txt")
            inputData = [[],[],[],[]]            
            for line in openFile:
                dataLine = line.split()
                dataLine[0] = float(dataLine[0])
                dataLine[1] = float(dataLine[1])
                dataLine[2] = float(dataLine[2])
                dataLine[3] = float(dataLine[3])
                inputData[0].append(dataLine[0])
                inputData[1].append(dataLine[1])
                inputData[2].append(dataLine[2])
                inputData[3].append(dataLine[3])
            userOption = 0
            while (userOption != 3):
                print("This program will analyze the provided data.")
                print("Option 1: Use a patient number to calculate half life"
                      ,"for their concentration. Averages reults if there is more than one.")
                print("Option 2: Uses 3 patient numbers to the same as option 1."
                      ,"Averages the three patients together and determines the two longest.")
                print("Option 3: Exit\n")
                userOption = int(input("Enter an option[1-3]: "))
                if(userOption == 1):                    
                    resultData = analyzeData(inputData,userOption)
                    print("Patient: ",resultData[0])
                    print("Number of entries: ",resultData[1])
                    print("Average: ",format(resultData[2],'.2f'),"\n")
                elif(userOption == 2):
                    result = analyzeData(inputData,userOption)
                    print("Patient: ",result[0])
                    print("Number of entries: ",result[1])
                    print("Average: ",format(result[2],'.2f'),"\n")
                    print("Patient: ",result[3])
                    print("Number of entries: ",result[4])
                    print("Average: ",format(result[5],'.2f'),"\n")
                    print("Patient: ",result[6])
                    print("Number of entries: ",result[7])
                    print("Average: ",format(result[8],'.2f'),"\n")
                    print("Total average of all the patients: ",format(result[9],'.2f'),"\n")
                    long = longest(result[0],result[3],result[6],result[2],result[5],result[8])
                    if (len(long) == 3):
                        print("They are all equal.")
                    else:
                        print("The longest averages are patient",long[0],"and patient",long[1],"\n")
                elif(userOption == 3):
                    print("Returning to main menu.")
                else:
                    print("That is not a valid entry.")
def analyzeData(data,optionNum):       
    if (optionNum == 1): 
        pNum = int(input("Enter a patient number [1-5]: "))
        results = halfLife(data,pNum)
        numofRecords = results[1]
        average = results[0]
        return pNum, numofRecords, average        
    elif (optionNum == 2):
        #take the patient numbers
        firstN = int(input("Enter the first patient number[1-5]: "))
        secondN = int(input("Enter the second patient number[1-5]: "))
        thirdN = int(input("Enter the third patient number[1-5]: "))
        #assign result data to patients
        firstP = halfLife(data,firstN)
        secondP = halfLife(data,secondN)
        thirdP = halfLife(data,thirdN)
        #assign average data 
        firstA = firstP[0]
        secondA = secondP[0]
        thirdA = thirdP[0]
        #assign counts
        firstC = firstP[1]
        secondC = secondP[1]
        thirdC = thirdP[1]
        totalAverage = (firstA + secondA + thirdA)/3
        return firstN,firstC,firstA,secondN,secondC,secondA,thirdN,thirdC,thirdA,totalAverage     
def longest(p1,p2,p3,a1,a2,a3):
    if(a1>a2 and a1>a3):
        if(a2>a3):
            return p1,p2
        else:
            return p1,p3
    elif(a2>a1 and a2>a3):
        if(a1>a3):
            return p2,p1
        else:
            return p2,p3
    elif(a3>a1 and a3>a2):
        if(a1>a2):
            return p3,p1
        else:
            return p3,p2
    else:
        return p1,p2,p3
def halfLife(pL, patientNum):
    sumofThalf = 0
    count = 0
    for num in range (0,len(pL[0])):                
        if (pL[0][num] == patientNum):
            tHalf = (-(pL[3][num]))*((math.log(2))/(math.log(pL[2][num]/pL[1][num])))                    
            sumofThalf = sumofThalf + tHalf
            count += 1                
    averageHalf = sumofThalf/count
    return averageHalf,count
def displayResults():
    results = calculateDistance()
    time = results[0]
    gravity = results[1]
    distance = results[2]
    print("Time: ",time)
    print("Gravity: ",gravity)
    print("Distance: ",format(distance,'.2f'))
def calculateDistance():
    calcValues = inputValues()
    calctime = calcValues[0]
    calcgravity = calcValues[1]
    resultD = math.pow((0.5*calcgravity*calctime),2)
    return calctime,calcgravity,resultD
def inputValues():
    enterT = float(input("Enter the fall time in seconds [0-45]: "))
    #if (enterT <0 or enterT >45):
    while(enterT < 0 or enterT > 45):
        print("Outside of range.")
        enterT = float(input("Enter the fall time in seconds [0-45]: "))               
    enterG = float(input("Enter the gravity [0.1-0.2]: "))
    while (enterG < 0.1 or enterG > 0.2):
        print("Outside of range.")
        enterG = float(input("Enter the gravity [0.1-0.2]: "))
    return enterT,enterG
main()