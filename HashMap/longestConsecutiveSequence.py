'''
LC 128. Longest Consecutive Sequence
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        uniq = set()
        max_count = 0
        #make a unique set of number
        for num in nums:
            uniq.add(num)
            
        for num in nums:
            #if there is num+1 don't do anything -- num is not a strating point of new range
            #we always start counting from a number that starts range
            if num-1 not in uniq:
                count = 0
                temp = num+1
                
                while temp in uniq:
                    temp += 1
                    
                count = (temp-num)
                max_count = max(max_count, count)
                
        return max_count
    
    '''
    O(N) how ?
    if num-1 not in uniq:
    at the above statement we are only running through the numbers -- if it's a start of new range, till end of range
    This means, we are running each range only once
    in this example [100,4,200,1,3,2]
    Ranges are 1-4, 100-100 and 200-200
    in 1-4
    if we encounter 2,3,4 we don't do anything 
    when we encountered 1, 1-1 = 0 not in set so we start looking for elements in the range starting at 1
    by this way each range is traversed only once thus makes the Time complexity O(N)
    Space complecity O(N) -- as we are storing unique elements in a set
    '''