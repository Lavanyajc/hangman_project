import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# replace every letter in chosen_word with blank spaces
lives = 6
end_of_game = False

display = []
for letter in chosen_word:
    display += '_'
print(display)

while not end_of_game:
    guess = input("guess a letter:").lower()

    if guess in display:
        print("you already entered this letter")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print("Letter is not in the chosen_word, you lost a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOSE")
            print(f"chosen word is {chosen_word}")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("YOU WIN")
        print("chosen_word")
        #print(f"chosen word is {chosen_word}")              