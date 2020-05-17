#  MODULES
import random
import unittest


#  METHODS
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
    cond1 = lambda lives : lives > 0
    cond2 = lambda word : '-' not in word
    return cond1(lives) and cond2(masked_word)

def show_bad_ending():
    print("You are hanged!")

def show_good_ending():
    global correct_word
    print(f"You guessed the word {correct_word}!")
    print("You survived!")

def input_valid(user_input):
    if len(user_input) != 1 or user_input.isspace():
        print("You should print a single letter")
        print('')
        return False
    if user_input.isupper():
        print('It is not an ASCII lowercase letter')
        print('')
        return False
    if already_guessed(user_input):
        print("You already typed this letter")
        print('')
        return False
    return True

def test_initialize():
    global lives
    lives = 8
    global win_condition
    win_condition = False
    global choices
    choices = ['python', 'java', 'kotlin', 'javascript']
    global correct_word
    correct_word = random.choice(choices)
    global masked_word
    masked_word = '-' * len(correct_word)
    global bad_choice_msg
    bad_choice_msg = "No such letter in the word"    
    
#  MAIN SETUP
print('H A N G M A N') 
print('')

lives = 8
win_condition = False
choices = ['python', 'java', 'kotlin', 'javascript']
correct_word = random.choice(choices)
masked_word = '-' * len(correct_word)
bad_choice_msg = "No such letter in the word"


#  GAME LOOP
while (lives > 0):
    print(masked_word)
    letter = input("Input a letter: ")
    if input_valid(letter) == False:
        continue
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

#  RESOLUTION

if win_condition:
    show_good_ending()
else:
    show_bad_ending()



# UNIT TESTING

print('')
print(' ========== UNIT TESTING ========== ')
print('')

test_initialize()

class TestHangmanProjectMethods(unittest.TestCase):

    def test_input_valid_req_one_char(self):
        self.assertTrue(input_valid('a'))
        self.assertFalse(input_valid('aa'))
        self.assertFalse(input_valid('aA'))
        self.assertFalse(input_valid('Aa'))
        self.assertFalse(input_valid(''))
        self.assertFalse(input_valid(' '))

if __name__ == '__main__':
    unittest.main()