badge_times1 = [
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

badge_times =[
["Paul",      "1355"], ["Jennifer",  "1910"], ["Jose",    "835"],
  ["Jose",       "830"], ["Paul",      "1315"], ["Chloe",     "0"],
  ["Chloe",     "1910"], ["Jose",      "1615"], ["Jose",   "1640"],
  ["Paul",      "1405"], ["Jose",       "855"], ["Jose",    "930"],
  ["Jose",       "915"], ["Jose",       "730"], ["Jose",    "940"],
  ["Jennifer",  "1335"], ["Jennifer",   "730"], ["Jose",   "1630"],
  ["Jennifer",     "5"], ["Chloe",     "1909"], ["Zhang",     "1"],
  ["Zhang",       "10"], ["Zhang",      "109"], ["Zhang",   "110"],
  ["Amos",         "1"], ["Amos",         "2"], ["Amos",    "400"],
  ["Amos",       "500"], ["Amos",       "503"], ["Amos",    "504"],
  ["Amos",       "601"], ["Amos",       "602"]
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


#moreThan3InHour()


badge_records_1 = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Martha",   "enter"],
  ["Steve",    "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Paul",     "enter"],
  ["Curtis",   "exit"],
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
  ["Paul",     "enter"],
  ["Paul",     "enter"],
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Paul",     "enter"],
  ["Paul",     "exit"],
  ["Paul",     "exit"] 
]

badge_records_2 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
]

badge_records_3 = [
  ["Paul", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
]

badge_records_4 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
  ["Paul", "enter"],
]

def inCorrectEntries(badge_records):
    mapp = {}
    exit_before_entry = set()
    entry_before_exit = set()
    for user, action in badge_records:
        if user not in mapp:
            if action == "exit":
                exit_before_entry.add(user)
            mapp[user] = action
        else:
            if action == mapp[user]:
                if action == "enter":
                    entry_before_exit.add(user)
                else:
                    exit_before_entry.add(user)
            
            mapp[user] = action

    print("exit_before_entry")
    print(exit_before_entry)
    print("entry_before_exit")
    print(entry_before_exit)


inCorrectEntries(badge_records_1)
#inCorrectEntries(badge_records_2)
#inCorrectEntries(badge_records_3)
#inCorrectEntries(badge_records_4)