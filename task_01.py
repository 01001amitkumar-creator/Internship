import re


def count_words(sentence):
    """Return the number of words in a sentence."""
    return len(sentence.split())


def find_longest_word(sentence):
    """Return the longest word, ignoring surrounding punctuation."""
    words = re.findall(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*", sentence)
    if not words:
        return "No words found"
    return max(words, key=len)


def reverse_sentence(sentence):
    """Return the sentence with its characters in reverse order."""
    return sentence[::-1]


def is_prime(number):
    """Return True if number is prime, otherwise False."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def main():
    print("=== Text and Number Tools ===")

    sentence = input("Enter a sentence: ")
    number_text = input("Enter an integer to check: ")

    print("\n--- Text Results ---")
    print("Word count:", count_words(sentence))
    print("Longest word:", find_longest_word(sentence))
    print("Reversed sentence:", reverse_sentence(sentence))

    print("\n--- Number Result ---")
    try:
        number = int(number_text)
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except ValueError:
        print("Invalid number. Please enter a whole integer.")


if __name__ == "__main__":
    main()
