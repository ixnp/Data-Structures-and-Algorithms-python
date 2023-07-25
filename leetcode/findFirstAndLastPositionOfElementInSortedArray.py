# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

def getStart(nums,target):
    start = 0
    end = len(nums)-1

    while(start <= end):
        mid = floor((start+end)/2)
        if(nums[mid] == target):
            if(mid-1 >= 0 and nums[mid-1] != target or mid == 0):
                return mid
            end = mid-1
        elif(nums[mid] > target):
            end = mid-1
        else:
            start = mid+1
    return -1

def getEnd(nums,target):
    start = 0
    end = len(nums)-1

    while(start <= end):
        mid = floor((start+end)/2)
        if(nums[mid] == target):
            if(mid+1 < len(nums) and nums[mid+1] != target or mid==len(nums)-1):
                return mid
            start = mid+1
        elif(nums[mid] > target):
            end = mid-1
        else:
            start = mid+1
    return -1

def searchRange(nums, target):
    start = getStart(nums,target)
    end = getEnd(nums,target)

    return [start,end]
print(searchRange([5,7,7,8,8,10],8))
