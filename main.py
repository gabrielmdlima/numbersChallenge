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

# Variáveis globais / Global variables
global numbers, attempts
global guesses
global corrects
numbers = []
guesses = []
corrects = []
attempts = 0

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

# Função para exibir o título secundário / Displays the secondary title
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
"""
)
  print('-=-'*18)
  print()

# Função para exibir as dificuldades e a dificuldade atual / Displays difficulty levels and current difficulty
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

# Função para exibir a tabela de resultados / Displays the scoreboard
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

# Função para limpar a tela / Clears the screen
def clear_screen():
  system('cls' if name == 'nt' else 'clear')

# Função para gerar os números aleatórios com base na dificuldade / Draws random numbers based on difficulty
def draw_numbers(difficulty):
  global numbers
  numbers = []
  for i in range(difficulty):
    numbers.append(randint(0,9))

# Função para exibir os menus e a seleção do usuário / Displays menus and handles user selection
def print_menu(menu, selected):
  # Verifica se o menu atual não é o menu principal / Checks if the current menu is not the main menu
  if not menu == MAIN_MENU:
    secondary_title()  # Exibe o título secundário para menus secundários / Displays a secondary title for secondary menus

    # Verifica qual menu está sendo exibido e chama a função correspondente / Checks which menu is being displayed and calls the appropriate function
    if menu == INSTRUCTIONS_MENU:
      print_instructions()  # Exibe as instruções / Displays the instructions
    elif menu == DIFF_MENU:
      print_difficultys()  # Exibe as dificuldades disponíveis / Displays the available difficulty levels
    elif menu == SECONDARY_MENU:
      print_scoreboard()  # Exibe o placar / Displays the scoreboard
  else:
    main_title()  # Exibe o título principal para o menu principal / Displays the main title for the main menu
  
  # Exibe o título do menu com bordas formatadas / Displays the menu title with formatted borders
  print(f'{menu[-1]:=^54}')
  
  # Itera sobre as opções do menu / Iterates through the menu options
  for i, option in enumerate(menu):
    if i == selected:  
      # Formata a opção selecionada com destaque / Formats the selected option with a highlight
      option = (f'\033[7;1;40m {option:^17} \033[m')  
      print(f'        {option:^50}  ')  # Centraliza a opção selecionada / Centers the selected option
    elif not i == len(menu) - 1:  
      # Formata as opções não selecionadas normalmente / Formats non-selected options normally
      option = (f'{option:^17}')
      print(f'  {option:^50}  ')  # Centraliza a opção não selecionada / Centers the non-selected option
  
  # Exibe a linha final de separação do menu / Displays the final menu separator line
  print('='*54)


# Função para capturar a entrada do teclado / Function to capture keyboard input
def get_pressioned_key(menu):
  selected = 0  # Índice do item atualmente selecionado no menu / Index of the currently selected menu item

  # Exibe o menu inicial com a primeira opção selecionada / Displays the initial menu with the first option selected
  print_menu(menu, selected)

  # Loop para capturar eventos do teclado / Loop to capture keyboard events
  while True:
    event = keyboard.read_event(suppress=True)  # Lê um evento de teclado e suprime sua propagação / Reads a keyboard event and suppresses its propagation
    if event.event_type == 'down':  # Verifica se a tecla foi pressionada / Checks if a key was pressed
      size = len(menu) - 1  # Obtém o índice máximo baseado no tamanho do menu / Gets the maximum index based on the menu size
      
      # Navega para cima no menu / Navigates up in the menu
      if event.name == 'up':  
        selected = (selected - 1) % size  # Atualiza o índice selecionado para o item acima, com wrap-around / Updates the selected index to the item above, with wrap-around
        print_menu(menu, selected)  # Atualiza a exibição do menu com o novo índice selecionado / Updates the menu display with the new selected index

      # Navega para baixo no menu / Navigates down in the menu
      elif event.name == 'down':  
        selected = (selected + 1) % size  # Atualiza o índice selecionado para o item abaixo, com wrap-around / Updates the selected index to the item below, with wrap-around
        print_menu(menu, selected)  # Atualiza a exibição do menu com o novo índice selecionado / Updates the menu display with the new selected index

      # Retorna a opção selecionada quando 'Enter' é pressionado / Returns the selected option when 'Enter' is pressed
      elif event.name == 'enter':  
        return menu[selected]  # Retorna o item do menu correspondente ao índice selecionado / Returns the menu item corresponding to the selected index


# Função para iniciar o jogo / Starts the game
def start_game():
  global attempts, guesses, corrects  # Declara as variáveis globais que serão usadas / Declares global variables to be used

  # Verifica o tamanho da lista 'numbers' e define a dificuldade apropriada
  # Checks the size of the 'numbers' list and sets the appropriate difficulty
  if len(numbers) == EASY:  # Caso seja "Fácil" / If it's "Easy"
    draw_numbers(EASY)
  elif len(numbers) == MEDIUM:  # Caso seja "Médio" / If it's "Medium"
    draw_numbers(MEDIUM)
  elif len(numbers) == HARD:  # Caso seja "Difícil" / If it's "Hard"
    draw_numbers(HARD)
  
  # Inicializa as variáveis usadas no jogo / Initializes variables used in the game
  guesses = []  # Lista para armazenar as tentativas do jogador / List to store player guesses
  corrects = []  # Lista para armazenar o número de acertos por tentativa / List to store the number of correct guesses per attempt
  attempts = 0  # Reseta o número de tentativas para 0 / Resets the number of attempts to 0

  # Inicia o loop principal do jogo / Starts the main game loop
  play_game()


# Função para processar a escolha do menu / Processes menu selection
def choice_processement(choice):
  # Define os menus disponíveis e seus nomes / Defines available menus and their names
  menus = {
    'main': MAIN_MENU,
    'difficulty': DIFF_MENU,
    'secondary': SECONDARY_MENU,
    'instructions': INSTRUCTIONS_MENU,
    'pause': PAUSE_MENU
  }

  # Verifica qual menu contém a escolha feita / Checks which menu contains the user's choice
  for name, menu in menus.items():
    if choice in menu:
      which_menu = name
      break

  # Lógica para o menu principal / Logic for the main menu
  if which_menu == 'main':
    if choice == 'Play game':  # Inicia o jogo / Starts the game
      start_game()
      return
    
    elif choice == 'Choose difficulty':  # Abre o menu de dificuldades / Opens the difficulty menu
      choice = get_pressioned_key(DIFF_MENU)
      return choice_processement(choice)
    
    elif choice == 'Instructions':  # Mostra o menu de instruções / Displays the instructions menu
      choice = get_pressioned_key(INSTRUCTIONS_MENU)
      return choice_processement(choice)
    
    elif choice == 'Exit game':  # Encerra o jogo / Exits the game
      main_title()
      print('See you soon!')
      return

  # Lógica para o menu de dificuldades / Logic for the difficulty menu
  elif which_menu == 'difficulty':
    if choice == 'Easy':  # Seleciona dificuldade "Fácil" / Selects "Easy" difficulty
      draw_numbers(EASY)
      choice = get_pressioned_key(DIFF_MENU)
      return choice_processement(choice)
    
    elif choice == 'Medium':  # Seleciona dificuldade "Média" / Selects "Medium" difficulty
      draw_numbers(MEDIUM)
      choice = get_pressioned_key(DIFF_MENU)
      return choice_processement(choice)
    
    elif choice == 'Hard':  # Seleciona dificuldade "Difícil" / Selects "Hard" difficulty
      draw_numbers(HARD)
      choice = get_pressioned_key(DIFF_MENU)
      return choice_processement(choice)
    
    elif choice == 'Back to Main Menu':  # Retorna ao menu principal / Returns to the main menu
      choice = get_pressioned_key(MAIN_MENU)
      return choice_processement(choice)
    
  # Lógica para o menu secundário / Logic for the secondary menu
  elif which_menu == 'secondary':
    if choice == 'Play again':  # Reinicia o jogo / Restarts the game
      start_game()
      return
      
    elif choice == 'Back to Main Menu':  # Retorna ao menu principal / Returns to the main menu
      choice = get_pressioned_key(MAIN_MENU)
      return choice_processement(choice)
    
    elif choice == ' Leave game ':  # Encerra o jogo / Exits the game
      main_title()
      print('Thanks for playing! See you soon!\n')
      return
  
  # Lógica para o menu de pausa / Logic for the pause menu
  elif which_menu == 'pause':
    if choice == 'Resume game':  # Retoma o jogo / Resumes the game
      play_game()
    
    elif choice == 'Leave game':  # Sai do jogo / Exits the game
      main_title()
      print('The numbers were: ', end='')
      for i, number in enumerate(numbers):
        print(number, end='')
      print('\n')
      print('Thanks for playing! See you soon!\n')
    
    elif choice == 'Restart game':  # Reinicia o jogo / Restarts the game
      start_game()
      return
  return



# Função para rodar o jogo principal / Runs the main game logic
def play_game():
  global attempts, guesses, corrects
  player_choice = ''  # Inicializa a escolha do jogador como uma string vazia. / Initializes the player's choice as an empty string.
  while len(player_choice) < len(numbers): 
    player_choice += '0'  # Garante que o tamanho de player_choice seja igual ao da sequência de números. / Ensures that player_choice has the same length as the sequence of numbers.

  diff_levels = {  
    EASY: '\033[32mEasy\033[m',  
    MEDIUM: '\033[33mMedium\033[m',  
    HARD: '\033[31mHard\033[m'  
  }  
  difficulty = diff_levels.get(len(numbers))  # Obtém o nível de dificuldade com base no tamanho da sequência. / Gets the difficulty level based on the sequence length.

  while True:
    secondary_title()  # Exibe o título secundário da tela. / Displays the secondary title of the screen.
    print(f'Difficulty: {difficulty}')  # Mostra o nível de dificuldade atual. / Shows the current difficulty level.
    print('Press \033[1menter\033[m to \033[1mPAUSE\033[m')  # Informa que o jogador pode pausar pressionando "Enter". / Tells the player they can pause by pressing "Enter".

    '''for i, number in enumerate(numbers):
      print(number, end='')  # Debug opcional: Exibe os números gerados. / Optional debug: Displays the generated numbers.
    print()'''

    if not attempts == 0:  
      # Exibe todas as tentativas anteriores, caso o jogador já tenha feito alguma. / Displays all previous attempts if the player has made any.
      print(f'{" GUESSES ":=^54}')  
      for i in range(len(guesses)):  
        print(f'Guess {i+1:2}: {guesses[i]}', end=' - ')  # Mostra o número da tentativa e o palpite. / Shows the attempt number and the guess.
        print(f'{corrects[i]} corrects numbers!')  # Mostra quantos números estão corretos. / Shows how many numbers are correct.  
      print('='*54)  
    else:
      print('='*54)  # Exibe uma linha separadora se ainda não houver tentativas. / Displays a separator line if no attempts have been made.

    if not len(player_choice) == len(numbers):  
      # Valida se o input do jogador tem o tamanho correto. / Validates if the player's input has the correct length.
      print(f'Input {player_choice} is invalid. Please try again!')  

    print('Type here ↴')  
    player_choice = str(input(f'Guess {attempts+1:2}: ')).strip()  
    # Solicita ao jogador que insira sua tentativa. / Asks the player to input their guess.

    count = 0  # Inicializa o contador de números corretos para cada tentativa. / Initializes the correct number counter for each attempt.
    if len(player_choice) == len(numbers):  
      guesses.append(player_choice)  # Adiciona a tentativa à lista de palpites. / Adds the attempt to the list of guesses.
      for i, number in enumerate(numbers):  
          if int(player_choice[i]) == number:  
              count += 1  # Conta os números na posição correta. / Counts the numbers in the correct position.  
      corrects.append(count)  # Registra o número de acertos da tentativa. / Records the number of correct guesses for the attempt.
      attempts += 1  # Incrementa o contador de tentativas. / Increments the attempts counter.

    if count == len(numbers):  
      # Se todos os números estiverem corretos, o jogador venceu. / If all numbers are correct, the player has won.
      choice = get_pressioned_key(SECONDARY_MENU)  # Exibe o menu secundário. / Displays the secondary menu.
      choice_processement(choice)  # Processa a escolha do jogador. / Processes the player's choice.
      return  # Sai da função. / Exits the function.

    if player_choice == '':  
      # Verifica se o jogador pressionou "Enter" para abrir o menu de pausa. / Checks if the player pressed "Enter" to open the pause menu.
      choice = get_pressioned_key(PAUSE_MENU)  # Exibe o menu de pausa. / Displays the pause menu.
      choice_processement(choice)  # Processa a escolha do jogador. / Processes the player's choice.
      return  # Sai da função. / Exits the function.

# Função que executa o jogo.
# Function that runs the game.
def run():
  main_title()
  draw_numbers(EASY)

  # Chama o menu principal e processa a escolha do jogador.
  # Calls the main menu and processes the player's choice.
  choice = get_pressioned_key(MAIN_MENU)
  choice_processement(choice)


# Ponto de entrada do programa.
# Program entry point.
if __name__ == '__main__':
  run()
