from random import randint
from functions.feedback import feedback


def joke():
    num = randint(0, 16)
    if num == 0:
        print('What do dentists call their x-rays?\nTooth pics!')
    if num == 1:
        print('There’s a fine line between a numerator and a denominator.')
    if num == 2:
        print('Did you hear about the first restaurant to open on the moon?')
        print('It had great food, but no atmosphere.')
    if num == 3:
        print('What did one ocean say to the other ocean?\nNothing, it just waved.')
    if num == 4:
        print('Do you want to hear a construction joke?\nSorry, I’m still working on it.')
    if num == 5:
        print('Did you hear about the fire at the circus?\nIt was in tents!')
    if num == 6:
        print('Why do ducks have feathers?\nTo cover their butt quacks!')
    if num == 7:
        print('Why should you never trust stairs?\nThey’re always up to something.')
    if num == 8:
        print('When does a joke become a ‘dad’ joke?\nWhen it becomes apparent.')
    if num == 9:
        print('I entered ten puns in a contest to see which would win.\nNo pun in ten did.')
    if num == 10:
        print('Why is Peter Pan always flying?\nBecause he Neverlands.')
        print('(I love this joke because it never grows old.)')
    if num == 11:
        print('Two windmills are standing on a wind farm.\nOne asks, ‘What’s your favorite kind of music?’')
        print('The other replies, ‘I’m a big metal fan.’')
    if num == 12:
        print('I took the shell off of my racing snail, thinking it would make him faster.')
        print('But if anything, it made him more sluggish.')
    if num == 13:
        print(
            'You know, it was so cold in D.C. the other day, I saw a politician with his hands in his own pockets.')
    if num == 14:
        print('How many tickles does it take to get an octopus to laugh?\nTen tickles')
    if num == 15:
        print(
            'My teachers told me I’d never amount to much since I procrastinate so much.\nI told them, “Just you wait!”')
    if num == 16:
        print('I need more jokes!!!')
    nex = input('\nanother?\ny/n\n')
    if nex == 'y':
        joke()
    if nex == 'n' and num >= 5:
        fed = input('Would you like to leave feedback?\ny/n\n')
        if fed == 'y':
            feedback()
        if fed == 'n':
            print('ok')
