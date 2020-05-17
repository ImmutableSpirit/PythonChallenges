import random

def get_occurrences(x, source):
    # Use list compression to get indexes of all occurrences of x in the source
    indexPosList = [ i for i in range(len(source)) if source[i] == x ]
    return indexPosList

def guess(letter):
    return get_occurrences(letter, correct_word)  

def already_guessed(letter):
    global masked_word
    return letter in masked_word

def reveal_occurrences(new_char, indexes):
    string_builder = []
    global masked_word

    for i in range(len(masked_word)):
        if i in indexes:
            string_builder.append(new_char)
        else:
            string_builder.append(masked_word[i])
    return ''.join(string_builder)

def win_condition_check():
    global lives
    global masked_word
    cond1 = lives > 0
    cond2 = '-' not in masked_word
    return cond1 and cond2

def show_bad_ending():
    print("You are hanged!")

def show_good_ending():
    print("You guessed the word!")
    print("You survived!")

print('H A N G M A N') 
print('')

lives = 8
win_condition = False
choices = ['python', 'java', 'kotlin', 'javascript']
correct_word = random.choice(choices)
masked_word = '-' * len(correct_word)
bad_choice_msg = "No such letter in the word"

# Game Loop
while (lives > 0):
    print(masked_word)
    letter = input("Input a letter: ")
    if already_guessed(letter):
        print("No improvements")
        lives -= 1
        print('')
    else: 
        occurrences = guess(letter)
        if len(occurrences) > 0:
            masked_word = reveal_occurrences(letter, occurrences)
            if win_condition_check():
                win_condition = True
                break
            print('')
        else:
            print(bad_choice_msg)
            lives -= 1
            print('')

if win_condition:
    show_good_ending()
else:
    show_bad_ending()
