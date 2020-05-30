#hangman. my simple version

#generate random word from cpu
#ask the user to guess the word from blank lines
#if letter is in word - say correct - ask for other words
#if letter is wrong- say try again
#if all letters are fine - say congrats

import random

wordlist=['dog','cat','rat','mouse','kangaroo','lion','sheep','goat','cow']
cpu_word=random.choice(wordlist)
filler=len(cpu_word)*'-'


while True:

    user_word = input (
        'welcome to hangman. The word im thinking about is {} can you guess a letter in the word? '.format ( filler ) )

    for l in user_word:
        if l in cpu_word:
            print ('yes thats correct there is {} in that word'.format(l))
            reveal=len(cpu_word)*'-'+l
            print('the word is  {} can you try another?'.format(reveal))
            continue

        elif l not in cpu_word:
            print('sorry thats wrong. try again!')









