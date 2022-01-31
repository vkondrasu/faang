'''
LC 49. Group Anagrams
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramap = {}
        
        for word in strs:
            
            key = ''.join(sorted(word))
            if key in anagramap:
                oldlist = anagramap[key]
                oldlist.append(''.join(word))
                anagramap[key] = oldlist
            else:
                anagramap[key] = [''.join(word)]
          
        result = []
        for key in anagramap:
            result.append(anagramap[key])
            
        return result