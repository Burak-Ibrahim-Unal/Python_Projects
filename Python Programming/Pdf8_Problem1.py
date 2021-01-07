studentsDB = [
                [1,"Mustafa","Turkey",[5,4,3,5,4]],
                [2,"Marco","Italy",[4,3,3,5,5]],
                [3,"Ann","Poland",[3.5,5,5,4,4]],
                [4,"Cloudia","Argentina",[4,4,3,3,5]]
              ]

def AvgGrade(list):
    newList=[]
    for i in range(len(list)):
        sum = 0
        for j in range(5):
            sum+=list[i][3][j]
        avg=sum/5
        newList.append(avg)
    """m=max(newList) de yazabiliriz.Ya da alttaki algoritmayı kullanabiliriz."""
    m=newList[0]
    for x in range(len(newList)):
        if m < newList[x]:
            m=newList[x]
    return m,newList

maximum,grades=AvgGrade(studentsDB)

def ShowStudentGrades(list1,list2):
    names=[]
    Grades=grades
    for i in range (len(list1)):
        names.append(list1[i][1])
    for j in range (len(list2)):
        Grades[j] = names[j][1] + grades[j]

    return FinalList


print("Maximum:",maximum)
print("Grades:",grades)
print("İsimler:",ShowStudentGrades(studentsDB,grades))