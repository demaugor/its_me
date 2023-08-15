import random

attempts_list = []


def show_score():
    if not attempts_list:
        print('В настоящее время нет ни одного высокого числа,'
              ' Выбери своё число')

    else:
        print(f'Текущие число равно'
              f' {min(attempts_list)} attempts')


def start_game():
    attempts = 0
    rand_num = random.randint(1, 10)
    print('Привет! Добропожаловать в игру!')
    player_name = input('Как твоё имя? ')
    wanna_play = input(
        f'Ку, {player_name}, хочешь сыграть '
        f't в игру? (Enter да/нет): ')

    if wanna_play.lower() != 'да':
        print('Это круто, спасибо')
        exit()
    else:
        show_score()

    while wanna_play.lower() == 'да':
        try:
            guess = int(input('Выберите число от 1 до 10 '))
            if guess < 1 or guess > 10:
                raise ValueError(
                    'Please guess a number within the given range')

            attempts += 1
            attempts_list.append(attempts)

            if guess == rand_num:
                print('Мило! У тебя получилось!')
                print(f'Это потребовало от вас {attempts} попыток')
                wanna_play = input(
                    'Хотели бы вы поиграть еще раз? (Введите Да/Нет): ')
                if wanna_play.lower() != 'да':
                    print('Это круто, приятного просмотра!')
                    break
                else:
                    attempts = 0
                    rand_num = random.randint(1, 10)
                    show_score()
                    continue
            else:
                if guess > rand_num:
                    print('число ниже')
                elif guess < rand_num:
                    print('число выше')

        except ValueError as err:
            print('О нет!, это недопустимое значение. Пробовать снова...')
            print(err)


if __name__ == '__main__':
    start_game()