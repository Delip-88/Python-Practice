import random
import string

# Get all lowercase ASCII letters
s = string.ascii_lowercase

def encrypt(word):
    if len(word) >= 3:
        # Generate 3 random characters for both beginning and end
        random3char_b = random.choices(s, k=3)
        random3char_e = random.choices(s, k=3)

        # Convert word to list for easy manipulation
        word_list = list(word)
        # Remove the first letter
        first_ltr = word_list.pop(0)
        # Append the removed first letter to the end
        word_list.append(first_ltr)

        # Combine random characters and modified word list
        return ''.join(random3char_b + word_list + random3char_e)
    else:
        # For words less than 3 characters, return the reversed word
        return word[::-1]

def decrypt(word):
    if len(word) >= 3:
        # Remove the first 3 and last 3 random characters
        list_word = word[3:-3]

        # Get the last character of the modified word
        first_word = list_word[-1]
        # Remove the last character from the list
        list_word = list_word[:-1]
        # Insert the removed last character at the beginning
        list_word = first_word + list_word

        return list_word
    else:
        # For words less than 3 characters, return the reversed word
        return word[::-1]

# Get input from the user
word = input("Enter a word: ")

# Encrypt the input word
encrypted_word = encrypt(word)
print("The encrypted word is: ", encrypted_word)

# Decrypt the encrypted word
decrypted_word = decrypt(encrypted_word)
print("The decrypted word is: ", decrypted_word)
