#Player and computer chooses either goblin, knight, or mage. The winner is determined by the following logic:

#goblin beats mage
#knight beats goblin
#mage beats knight 

import random

computer_choice = ''
choices = ['goblin', 'knight', 'mage']
while True:
    player_choice = input('Enter your choice: ').lower()
    if player_choice not in choices:
        print('Invalid input! Choose either goblin, mage or knight')
    else:
        break
computer_choice = choices[random.randint(0,len(choices)-1)]
print('Computer plays',computer_choice)
if player_choice == computer_choice:
    print('Tie!')
elif (player_choice == 'goblin' and computer_choice == 'mage') or (player_choice == 'knight' and computer_choice == 'goblin') or (player_choice == 'mage' and computer_choice == 'knight'):
    print('You win!')
else:
    print('Computer wins!')
