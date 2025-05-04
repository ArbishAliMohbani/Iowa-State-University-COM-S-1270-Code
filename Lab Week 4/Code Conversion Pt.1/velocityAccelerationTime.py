# Arbish Ali Mohbani                    02/11/2025
# Lab # 3 

def velocityAccelerationTime(initial_velocity1, acceleration1, time1):
    final_velocity = initial_velocity1 + (acceleration1 * time1)
    return final_velocity

def main():
    initial_velocity = float(input("Enter the value for initial velocity (m/s): "))
    acceleration = float(input("Enter the value for acceleration (m/s^2): "))
    time = float(input("Enter the value for time (sec): "))
    num1 = velocityAccelerationTime(initial_velocity, acceleration, time)
    print("The Final velocity is: "+str(num1)+" m/s")


if __name__ == "__main__":
    main()

# End