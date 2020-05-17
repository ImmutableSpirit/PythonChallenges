import random

def get_occurrences(x, source):
    # Use list compression to get indexes of all occurrences of x in the source
    indexPosList = [ i for i in range(len(source)) if source[i] == x ]
    return indexPosList

def guess(letter):
    return get_occurrences(letter, correct_word)  

def reveal_occurrences(new_char, indexes):
    string_builder = []
    global masked_word

    for i in range(len(masked_word)):
        if i in indexes:
            string_builder.append(new_char)
        else:
            string_builder.append(masked_word[i])
    return ''.join(string_builder)

def show_ending_dialogue():
    print("Thanks for playing!")
    print("We'll see how well you did in the next stage")

print('H A N G M A N') 
print('')
max_attempts = 8
choices = ['python', 'java', 'kotlin', 'javascript']
correct_word = random.choice(choices)
masked_word = '-' * len(correct_word)
bad_choice_msg = "No such letter in the word"

# Game Loop
for i in range(max_attempts):
    print(masked_word)
    letter = input("Input a letter: ")
    occurrences = guess(letter)
    if len(occurrences) > 0:
        masked_word = reveal_occurrences(letter, occurrences)
        print('')
    else:
        print(bad_choice_msg)
        print('')

show_ending_dialogue()
