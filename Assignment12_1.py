def CheckVowel(chr):
    
    if chr in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")

char = input("Enter a character: ")

CheckVowel(char)
