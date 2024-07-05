def check_vowel():
    s = input("Enter a String: ")
    vowels = 'aeiouAEIOU'
    for char in s:
        if char in vowels:
            print("The string contains a vowel.")
            return
    print("The string does not contain any vowel.")

check_vowel()