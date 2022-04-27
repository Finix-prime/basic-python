mm = ['1)-main course','2)-dessert','3)-drink']
mc = ['1)-tom yum','2)-papaya salad','3)-steak',]
mc1 = ['tom yum','papaya salad','steak']
de = ['1)-bualoy','2)-marcaron','3)-cake']
de1 = ['bualoy','marcaron','cake']
dr = ['1)-water','2)-juice','3)-beer',]
dr1 =['water','jiuce','beer']
n = "0"
order = "0"
orderlist = []
print(mm)
while n != '4':
    n = input('please choose your menu or 4 to finished -->')
    if n == '1':
        print(mc)
        while order != '4':
            order = input('choose your main course and 4 finished main course-->')
            if order == '4':
                order = "0"
                break
            else:
                orderlist.append(mc1[int(order)-1])
                order = "0"
    elif n == '2':
        print(de)
        while order != '4':
            order = input('choose your main course and 4 finished dessert-->')
            if order == '4':
                order = "0"
                break
            else:
                orderlist.append(de1[int(order)-1])
                order = "0"

    elif n == '3':
        print(dr)
        while order != '4':
            order = input('choose your main course and 4 finished drink-->')
            if order == '4':
                order = "0"
                break
            else:
                orderlist.append(dr1[int(order)-1])
                order = "0"
    elif n == '4':
        print("your order is" ,orderlist)
        order = "0"
        break
    else:
        print("error star again")
        n = ""
        order ="0"
        break




