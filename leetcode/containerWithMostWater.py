# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

#Big-O: O(n)
def maxArea(height):
    p1 = 0
    p2 = len(height)-1
    maxArea = 0
    if(p2 == 0):
        return False
    if(p2 == 1):
        if(height[0] < height[1]):
            return height[0] * 1
        else:
            return height[1] * 1
    while(p1 < p2):
        width = abs(p1 - p2)
        currentHeight = min(height[p1], height[p2])
        area = currentHeight * width
        maxArea = max(maxArea,area)
        if(height[p1] < height[p2]):
            p1 +=1
        else:
            p2 -=1
        
    return maxArea

print(maxArea([2,3,4,5,18,17,6]))