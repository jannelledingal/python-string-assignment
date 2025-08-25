# Dingal IT5(2770) Assignment 1 08/24/2025

def menu():
    print("\nChoose an operation:")
    print("0. Enter a new sentence")
    print("1. Reverse the sentence")
    print("2. Count vowels")
    print("3. Check if palindrome")
    print("4. Find and replace a word")
    print("5. Format (title case)")
    print("6. Split into words")
    print("7. Word frequency counter")
    print("8. Swap case")
    print("9. Exit")

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in sentence if ch in vowels)

def is_palindrome(sentence):
    cleaned = "".join(ch.lower() for ch in sentence if ch.isalnum())
    return cleaned == cleaned[::-1]

# main program 
sentence = input("Enter a sentence: ")

while True:
    print("\n" + "-" * 60)
    print("Current sentence:", sentence)
    menu()
    choice = input("Enter your choice: ").strip()
    print("-" * 60)

    if choice == "0":
        old = sentence
        sentence = input("Enter a new sentence: ")
        print(f"\nPrevious sentence: {old}")
        print(f"New sentence     : {sentence}")

    elif choice == "1":  # Reverse
        old = sentence
        sentence = sentence[::-1]
        print(f"Previous sentence: {old}")
        print(f"New sentence     : {sentence}")

    elif choice == "2":  # Count vowels 
        vc = count_vowels(sentence)
        print(f"Vowel count: {vc}")

    elif choice == "3":  # Palindrome check 
        print("Palindrome:", "Yes" if is_palindrome(sentence) else "No")

    elif choice == "4":  
        old = sentence
        find_word = input("\nWord to find: ")
        if find_word == "":
            print("Cannot replace an empty string. Sentence unchanged.")
        else:
            replace_word = input("\nWord to replace with: ")
            print(f"\n\nWord to find: {find_word}")
            print(f"Word to replace with: {replace_word}")
            sentence = sentence.replace(find_word, replace_word)
            print(f"Previous sentence: {old}")
            print(f"New sentence     : {sentence}")

    elif choice == "5":  # Title case 
        old = sentence
        sentence = sentence.title()
        print(f"Previous sentence: {old}")
        print(f"New sentence     : {sentence}")

    elif choice == "6":  # Split into words 
        words = sentence.split()
        print("Words:", words)

    elif choice == "7":  # Word frequency 
        freq = {}
        for w in sentence.split():
            freq[w] = freq.get(w, 0) + 1
        print("Word frequency:", freq)

    elif choice == "8":  # Swap case 
        old = sentence
        sentence = sentence.swapcase()
        print(f"Previous sentence: {old}")
        print(f"New sentence     : {sentence}")

    elif choice == "9":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again.")
