print("""
##############################
Pisagor List...(Burak Ibrahim Unal)
##############################
""")


def findPisagor():
    pis_list = []
    for i in range(1, 101):
        for j in range(1, 101):
            k = ((i ** 2) + (j ** 2)) ** 0.5
            if k == int(k):
                pis_list.append((i,j,int(k)))
    return pis_list

for i in findPisagor():
    print(i)




