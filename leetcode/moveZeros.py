#Given an array of integers, write a 
#function to move all 0's to the end of the 
#array while maintaining the relative order of the other elements

# [0,1,0,3,12]
# [1,3,12,0,0]


#Q: are the elements sorted?
#A: No

#Q: Could the array only consist of 0s
#A: Yes

#Q: Should you do it in place
#A: Yes

#Big 0 : O(n)
def moveZeroes(nums):
    j = 0
    i = 1
    length = len(nums)
    if(length == 1):
        return nums
    while j != length:
        if(i != length):
            if(nums[i] != 0):
                nums[j] = nums[i]
                j += 1
            i += 1
        else: 
            nums[j] = 0
            j += 1
    return nums
    
print(moveZeroes([1]))
print(moveZeroes([0,1]))
print(moveZeroes([0,0,0,0]))
print(moveZeroes([0,1,0,3,12]))

# j = 3 i = 5 [1,3,12,0,0]