text1 = input("Please type your string:\n")
def removeChars(text):
    newText=""
    chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for c in text:
        if c not in chars:
            newText += c
    return newText

def removeChars2(text):
    newText2=""
    punchars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for i in range(len(text)):
        if text[i] not in punchars:
            newText2 += text[i]
    return newText2

print("Result:{}".format(removeChars(text1)))
print("Result2:{}".format(removeChars2(text1)))