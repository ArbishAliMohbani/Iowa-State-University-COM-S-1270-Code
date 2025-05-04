# Arbish Ali Mohbani                    02/12/2025
# Lab # 3 
def calculateResistance(voltage1, current1):
    resistance = voltage1 / current1
    return resistance

def main():
    voltage = float(input("Enter the value for voltage: "))
    current = float(input("Enter the value for current: "))
    num1 = calculateResistance(voltage, current)
    print("The resistance is: "+str(num1))

if __name__ == "__main__":
    main()

# End