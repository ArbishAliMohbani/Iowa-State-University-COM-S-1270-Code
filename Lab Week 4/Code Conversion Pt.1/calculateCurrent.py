# Arbish Ali Mohbani                    02/12/2025
# Lab # 3 
def calculateCurrent(voltage1, resistance1):
    current = voltage1 / resistance1
    return current

def main():
    voltage = float(input("Enter the value for voltage: "))
    resistance = float(input("Enter the value for resistance: "))
    num1 = calculateCurrent(voltage, resistance)
    print("The current is: "+str(num1))

if __name__ == "__main__":
    main()

# End