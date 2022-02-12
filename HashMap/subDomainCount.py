'''
LC 811. Subdomain Visit Count
'''
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mapp = {}
        
        for domain in cpdomains:
            data = domain.split(" ")
            count = int(data[0])
            
            url = data[1]
            
            while url:
                mapp[url] = mapp.get(url, 0) + count
                if "." in url:
                    url = url.split(".",1)
                    if len(url) > 1:
                        url = url[1]
                else:
                    break
                    
        result = []
                    
        for domain in mapp:
            result.append(str(mapp[domain]) + " " + domain)
            
        return result