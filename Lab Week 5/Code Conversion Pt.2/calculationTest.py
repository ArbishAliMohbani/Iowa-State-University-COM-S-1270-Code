# Arbish Ali Mohbani            02/19/2025
# Matthew Holman
# Lab # 5

import myFinances
import myOhmsLaw
import myPhysics
import myShapes

def main():
    choose = str(" ")
    while(choose != "q"):
        choose = input("-------------------------------------------------------\nPlease Choose one option below:\n\n1) Calculate the area and the circumference of circle\n2) Calculate the area and the perimeter of the rectangle\n3) Calculate current\n4) Calculate Resistance\n5) Calculate Voltage\n6) Calculate Final Velocity\n7) Calculate Distance\n8) Calculate the Annual Percentage\n9) Calculate the Compound Amount\n\nType [q] to to quit the program\n-------------------------------------------------------\n\nSelect option from 1 to 9: \n\n")
        if(choose == "1"):
            height = int(input("Enter Height value: "))
            base = int(input("Enter Base value: "))
            length = int(input("Enter Length value: "))
            width = int(input("Enter width value: "))
            print("\nThe Area is: "+str(myShapes.areaofRectangle(height, base)))
            print("The Perimeter is: "+str(myShapes.rectanglePerimeter(length, width)))

        elif(choose == "2"):
            radius = int(input("Enter Radius value: "))
            print("\nThe Area of Circle is: "+str(myShapes.areaofCircle(radius)))
            print("The Circumference of Circle is: "+str(myShapes.circleCircumference(radius)))

        elif(choose == "3"):
            voltage = int(input("Enter Voltage Value: "))
            resistance = int(input("Enter Resistance Value: "))
            print("\nThe Current is: "+str(myOhmsLaw.calculateCurrent(voltage, resistance)))

        elif(choose == "4"):
            voltage = int(input("Enter Voltage Value: "))
            current = int(input("Enter Current Value: "))
            print("\nThe Resistance is: "+str(myOhmsLaw.calculateResistance(voltage, current)))

        elif(choose == "5"):
            current = int(input("Enter Current Value: "))
            resistance = int(input("Enter Resistance Value: "))
            print("\nThe Voltage is: "+str(myOhmsLaw.calculateVoltage(current, resistance)))

        elif(choose == "6"):
            initial_velocity = int(input("Enter Initial Velocity value: "))
            acceleration = int(input("Enter the Acceleration value: "))
            time = int(input("Enter Time Value: "))
            print("\nThe Final Velocity is: "+str(myPhysics.velocityAccelerationTime(initial_velocity, acceleration, time)))

        elif(choose == "7"):
            time = int(input("Enter Time value: "))
            speed = int(input("Enter Speed value: "))
            print("\nThe Distance is: "+str(myPhysics.distanceSpeedTime(time, speed)))

        elif(choose == "8"):
            interest_charges = int(input("Enter Interest Charges: "))
            fees = int(input("Enter Fees: "))
            loan_amount = int(input("Enter Loan Amount: "))
            days_in_term = int(input("Enter Days in Term: "))
            print("\nThe Annual Percentage Rate is: "+str(myFinances.annualPercentageRate(interest_charges, fees, loan_amount, days_in_term)))

        elif(choose == "9"):
            principal = int(input("Enter the Principal value: "))
            rate = int(input("Enter Rate: "))
            number_compounds = int(input("Enter the Number it Compounds: "))
            time = int(input("Enter the Time: "))
            print("\nThe Accured Amount is: "+str(myFinances.compoundAmount(principal, rate, number_compounds, time)))

    print("Thank you for Using!")

if __name__ == "__main__":
    main()
