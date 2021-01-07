"""
Checking Palindromes – a program that checks whether a string is a palindrome
(if it reads the same forward and backward)
 Problem solution:
 checking whether the first character in the string is the same as the last character
  if so, then checking whether the second character is the same as the second-to-last character
  continue proces until mismatch is found or all characters in the string are checked,
 exept for the middle character if the sting has an old number of characters
  Guidelines:  Prompt the user to enter a string  Report wheather the string is a palindrome
Problem 3
"""

def main():
    str=input("Enter string please:").strip()
    if (control(str)):
        print(str +" is Palindrome")
    else:
        print(str+ " is not palindrome")

def control(text):
    first=0
    last=len(text)-1
    while first < last:
        if text[first] != text[last]:
            return False
        first+=1
        last-=1
    return True

main()