from unittest import result

'''
LC 68. Text Justification
'''
class Solution:
    def fullJustify(sel, words, maxWidth):
        def getLine(words, start, end, lenn, maxx):
            result = ""
            p, q = 1, 0
            if start != end:
                p = (maxx - lenn) // (end - start)
                q = (maxx - lenn) % (end - start)

            for i in range(start, end+1):
                result += words[i]
                if i != end:
                    if end == n-1:
                        result += " "
                    else:
                        result += " "*p
                        if q > 0:
                            result += " "
                            q -= 1
            result += " " * (maxx - len(result))
            return result

        result = []
        start = 0
        n = len(words)

        while start < n:
            j = start-1
            cur_len = 0
            while j+1 < n and cur_len + len(words[j+1]) + (j+1-start) <= maxWidth:
                cur_len += len(words[j+1])
                j += 1

            result.append(getLine(words, start, j, cur_len, maxWidth))
            start = j+1

        return result

s = Solution()
answer = s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print(answer)
answer = s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
print(answer)
answer = s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)
print(answer)