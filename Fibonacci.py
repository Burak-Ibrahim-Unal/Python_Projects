print("""
#################################
Fibonacci
#################################
""")
a=0
b=1
i=toplam=1
while i<10:
    print("Fibonacci dizisi sayıları: {}",toplam)
    toplam=toplam+a
    a=b
    b=toplam
    i+=1