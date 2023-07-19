# You are given an array people where people[i]
# is the weight of the ith person 
# and an infinite number of boats where each boat 
# can carry a maximum weight of limit. 
#Each boat carries at most two people at the same time
# provided the sum of the weight of those people is at most limit.

# Input: people = [1,2], limit = 3
# Output: 1

#Q: Will a persons weight > the boats limit
#Q: Can a persons weight be 0 


#[3,4,1,2] limit 4

def boatsToSavePeople(people, limit):
    sortedPeople = people.sort()
    largestPerson = len(people) -1
    smallestPerson = 0
    boatCount = 0
    while(largestPerson >= smallestPerson):
        if(people[largestPerson] + people[smallestPerson] <= limit):
            boatCount += 1
            largestPerson -=1
            smallestPerson +=1
        else:
            boatCount += 1
            largestPerson -= 1
    return boatCount     
  
print(boatsToSavePeople([3,4,1,2], 4))
print(boatsToSavePeople([1,2], 3))