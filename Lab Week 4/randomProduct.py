# Arbish Ali Mohbani            02/12/2025
# Lab # 3               
# Mattew Holman
    

import random

def randomProduct(num1, num2, num3):
    product = int(1)
    temp = int(0)
    for i in range(0, num1+1):
        temp = random.randrange(num2, num3)
        product*=temp
    return product

    
def main():
    a = int(input("Enter Number 1: "))
    b = int(input("Enter Number 2: "))
    c = int(input("Enter Number 3: "))
    final_product = randomProduct(a, b, c)
    print("The random product is: "+str(final_product))


if __name__ == "__main__":
    main()
