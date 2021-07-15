#!/usr/bin/env python3

import random

num_quantity = 3    #digits
max_attempt = 5    #guess

def getSecretNum():

    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(num_quantity):
        secretNum += str(numbers[i])
        #print(secretNum)
    return secretNum

def getClues(attempt, secretNum):

    if attempt == secretNum:
        return 'Вы угадали!'
    
    clues = []
    for i in range(len(attempt)):
        if attempt[i] == secretNum[i]:
            clues.append('Горячо')
        elif attempt[i] in secretNum:
            clues.append('Тепло')
        elif attempt[i] not in secretNum:
            clues.append('Холодно')
        if len(clues) == 0:
            clues.append('Холодно')

    clues
    return ' '.join(clues)

def isOnlyQuantity(num):

    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
        return True

print('Я загадаю %s-х значное число, которое вы должны отгадать.' % (num_quantity))
print('Я дам несколько подсказок...')
print('Когда я говорю:')
print(' Холодно - Ни одна цифра не отгадана.')
print(' Тепло - Одна цифра отгадана, но не отгадана ее позиция.')
print(' Горячо - Одна цифра и ее позиция отгаданы.')

while True:
    secretNum = getSecretNum()
    print('Итак, я загадал число. У вас есть %s попыток, чтобы отгадать его.\n' % (max_attempt))

    attemptTaken = 1
    while attemptTaken <= max_attempt:
        attempt = ''
        while len(attempt) != num_quantity or not isOnlyQuantity(attempt):
            print('Попытка №%s: ' %(attemptTaken))
            attempt = input()

        print(getClues(attempt, secretNum))
        attemptTaken += 1

        if attempt == secretNum:
            break
        if attemptTaken > max_attempt:
            print('Попыток больше не осталось. Я загадал число %s.' % (secretNum))
        
    print('Хотите сыграть еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        break
