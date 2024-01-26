start_n = [1,2,2,[3,4],(1,2,3),"1",{1,2,3}]
re_set = set()
printSet = []

for i in start_n:
    if type(i) == str or type(i) == bool or type(i) == tuple or type(i) == int or type(i) == float:
        print(True)
    else:
        print(False)
        printSet.append(i)
print("Эти элементы изменямые: ", printSet)






