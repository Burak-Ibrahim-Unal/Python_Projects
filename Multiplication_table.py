print("""
############################
The multiplication table (Burak Ibrahim Unal)
############################

""")
for i in range(1,11):
    for j in range(1,11):
        if j==10:
            print("{}*{}={}".format(i, j, i * j))
            print("\n############################\n")
        else:
            print("{}*{}={}".format(i, j, i * j))
