matrix2d=[
              [1,2,3,4,5],
              [2,4,6,8,10],
              [1,3,5,7,9],
              [1,4,7,10,13],
              [2,5,8,11,14]
         ]

def sumDiagonal1(m1):
    sum=0
    for i in range (5):
      sum += m1[i][i]
    return sum

def sumDiagonal2(m2):
    sum=0
    for i in range (5,0):
      sum += m2[i][i]
    return sum

print("Value:",matrix2d)




