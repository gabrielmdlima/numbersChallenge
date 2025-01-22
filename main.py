from os import system, name
from random import randint
import keyboard

# Constantes para os menus / Menus constants
MAIN_MENU = ('Play game', 'Choose difficulty', 'Instructions', 'Exit game', ' MAIN MENU ')
DIFF_MENU = ('Easy', 'Medium', 'Hard', 'Back to Main Menu', ' CHOOSE DIFFICULTY ')
INSTRUCTIONS_MENU = ('Back to Main Menu', 'Exit game', ' MENU ')
SECONDARY_MENU = ('Play again', 'Back to Main Menu', ' Leave game ', ' MENU ')
PAUSE_MENU = ('Resume game', 'Restart game', 'Back to Main Menu', 'Leave game', ' PAUSE ')
EASY = 4
MEDIUM = 5
HARD = 6

# Classe resposável pelo processamento dos dados usados durante a execução do código
class GameDataProcessesor:
  def __init__(self):
    self.numbers = []
    self.guesses = []
    self.corrects = []
    self.attempts = 0
    self.selected = 0
    self.player_choice = ''
    self.menus = self.set_menus_names()

    self.set_numbers(EASY)

  # Função para gerar os números aleatórios com base na dificuldade / Draws random numbers based on difficulty
  def set_numbers(self, difficulty):
    self.numbers = []
    for _ in range(difficulty):
      self.numbers.append(randint(0, 9))

  # Adiciona a tentativa à lista de palpites. / Adds the attempt to the list of guesses.
  def set_guesses(self, player_choice):
    self.guesses.append(player_choice)

  # Registra o número de acertos da tentativa. / Records the number of correct guesses for the attempt.
  def set_corrects(self, count):
    self.corrects.append(count)

  # Incrementa o contador de tentativas. / Increments the attempts counter.
  def set_attempts(self):
    self.attempts += 1

  # Obtém o nível de dificuldade com base no tamanho da sequência. / Gets the difficulty level based on the sequence length.
  def currently_difficulty(self):
    difficulty_levels = {
      EASY: '\033[32mEasy\033[m',  
      MEDIUM: '\033[33mMedium\033[m',  
      HARD: '\033[31mHard\033[m'  
    }
    return difficulty_levels.get(len(self.numbers))

  # Garante que o tamanho de player_choice seja igual ao da sequência de números. / Ensures that player_choice has the same length as the sequence of numbers.
  def set_player_choice(self):
    if not len(self.numbers) == 0:
      while len(self.player_choice) < len(self.numbers): 
        self.player_choice += '0'

  # Define os menus disponíveis e seus nomes / Defines available menus and their names
  def set_menus_names(self):
    menus = {
      'main': MAIN_MENU,
      'difficulty': DIFF_MENU,
      'secondary': SECONDARY_MENU,
      'instructions': INSTRUCTIONS_MENU,
      'pause': PAUSE_MENU
    }
    return menus
  
  # Reinicia as variáveis usadas no jogo / Reset variables used in the game
  def reset_game_data(self):
    size = len(self.numbers)
    if size == EASY: 
      self.set_numbers(EASY)
    elif size == MEDIUM: 
      self.set_numbers(MEDIUM)
    elif size == HARD: 
      self.set_numbers(HARD)

    self.guesses = []
    self.corrects = []
    self.attempts = 0

# Função para limpar a tela / Clears the screen
def clear_screen():
  system('cls' if name == 'nt' else 'clear')
  
# Função para exibir o título principal / Displays the main title
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

# Função para exibir a tabela de resultados / Displays the scoreboard
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

# Função para exibir instruções do jogo / Displays the game instructions
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
""")
  print('-=-'*18)
  print()

# Função para exibir as dificuldades e a dificuldade atual / Displays difficulty levels and current difficulty
def print_difficultys(data):
  print('-=-'*18)
  print(
f"""
             Easy   = Sequence of \033[1m{EASY}\033[m numbers
             Medium = Sequence of \033[1m{MEDIUM}\033[m numbers 
             Hard   = Sequence of \033[1m{HARD}\033[m numbers
""")
  print(f'               Currently difficulty: {data.currently_difficulty()}')
  print('-=-'*18)
  print()

# Função para exibir a tabela de resultados / Displays the scoreboard
def print_scoreboard(data):
  print('-=-'*18)
  print('The numbers were: ', end='')
  for _, number in enumerate(data.numbers):
    print(number, end='')
  print()
  print(
f"""
Congratulations! You win with {data.attempts} attempts!
""")
  print('-=-'*18)
  print()

# Função para exibir os menus e a seleção do usuário / Displays menus and handles user selection
def print_menu(data, menu):
  if not menu == MAIN_MENU:
    secondary_title()
    if menu == INSTRUCTIONS_MENU:
      print_instructions()
    elif menu == DIFF_MENU:
      print_difficultys(data)
    elif menu == SECONDARY_MENU:
      print_scoreboard(data)
  else:
    main_title()
    print(f'{"↑ and ↓ keys to navigate.":^54}')

  print(f'{menu[-1]:=^54}')

  for i, option in enumerate(menu):
    if i == data.selected:
      option = (f'\033[7;1;40m {option:^17} \033[m')  
      print(f'        {option:^50}  ')  
    elif not i == len(menu) - 1:
      option = (f'{option:^17}')
      print(f'  {option:^50}  ')  

  print('='*54)

# Função para capturar a entrada do teclado / Function to capture keyboard input
def get_pressioned_key(data, menu):

  # Exibe o menu inicial com a primeira opção selecionada / Displays the initial menu with the first option selected
  print_menu(data, menu)

  size = len(menu) - 1

  while True:
    event = keyboard.read_event(suppress=True)
    if event.event_type == 'down':
      if event.name == 'up':
        data.selected = (data.selected - 1) % size
        print_menu(data, menu)
      elif event.name == 'down':
        data.selected = (data.selected + 1) % size
        print_menu(data, menu)
      elif event.name == 'enter':
        return menu[data.selected]

# Função para processar a escolha do menu / Processes menu selection
def choice_processement(data, choice):
  
  # Verifica qual menu contém a escolha feita / Checks which menu contains the user's choice
  for name, menu in data.menus.items():
    if choice in menu:
      which_menu = name
      break

  # Lógica para o menu principal / Logic for the main menu
  if which_menu == 'main':
    if choice == 'Play game':
      data.reset_game_data()
      play_game(data)
      return
    
    elif choice == 'Choose difficulty':
      data.selected = 0
      choice = get_pressioned_key(data, DIFF_MENU)
      return choice_processement(data, choice)
    
    elif choice == 'Instructions':
      data.selected = 0
      choice = get_pressioned_key(data, INSTRUCTIONS_MENU)
      return choice_processement(data, choice)
    
    elif choice == 'Exit game':
      main_title()
      print('See you soon!')
      return

  # Lógica para o menu de dificuldades / Logic for the difficulty menu
  elif which_menu == 'difficulty':
    if choice == 'Easy':
      data.set_numbers(EASY)
      choice = get_pressioned_key(data, DIFF_MENU)
      return choice_processement(data, choice)
    
    elif choice == 'Medium':
      data.set_numbers(MEDIUM)
      choice = get_pressioned_key(data, DIFF_MENU)
      return choice_processement(data, choice)
    
    elif choice == 'Hard':
      data.set_numbers(HARD)
      choice = get_pressioned_key(data, DIFF_MENU)
      return choice_processement(data, choice)
    
    elif choice == 'Back to Main Menu':
      data.selected = 0
      choice = get_pressioned_key(data, MAIN_MENU)
      return choice_processement(data, choice)

  # Lógica para o menu secundário / Logic for the secondary menu
  elif which_menu == 'secondary':
    if choice == 'Play again':
      data.reset_game_data()
      play_game(data)
      return
    
    elif choice == ' Leave game ':
      main_title()
      print('Thanks for playing! See you soon!\n')
      return

  # Lógica para o menu de pausa / Logic for the pause menu
  elif which_menu == 'pause':
    if choice == 'Resume game':
      play_game(data)

    elif choice == 'Leave game':
      main_title()
      print('The numbers were: ', end='')
      for _, number in enumerate(data.numbers):
        print(number, end='')
      print('\n')
      print('Thanks for playing! See you soon!\n')
    
    elif choice == 'Restart game':
      data.reset_game_data()
      play_game(data)
      return

# Função para rodar o jogo principal / Runs the main game logic
def play_game(data):
  data.set_player_choice()
  sugestion = data.player_choice

  while True:
    secondary_title()
    # Mostra o nível de dificuldade atual. / Shows the current difficulty level.
    print(f'Difficulty: {data.currently_difficulty()}')
    print(f'Sequence lenght: \033[1m{len(data.numbers)} digits\033[m')
    
    print('Press \033[1menter\033[m to \033[1mPAUSE\033[m')

    # Debug opcional: Exibe os números gerados. / Optional debug: Displays the generated numbers.
    '''for _, number in enumerate(data.numbers):
      print(number, end='')
    print()'''

    # Exibe todas as tentativas anteriores, caso o jogador já tenha feito alguma. / Displays all previous attempts if the player has made any.
    if not data.attempts == 0:
      print(f'{" GUESSES ":=^54}')
      for i in range(len(data.guesses)):
        print(f'Guess {i+1:2}: {data.guesses[i]}', end=' - ')
        print(f'{data.corrects[i]} corrects numbers!')
    print('='*54)

    while True:
      # Valida se o input do jogador tem o tamanho correto. / Validates if the player's input has the correct length.
      if not len(data.player_choice) == len(data.numbers):
        print(f"Input '{data.player_choice}' is invalid. Please try a {len(data.numbers)}-numbers sequence!\n")

      print(f"Type here ↴ Try '{sugestion}'" if data.attempts == 0 else 'Type here ↴')
      data.player_choice = str(input(f'Guess {data.attempts+1:2}: ')).strip()  # Solicita ao jogador que insira sua tentativa. / Asks the player to input their guess.

      # Verifica se o jogador pressionou "Enter" para abrir o menu de pausa. / Checks if the player pressed "Enter" to open the pause menu.
      if data.player_choice == '':
        data.selected = 0
        choice = get_pressioned_key(data, PAUSE_MENU)
        choice_processement(data, choice)
        return
      else:
        break

    count = 0  # Inicializa o contador de números corretos para cada tentativa. / Initializes the correct number counter for each attempt.
    if len(data.player_choice) == len(data.numbers):
      data.guesses.append(data.player_choice)  # Adiciona a tentativa à lista de palpites. / Adds the attempt to the list of guesses.
      for i, number in enumerate(data.numbers):
        if int(data.player_choice[i]) == number:
          count += 1
      data.corrects.append(count)  # Registra o número de acertos da tentativa. / Records the number of correct guesses for the attempt.
      data.set_attempts()  # Incrementa o contador de tentativas. / Increments the attempts counter.

      # Se todos os números estiverem corretos, o jogador venceu. / If all numbers are correct, the player has won.
    if count == len(data.numbers):
      data.selected = 0
      choice = get_pressioned_key(data, SECONDARY_MENU)
      choice_processement(data, choice)
      return


# Função que executa o jogo / Function that runs the game
def run(data):
  main_title()

  # Chama o menu principal e processa a escolha do jogador / Calls the main menu and processes the player's choice
  choice = get_pressioned_key(data, MAIN_MENU)
  choice_processement(data, choice)

# Ponto de entrada do programa / Program entry point
if __name__ == '__main__':
  data = GameDataProcessesor()
  run(data)
