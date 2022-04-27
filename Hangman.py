ans = ['astronaut','project','office','teacher','reaction','expensive','mosquito','dracula','building','nuclear']
shape1 = {"a_tr__a_t": "some kind of pilot"}
shape2 = {"_ro__ct":"what manager always do"}
shape3 = {"_ff_c_":"a place where you work"}
shape4 = {"t_a_h_r":"some one who learning from"}
shape5 = {"_e__ti_n":"how you act"}
shape6 = {"e_p_n_si_e":"the blue diamond price"}
shape7 = {"m_sq__t_":"the animal who take the blood for food"}
shape8 = {"__a_u_a":"from the fantasy novels about the immortal blood taker"}
shape9 = {"b__ld_n_":"a structure where do you live in"}
shape10 = {"_u__ea_":"the high energy can be exploded with a huge damage"}
shapelist = [shape1,shape2,shape3,shape4,shape5,shape6,shape7,shape8,shape9,shape10]
i = 0
life = 10
while i in range(10):
    print("quit press 1")
    print(shapelist[i],"life =",life)
    check = input("ans = ")
    if check == "1":
        break
    if check == ans[i]:
        print("Congrats nex level")
        i += 1
    else:
        life -= 1
        print("Wrong answer try again ----> ","life =",life)
        if life == 0:
            print("game over")
            break




