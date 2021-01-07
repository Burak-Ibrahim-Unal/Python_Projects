"""
Vowel removing – a program that removes all the vowels from a string
e.g. input → ”alphabet” output → ”lphbt”  Guidelines:
 Write a function that has one string parameter and returns string without vowels

"""

text1 = input("Please type your string:\n")
def ExtVowel(text):
    vowels="aeiouAEIOU"
    newText=""
    for i in text:
        if i not in vowels:
            newText +=i
    return newText

def ExtVowel2(text):
    vowels={'a','e','i','o','u','A','E','I','O','U'}
    newText2=""
    for i in range(len(text)):
        if text[i] not in vowels:
            newText2+=text[i]
    return newText2

print("Result1:{}\n".format(ExtVowel(text1)))
print("Result2:{}\n".format(ExtVowel2(text1)))
