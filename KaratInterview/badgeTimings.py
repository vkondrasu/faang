badge_times = [
["Paul", "1355"],
["Jennifer", "1910"],
["John", "835"],
["John", "830"],
["Paul", "1315"],
["John", "1615"],
["John", "1640"],
["Paul", "1405"],
["John", "855"],
["John", "930"],
["John", "915"],
["John", "730"],
["John", "940"],
["Jennifer", "1335"],
["Jennifer", "730"],
["John", "1630"],
["Jennifer", "5"]
]

def withinHour(old, new):
    new_hour , new_min = new //100, new%100
    old_hour , old_min = old //100, old%100

    new_time = new_hour * 60 + new_min
    old_time = old_hour * 60 + old_min

    return (new_time - old_time) <= 60
'''
assert(withinHour(830,835) == True)
assert(withinHour(830,855) == True)
assert(withinHour(830,915) == True)
assert(withinHour(830,930) == True)
assert(withinHour(830,935) == False)
'''
    

def moreThan3InHour():
    mapp = {}
    for entry in badge_times:
        if entry[0] in mapp:
            mapp[entry[0]].append(int(entry[1]))
        else:
            mapp[entry[0]] = [int(entry[1])]
    
    for user in mapp:
        entry_times = sorted(mapp[user])

        start = 0
        count = 1
        old_time = entry_times[0]
        for i in range(1, len(entry_times)):
            if withinHour(old_time, entry_times[i]):
                count += 1
            else:
                if count >= 3:
                    print(user, entry_times[start:i])
                count = 1
                start = i
                old_time = entry_times[i]

        if count >= 3:
            print(user, entry_times[start:i+1])


moreThan3InHour()
