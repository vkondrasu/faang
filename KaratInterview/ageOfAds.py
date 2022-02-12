#LC 811. Subdomain Visit Count
def domainCounting(cpdomains):
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
'''
print(domainCounting(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
print(domainCounting(["9001 discuss.leetcode.com"]))
'''


def compareBrowsing(history1, history2):
    n1 = len(history1)
    mapp = {}
    for i in range(n1):
        if history1[i] in mapp:
            mapp[history1[i]].append(i)
        else:
            mapp[history1[i]] = [i]

    n2 = len(history2)

    max_count = 0
    max_path = []

    for i in range(n2):
        if history2[i] in mapp:
            for ind in mapp[history2[i]]:
                start_1 = ind
                start_2 = i

                count = 0

                while start_1 < n1 and start_2 < n2:
                    if history1[start_1] == history2[start_2]:
                        start_1 += 1
                        start_2 += 1
                        count += 1
                    else:
                        break

                if count > max_count:
                        max_path = history1[ind: start_1]
                        max_count = count

    return max_path
            

user0 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user1 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]


print(compareBrowsing(user0, user1))
print(compareBrowsing(user2, user1))
print(compareBrowsing(user0, user2))
print(compareBrowsing(user5, user2))
print(compareBrowsing(user3, user4))
print(compareBrowsing(user4, user3))

#complete when input data is available
def adSuccessRate():
    pass
