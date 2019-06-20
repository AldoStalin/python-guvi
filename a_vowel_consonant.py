a_char=input()
a_vowel=['a','e','i','o','u']
if a_char.isalpha()==0:
    print("invalid")
elif a_char in a_vowel:
    print("Vowel")
else:
    print("Consonant")
