import random

HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 0   |
     |
     |
    ===''', '''
 +---+
 0   |
 |   |
     |
    ===''', '''
 +---+
 0   |
/|   |
     |
    ===''', '''
 +---+
 0   |
/|\  |
     |
    ===''', '''
 +---+
 0   |
/|\  |
/    |
    ===''', '''
 +---+
 0   |
/|\  |
/ \  |
    ===''', '''
 +---+
[0   |
/|\  |
/ \  |
    ===    
    ''', '''
 +---+
[0]  |
/|\  |
/ \  |
    ===    
    ''']

words = {'Цвета': 'красный оранжевый желтый зеленый синий голубой фиолетовый белый черный коричневый'.split(),
         'Фигуры': 'квадрат треугольник прямоугольник круг эллипс ромб трапеция параллелограмм '
                   'пятиугольник шестиугольник восьмиугольник'.split(),
         'Фрукты': 'яблоко апельсин лимон лайм груша мандарин виноград грейпфрут персик '
                   'банан абрикос манго банан нектарин'.split(),
         'Животные': 'аист бабуин баран барсук бык волк зебра кит коза корова кошка кролик '
                     'крыса лев лиса лось медведь мул '
                     'мышь норка носорог обезьяна овца олень осел панда пума скунс собака сова '
                     'тигр тюлень хорек ящерица'.split()
         }


def get_random_word(word_dict):
    word_key = random.choice(list(word_dict.keys()))

    word_index = random.randint(0, len(word_dict) - 1)
    return word_dict[word_key][word_index]


def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    print("Ошибочные буквы:", end=" ")

    for letter in missed_letters:
        print(letter, end=" ")
    print()

    blanks = "_" * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=" ")
    print()


def get_guess(already_guessed):
    while True:
        guess = input("Введите букву: ").lower()

        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in already_guessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ.')
        else:
            return guess


def play_again():
    print("Хотите сыграть еще? (да или нет)")
    return input().lower().startswith("д")


print('В И С Е Л И Ц А')

difficulty = ""
while difficulty not in "ЛСТ":
    print("Выберите уровень сложности: Л - Легкий, С - Средний, Т - Тяжелый")
    difficulty = input().upper()
if difficulty == "С":
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == "Т":
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missed_letters = ''
correct_letters = ''
secret_word = get_random_word(words)
game_is_done = False

while True:
    display_board(missed_letters, correct_letters, secret_word)

    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess

        found_all_letters = True

        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break

        if found_all_letters:
            print(f"ДА! Секретное слово - {secret_word}! Вы угадали!")
            game_is_done = True
    else:
        missed_letters = missed_letters + guess

        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            display_board(missed_letters, correct_letters, secret_word)
            print('Вы исчерпали все попытки!\nНе угадано букв: ' + str(len(missed_letters)) + ' и угадано букв: ' + str(
                len(correct_letters)) + '. Было загадано слово "' + secret_word + '".')
            game_is_done = True

    if game_is_done:

        if play_again():
            missed_letters = ""
            correct_letters = ""
            game_is_done = False
            secret_word = get_random_word(words)
        else:
            break
