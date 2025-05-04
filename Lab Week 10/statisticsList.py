# https://www.wyzant.com/resources/lessons/math/statistics_and_probability/averages/

import random
def findMean(num_list, element_len):
    total = 0
    for i in range(0, element_len):
        total+=num_list[i]
    mean = total/element_len
    return mean

def findMedian(num_list, element_len):
    num_list.sort()
    median = 0
    median_num = element_len/2
    if(median_num%2==0):
        median = (num_list[int(median_num)]+num_list[int(median_num+1)])/2
    else:
        median = num_list[int(median_num+0.5)]
    return median


def generateInput():
    num_list = []
    element_len = random.randrange(200, 501)
    for i in range(0, element_len+1):
        num_list.append(random.randrange(1, 2001))
    return num_list, element_len

def main():
    num_list, element_len = generateInput()
    mean = findMean(num_list, element_len)
    median = findMedian(num_list, element_len)
    print("Mean: {"+str(mean)+"}\nMedian: {"+str(median)+"}")

if __name__ == "__main__":
    main()