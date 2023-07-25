# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

def lengthOfLongestSubstring(str):
    map = {} 
    subStringLength = 0
    start = 0
    end = 0
    length = len(str)
    while(start < length and end < length):
        current = str[end]
        if(current in map):
            start = max(start, map[current]+1)

        map[current] = end
        subStringLength = max(subStringLength,end - start +1)
        end+=1
    return subStringLength

print(lengthOfLongestSubstring('abcabcbb'))
# length = 8
# start = 0
# end = 3
# subString = 3
# map {a = 0, b=1, c=2}

