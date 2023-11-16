import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    l=[]
    for i in range(100):
        a=random.randint(0,1)
        l.append(a)
    streak = 0
    for i in range(len(l) - 5):
        is_streak = True
        for j in range(6):
            if l[i + j] != l[i]:
                is_streak = False
                break
        if is_streak:
            streak += 1

    if streak > 0:
        numberOfStreaks += 1
print('Chance of streak: %s%%' % (numberOfStreaks / 10000))