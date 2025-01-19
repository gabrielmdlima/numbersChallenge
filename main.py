from os import system, name
from random import randint
import keyboard

MAIN_MENU = ('Play game', 'Choose difficulty', 'Instructions', 'Exit game', ' MAIN MENU ')
DIFF_MENU = ('Easy', 'Medium', 'Hard', 'Back to Main Menu', ' CHOOSE DIFFICULTY ')
INSTRUCTIONS_MENU = ('Back to Main Menu', 'Exit game', ' MENU ')
SECONDARY_MENU = ('Play again', 'Back to Main Menu', ' Leave game ', ' MENU ')
PAUSE_MENU = ('Resume game', 'Back to Main Menu', 'Leave game', ' PAUSE ')
EASY = 4
MEDIUM = 5
HARD = 6

global numbers, attempts
global guesses
global corrects
numbers = []
guesses = []
corrects = []
attempts = 0


def main_title():
  clear_screen()
  print(
"""······················································
:     _   _                 _                        :
:    | \ | |_   _ _ __ ___ | |__   ___ _ __ ___      :
:    |  \| | | | | '_ ` _ \| '_ \ / _ \ '__/ __|     :
:    | |\  | |_| | | | | | | |_) |  __/ |  \__ \     :
:    |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  |___/     :
:     ____ _           _ _                           :
:    / ___| |__   __ _| | | ___ _ __   __ _  ___     :
:   | |   | '_ \ / _` | | |/ _ \ '_ \ / _` |/ _ \    :
:   | |___| | | | (_| | | |  __/ | | | (_| |  __/    :
:    \____|_| |_|\__,_|_|_|\___|_| |_|\__, |\___|    :
:                                     |___/          :
······················································
"""
  )


def secondary_title():
  clear_screen()
  print(
"""······················································
: ┌┐┌┬ ┬┌┬┐┌┐ ┌─┐┬─┐┌─┐  ┌─┐┬ ┬┌─┐┬  ┬  ┌─┐┌┐┌┌─┐┌─┐ :
: ││││ ││││├┴┐├┤ ├┬┘└─┐  │  ├─┤├─┤│  │  ├┤ ││││ ┬├┤  :
: ┘└┘└─┘┴ ┴└─┘└─┘┴└─└─┘  └─┘┴ ┴┴ ┴┴─┘┴─┘└─┘┘└┘└─┘└─┘ :
······················································
"""
  )


def print_instructions():
  print('-=-'*18)
  print(
f"""
  \033[1mINSTRUCTIONS\033[m

  Welcome to Numbers Challenge! Your goal is to  
  figure out the correct sequence of numbers  
  generated randomly by the program. The game will  
  only tell you \033[1mhow many numbers are in the correct  
  position\033[m.  

  \033[1mRULES:\033[m
  1. Choose a difficulty level from the main menu:  
    - \033[32mEasy\033[m: Sequence of {EASY} numbers.  
    - \033[33mMedium\033[m: Sequence of {MEDIUM} numbers.  
    - \033[31mHard\033[m: Sequence of {HARD} numbers.  
  2. For each attempt, enter a sequence of numbers  
    matching the length of the chosen difficulty.  
  3. The game will check your guess and tell you  
    \033[1mhow many numbers are in the correct position\033[m.  
  4. Keep trying until you guess the entire sequence  
    in the correct order.  

  \033[1mCONTROLS:\033[m
  - Use the "↑" and "↓" keys to navigate the menus.  
  - Press "Enter" to confirm your selection.  
  - During the game, press "Enter" to open the pause  
    menu.  

  \033[1mTIPS:\033[m
  - Test different combinations of numbers to figure  
    out their correct positions.  
  - Use the game's feedback to refine your guesses.  

  \033[1mGood luck and have fun!\033[m
"""
)
  print('-=-'*18)
  print()


def print_difficultys():
  diff_levels = {
    EASY: '\033[32mEasy\033[m',
    MEDIUM: '\033[33mMedium\033[m',
    HARD: '\033[31mHard\033[m'
  }

  print('-=-'*18)
  print(
f"""
             Easy   = Sequence of \033[1m{EASY}\033[m numbers
             Medium = Sequence of \033[1m{MEDIUM}\033[m numbers 
             Hard   = Sequence of \033[1m{HARD}\033[m numbers
"""
)
  difficulty = diff_levels.get(len(numbers))
  print(f'               Currently difficulty: {difficulty}')
  print('-=-'*18)
  print()


def print_scoreboard():
  print('-=-'*18)
  print('The numbers were: ', end='')
  for i, number in enumerate(numbers):
    print(number, end='')
  print()
  print(
f"""
Congratulations! You win with {attempts} attempts!
"""
)
  print('-=-'*18)
  print()


def clear_screen():
  system('cls' if name == 'nt' else 'clear')


def draw_numbers(difficulty):
  global numbers
  numbers = []
  for i in range(difficulty):
    numbers.append(randint(0,9))
    if i == difficulty - 1:
      print(numbers[i])
    else:
      print(numbers[i], end='')


def print_menu(menu, selected):
  if not menu == MAIN_MENU:
    secondary_title()
    if menu == INSTRUCTIONS_MENU:
      print_instructions()
    elif menu == DIFF_MENU:
      print_difficultys()
    elif menu == SECONDARY_MENU:
      print_scoreboard()
  else:
    main_title()
  
  print(f'{menu[-1]:=^54}')
  for i, option in enumerate(menu):
    if i == selected:
      print(f'\033[1m  {option:^50}  \033[m')
    elif not i == len(menu) - 1:
      print(f'  {option:^50}  ')
  print('='*54)


def get_pressioned_key(menu):
  selected = 0

  print_menu(menu, selected)

  while True:
    event = keyboard.read_event(suppress=True)
    if event.event_type == 'down':
      size = len(menu) - 1
      if event.name == 'up':
        selected = (selected - 1) % size
        print_menu(menu, selected)
      elif event.name == 'down':
        selected = (selected + 1) % size
        print_menu(menu, selected)
      elif event.name == 'enter':
        return menu[selected]


def choice_processement(choice):
  global attempts, guesses, corrects
  menus = {
    'main': MAIN_MENU,
    'difficulty': DIFF_MENU,
    'secondary': SECONDARY_MENU,
    'instructions': INSTRUCTIONS_MENU,
    'pause': PAUSE_MENU
  }

  for name, menu in menus.items():
    if choice in menu:
      which_menu = name
      break

  if which_menu == 'main':
    if choice == 'Play game':
      if len(numbers) == EASY:
        draw_numbers(EASY)
      elif len(numbers) == MEDIUM:
        draw_numbers(MEDIUM)
      elif len(numbers) == HARD:
        draw_numbers(HARD)

      attempts = 0
      guesses = []
      corrects = []
      play_game()
      return
    
    elif choice == 'Choose difficulty':
      choice = get_pressioned_key(DIFF_MENU)
      return choice_processement(choice)
    
    elif choice == 'Instructions':
      choice = get_pressioned_key(INSTRUCTIONS_MENU)
      return choice_processement(choice)
    
    elif choice == 'Exit game':
      main_title()
      print('See you soon!')
      return

  elif which_menu == 'difficulty':
    if choice == 'Easy':
      draw_numbers(EASY)
      choice = get_pressioned_key(DIFF_MENU)
      return choice_processement(choice)
    
    elif choice == 'Medium':
      draw_numbers(MEDIUM)
      choice = get_pressioned_key(DIFF_MENU)
      return choice_processement(choice)
    
    elif choice == 'Hard':
      draw_numbers(HARD)
      choice = get_pressioned_key(DIFF_MENU)
      return choice_processement(choice)
    
    elif choice == 'Back to Main Menu':
      choice = get_pressioned_key(MAIN_MENU)
      return choice_processement(choice)
    
  elif which_menu == 'secondary':
    if choice == 'Play again':

      if len(numbers) == EASY:
        draw_numbers(EASY)
      elif len(numbers) == MEDIUM:
        draw_numbers(MEDIUM)
      elif len(numbers) == HARD:
        draw_numbers(HARD)
      
      guesses = []
      corrects = []
      attempts = 0
      play_game()
      return
      
    elif choice == 'Back to Main Menu':
      choice = get_pressioned_key(MAIN_MENU)
      return choice_processement(choice)
    
    elif choice == ' Leave game ':
      main_title()
      print('Thanks for playing! See you soon!\n')
      return
  
  elif which_menu == 'pause':
    if choice == 'Resume game':
      play_game()
    elif choice == 'Leave game':
      main_title()
      print('The numbers were: ', end='')
      for i, number in enumerate(numbers):
        print(number, end='')
      print('\n')
      print('Thanks for playing! See you soon!\n')
  return


def play_game():
  global attempts, guesses, corrects
  player_choice = ''
  while len(player_choice) < len(numbers): 
    player_choice += '0'

  while True:
    secondary_title()
    print('Press \033[1menter\033[m to \033[1mPAUSE\033[m')
    
    '''for i, number in enumerate(numbers):
      print(number, end='')
    print()'''

    if not attempts == 0:
      print(f'{" GUESSES ":=^54}')
      for i in range(len(guesses)):
        print(f'Guess {i+1}: {guesses[i]}', end=' - ')
        print(f'{corrects[i]} corrects numbers!')
      print('='*54)
    else:
      print('='*54)

    if not len(player_choice) == len(numbers): 
      print(f'Input {player_choice} is invalid. Please try again!')
    
    print('Type here ↴')
    player_choice = str(input(f'Guess {attempts+1}: ')).strip()

    count = 0
    if len(player_choice) == len(numbers):
      guesses.append(player_choice) 
      for i, number in enumerate(numbers):
        if int(player_choice[i]) == number:
          count += 1
      corrects.append(count)
      attempts += 1

    if count == len(numbers):
      choice = get_pressioned_key(SECONDARY_MENU)
      choice_processement(choice)
      return
    
    if player_choice == '':
      choice = get_pressioned_key(PAUSE_MENU)
      choice_processement(choice)
      return


def run():
  main_title()
  draw_numbers(EASY)

  choice = get_pressioned_key(MAIN_MENU)
  choice_processement(choice)


if __name__ == '__main__':
  run()
