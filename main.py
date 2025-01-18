from os import system, name
from random import randint
import keyboard

MAIN_MENU = ('Play game', 'Choose difficulty', 'Instructions', 'Exit game', ' MAIN MENU ')
DIFF_MENU = ('Easy', 'Medium', 'Hard', 'Back to Main Menu', ' CHOOSE DIFFICULTY ')
INSTRUCTIONS_MENU = ('Back to Main Menu', 'Exit game', ' MENU ')
SECONDARY_MENU = ('Play again', 'Back to Main Menu', 'Leave game', ' MENU ')
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
"""
Instructions here!
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
    numbers.append(randint(1,9))
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
    
    elif choice == 'Leave game':
      main_title()
      print('Thanks for playing! See you soon!')
      return
  
  elif which_menu == 'pause':
    play_game()
  return


# def player_attempt():
  


def play_game():
  global attempts, guesses, corrects
  player_choice = ''
  while len(player_choice) < len(numbers): 
    player_choice += '0'

  while True:
    secondary_title()

    for i, number in enumerate(numbers):
      print(number, end='')
    print()

    if not attempts == 0:
      for i in range(len(guesses)):
        print(f'Guess {i+1}: {guesses[i]}', end=' - ')
        print(f'{corrects[i]} corrects numbers!')
      print()

    if not len(player_choice) == len(numbers): 
      print(f'Input {player_choice} is invalid. Please try again!')
    
    
    player_choice = str(input(f'Guess {attempts+1} [Press enter to pause]: ')).strip()

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
      return  # CORRIGIR ISSO

#  DESCOBRIR QUANDO GANHOU / DAR OPÇÃO DE SAIR

def run():
  main_title()
  draw_numbers(EASY)

  choice = get_pressioned_key(MAIN_MENU)
  choice_processement(choice)
  print(numbers)


if __name__ == '__main__':
  run()
