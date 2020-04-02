# Sam Cole
# Palindrome Check


def is_palindrome(word):
    word.strip()
    word.lower()
    if len(word) == 1 or 0:
        return True
    else:
        if word[0] == word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False


word = str(input("Enter a word you think might be a palindrome"))
if is_palindrome(word):
    print("This word is a Palindrome")
else:
    print("This word isnt a Palindrome")
