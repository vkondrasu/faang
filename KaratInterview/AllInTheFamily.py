input_data = [[1, 3], [2, 3], [3, 6], [5, 6],[5, 7], [4, 5], [4, 8], [4, 9], [9, 11]]

def findUnknownParents(relationships):
    mapp = {}
    for rel in relationships:
        parent, child = rel[0], rel[1]
        if child in mapp:
            mapp[child].append(parent)
        else:
            mapp[child] = [parent]

        if parent not in mapp:
            mapp[parent] = []

    zero_parents = []
    one_parents = []

    #print(mapp)

    for child in mapp:
        if len(mapp[child]) == 0:
            zero_parents.append(child)
        elif len(mapp[child]) == 1:
            one_parents.append(child)

    return [zero_parents, one_parents]

print(findUnknownParents(input_data))

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def ordIntersection(list1, list2):
    result = []
    for x in list1:
        if x in list2:
            result.append(x)

    return result

def findCommonAncestor(relationships, x, y):
    mapp = {}
    for rel in relationships:
        parent, child = rel[0], rel[1]
        if child in mapp:
            mapp[child].append(parent)
        else:
            mapp[child] = [parent]

    x_parents = [x]
    y_parents = [y]

    next_x = [x]
    next_y = [y]

    temp =[]
    while next_x:
        for x_parent in next_x:
            if x_parent in mapp:
                temp.extend(mapp[x_parent])
            
        next_x = temp
        temp = []
        x_parents.extend(next_x)

    temp =[]
    while next_y:
        for y_parent in next_y:
            if y_parent in mapp:
                temp.extend(mapp[y_parent])
            
        next_y = temp
        temp = []
        y_parents.extend(next_y)


    #print(x_parents)
    #print(y_parents)

    return len(intersection(x_parents, y_parents)) > 0
        


'''

print(findCommonAncestor(input_data, 3, 11))
print(findCommonAncestor(input_data, 1, 2))
'''


assert(findCommonAncestor(input_data, 3, 11) == False)
assert(findCommonAncestor(input_data, 1, 2) == False)
assert(findCommonAncestor(input_data, 6, 4) == True)
assert(findCommonAncestor(input_data, 6, 11) == True)
assert(findCommonAncestor(input_data, 6, 7) == True)
assert(findCommonAncestor(input_data, 5, 4) == True)
assert(findCommonAncestor(input_data, 6, 2) == True)
assert(findCommonAncestor(input_data, 6, 8) == True)
#assert(findCommonAncestor(input_data, 6, 7) == False) #to test that assert is working -- wrong test case


def earliestAncestor(relationships, x, y):
    mapp = {}
    for rel in relationships:
        parent, child = rel[0], rel[1]
        if child in mapp:
            mapp[child].append(parent)
        else:
            mapp[child] = [parent]

    x_parents = [x]
    y_parents = [y]

    next_x = [x]
    next_y = [y]

    temp =[]
    while next_x:
        for x_parent in next_x:
            if x_parent in mapp:
                temp.extend(mapp[x_parent])
            
        next_x = temp
        temp = []
        x_parents.extend(next_x)

    temp =[]
    while next_y:
        for y_parent in next_y:
            if y_parent in mapp:
                temp.extend(mapp[y_parent])
            
        next_y = temp
        temp = []
        y_parents.extend(next_y)

    inter = ordIntersection(x_parents, y_parents)

    if len(inter) > 0:
        return inter[0]
    else:
        return False


assert(earliestAncestor(input_data, 3, 11) == False)
assert(earliestAncestor(input_data, 1, 2) == False)
assert(earliestAncestor(input_data, 6, 4) == 4)
assert(earliestAncestor(input_data, 6, 11) == 4)
assert(earliestAncestor(input_data, 6, 7) == 5)
assert(earliestAncestor(input_data, 5, 4) == 4)
assert(earliestAncestor(input_data, 6, 2) == 2)
assert(earliestAncestor(input_data, 6, 8) == 4)