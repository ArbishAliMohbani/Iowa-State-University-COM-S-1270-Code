# Arbish Ali Mohbani                    02/12/2025
# Lab # 3 

def calculateVoltage(current1, resistance1):
    voltage = current1 * resistance1
    return(voltage)

def main():
    current = float(input("Enter the value for current: "))
    resistance = float(input("Enter the value for resistance: "))
    num1 = calculateVoltage(current, resistance)
    print("The voltage is: "+str(num1))


if __name__ == "__main__":
    main()

# End