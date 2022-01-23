'''
LC 1291. Sequential Digits
'''

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def findDigits(num):
            count = 0
            while num > 0:
                num //= 10
                count += 1
            return count
        
        digits = [1,2,3,4,5,6,7,8,9]
        l = findDigits(low)
        h = findDigits(high)
        
        #print(l,h)
        
        def getNumWithDigits(digits):
            num = 0
            for digit in digits:
                num = num*10 + digit
                
            return num
        result = []
        for i in range(l,h+1):
            for j in range(len(digits)-i+1):
                number = getNumWithDigits(digits[j:j+i])
                if number <= high:
                    if number >= low:
                        result.append(number)
                else:
                    return result
                        
        return result
        
        '''
        sample = "123456789"
        n = 10
        nums = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(n - length):
                num = int(sample[start: start + length])
                if num >= low and num <= high:
                    nums.append(num)
        
        return nums
        '''
        
                
        