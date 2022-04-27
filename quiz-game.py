q1 = "which is a sea animal ----"
a1 = "1) shark","2) dog","3) bird","4) frog"
q2 = "who is the fastest animal ---"
a2 = "1) fish","2) tiger","3) turtle","4) worm"
quest = [q1,q2]
ch = [a1,a2]
an = ["1","2"]
i = 0
while i in range(len(quest)):
    print(quest[i],ch[i])
    print(an[i])
    ans = input("your ans --> ")
    if an[i] == ans:
        print("Correct! good job")
    else:
        print("wrong answer! learn harder")
    i += 1

