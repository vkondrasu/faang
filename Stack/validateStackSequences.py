'''
LC 946. Validate Stack Sequences
'''
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushlen = len(pushed)
        poplen = len(popped)
        
        i , j = 0, 0
        st = []
        
        while i < pushlen or j < poplen:
            #if our stack is empty we have to do a push
            if len(st) == 0:
                if i < pushlen:
                    st.append(pushed[i])
                    i+=1
                else: #if there is nothing else to push then we can return False
                    return False
            
            elif st[-1] == popped[j]: #if top of the stack matches current element at pop.. then pop it
                st.pop()
                j += 1
            elif i == pushlen:#we have reached end of pushed but not end of popped so return False
                return False
            else:#we have something to push onto the stack
                st.append(pushed[i])
                i += 1
                
        return True