from dictionary import dictionary
import random


def every_second_letter(word):
    hint = "_".join([word[i] for i in range(0, len(word), 2)])
    print(hint)


def give_hint(word, attempt):
    if attempt == 1:
        first_letter = word[0]
        print(f"Hint: The first letter is: {first_letter}")
    elif attempt == 2:
        print("Last hint: ", end=" ")
        every_second_letter(word)


def voc_checker():
    correct_count = 0
    while True:
        random_word = random.choice(list(dictionary.keys()))
        print(f"Translate from English into German: {random_word}")
        translation = input("Write the translation here (or type 'q' to quit): ")

        if translation.lower() == 'q':
            print(f"You got {correct_count} correct! See you soon!")
            break

        if translation == dictionary[random_word]:
            print("Correct!")
            correct_count += 1
        else:
            for attempt in range(1, 3):
                give_hint(dictionary[random_word], attempt)
                second_try = input("Try again (or type 'q' to quit): ")

                if second_try.lower() == 'q':
                    print(f"You got {correct_count} correct! See you soon!")
                    return

                if second_try == dictionary[random_word]:
                    print("Correct!")
                    correct_count += 1
                    break
            else:
                print(f"Sorry, the correct translation was: {dictionary[random_word]}")


voc_checker()
