'''
LC 929. Unique Email Addresses
'''
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mapp = {}
        count = 0
        for email in emails:
            mailId, domain = email.split("@")
            mailId = mailId.split("+")[0]
            mailId = mailId.replace(".","")
            
            if domain in mapp:
                if mailId not in mapp[domain]:
                    mapp[domain].add(mailId)
                    count += 1
            else:
                mapp[domain] = set([mailId])
                count += 1
                    
        return count