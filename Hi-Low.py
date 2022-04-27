import random

d1 = random.randint(1,6)
d2 = random.randint(1,6)
d3 = random.randint(1,6)
print('choose where you bet --- "High-Mid-Low" ')
ans = ""
point = d1+d2+d3
show = {1:"high",2:"mid",3:"low"}

if point <= 9:
    ans = show[3]
elif point < 9 and point <=18:
    ans = show[2]
else:
    ans = show[1]

guess = input("bet --> ")

if guess == ans:
    print("You Win !!!!")
else:
    print("Sorry! you loose come on do it again")


