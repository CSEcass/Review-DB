# Leek Code Problem: Find the number that doesnt repeat
numlist = [2,3,3,8,2,3,2]
print(numlist)

for num in numlist:
    amount = numlist.count(num)
    if amount == 1:
        print('Unique number: ' + str(num))
    else:
        print('Not a unique number.')
print()
# NOTE the above operation takes too long, below is a shorter way.

def f():
    k = input()
    numlist = input().split(' ')
    numdict = {}
    for num in numlist:
        if num in numdict.keys():
            numdict[num] = numdict[num] + 1
        else:
            numdict[num] = 1
    for num, amount in numdict.items():
        if amount == 1:
            print(num)
            return
f()