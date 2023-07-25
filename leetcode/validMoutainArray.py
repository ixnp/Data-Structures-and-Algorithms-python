# Given an array of integers arr
#return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

#Big-O O(n)
def validMountainArray(arr):
    if(len(arr) < 3):
        return False
    i = 1 
    #Continue through the array until the end or the elements decrease in value
    while(i < len(arr) and arr[i] > arr[i-1]):
        i += 1
    #Check to see if we are at the start or end of the array
    if(i == 1 or i == len(arr)):
        return False
    #checks to see if the array is decreasing 
    while(i < len(arr) and arr[i] < arr[i-1]):
        i += 1
    return i == len(arr)

# [3,5,5]
# [0,3,2,1]
print(validMountainArray([0,3,2,1]))

