import random
count = 0
dog = open('dog.txt','w')

let = 'abcdefghijklmnopqrstuvwxyz'

for i in range(100000):
    for i in range(20):
        for i in range(3):
            dog.write(random.choice(let))
        dog.write(' ')
    dog.write('\n')
dog.close()

dog = open('dog.txt','r')
for line in dog:
    lst=line.split()
    for i in range(len(lst)):
        if 'dog' in lst[i]:
            count += 1

print(count)