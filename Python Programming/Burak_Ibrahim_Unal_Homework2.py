"""

Typical autocorrect functions are as follows:
1) if a word starts with two capitals, followed by a lower-case letter, the second capital is made lower case;
2) if a sentence contains a word that is immediately followed by the same word, the second occurrence is removed;
3) if a sentence starts with a lower-case letter, that letter is turned into a capital;
4) if a word consists entirely of capitals, except for the first letter which is lower case,
then the case of the letters in the word is reversed;
5) if the sentence contains the name of a day (in English) which does not start with a capital,
 the first letter is turned into a capital.
Write a function that takes a sentence and makes these auto-corrections. Test it out on the string below.


---------------------------
Burak Ibrahim Unal Homework
---------------------------
"""
""" 1) if a word starts with two capitals, followed by a lower-case letter, the second capital is made lower case;"""
def wordStartsCapital(list):
    newList=[]
    for i in list:
        if i[0:2].isupper() and i[2].islower():
            i=i.capitalize()
        newList.append(i)
    return newList
"""2) if a sentence contains a word that is immediately followed by the same word, the second occurrence is removed;"""
def wordContainsSame(lst):
    newList=[]
    for i in lst:
        if lst.count(str(i))>1:
            lst.remove(i)
        newList.append(i)
    return newList

"""3) if a sentence starts with a lower-case letter, that letter is turned into a capital;"""
def firstUpper(lst):
    newList=[]
    for i in range(len(lst)):
        if i==0:
            lst[i]=lst[i].capitalize()
        else:
            pass
        newList.append(lst[i])
    return lst

"""4) if a word consists entirely of capitals, except for the first letter which is lower case,
then the case of the letters in the word is reversed;"""
def firstLowerInvert(lst):
    newList=[]
    for i in lst:
        if i[0].islower() and i[1:].isupper():
            i=i[::-1]
        newList.append(i)
    return newList

"""5) if the sentence contains the name of a day (in English) which does not start with a capital,
 the first letter is turned into a capital."""
def dayStartsNotCapital(lst):
    days_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    newList=[]
    for i in lst:
        if i in days_list:
            i=i.capitalize()
        else:
            pass
        newList.append(i)
    return newList

def main():
    sentence = "as it turned out our chance meeting with REverend aRTHUR BElling was was to change our whole way of life,and " \
               "every sunday we'd hurry along to St lOONY up the Cream BUn and Jam..."
    myList = sentence.split(" ")
    myList = wordStartsCapital(myList)
    myList = wordContainsSame(myList)
    myList = firstUpper(myList)
    myList = firstLowerInvert(myList)
    myList = dayStartsNotCapital(myList)
    print(' '.join(myList))

main()

"""
TEST
print(wordStartsCapital(myList))
print (wordContainsSame(myList))
print(firstUpper(myList))
print(firstLowerInvert(myList))
print(dayStartsNotCapital(myList))
"""
