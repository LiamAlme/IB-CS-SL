import turtle

t = turtle.Turtle()

mystery = open('mystery.txt','r')

for line in mystery:
    if 'DOWN' in line:
        t.pd()
    elif 'UP' in line:
        t.pu()
    else:
        lst = line.split(' ')
        lst[1].rstrip('\n')
        t.goto(int(lst[0]),int(lst[1]))