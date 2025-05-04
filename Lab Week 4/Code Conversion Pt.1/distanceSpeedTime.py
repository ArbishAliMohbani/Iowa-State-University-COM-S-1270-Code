# Arbish Ali Mohbani                    02/11/2025
# Lab # 3 
def distanceSpeedTime(time, speed):
    distance = time * speed
    return distance

def main():
    num1 = float(input("Enter the value for time: "))
    num2 = float(input("Enter the value for speed: "))
    num3 = distanceSpeedTime(num1, num2)
    print("The distance is: "+str(num3))


if __name__ == "__main__":
    main()

# End