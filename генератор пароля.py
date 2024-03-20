from string import *
from random import *

def is_digit():
    if count.isdigit() and len_passw.isdigit():
        return True
    else:
        return False

def is_yes_or_no():
    if dig_need.lower() not in ['y', 'n'] or big_alpha_need.lower() not in ['y', 'n'] or small_alpha_need.lower() not in ['y', 'n'] or punctuation_need.lower() not in ['y', 'n']:
        return False
    else:
        True

def password():
    l_passw = []
    for _ in range(int(count)):
        password = ''
        for i in range(1, int(len_passw) + 1):
            password += choice(char)
        l_passw.append(password)
    return l_passw

l_simw = [digits, ascii_uppercase, ascii_lowercase, punctuation]
l_ques = []

count = input('Введите необходимое количество сгенерированных паролей: ')
len_passw = input('Введите необходимую длину пароля: ')
dig_need = input('Включать цифры в пароль? (y/n) ')
l_ques.append(dig_need)
big_alpha_need = input('Включать заглавные буквы в пароль? (y/n) ')
l_ques.append(big_alpha_need)
small_alpha_need = input('Включать строчные буквы в пароль? (y/n) ')
l_ques.append(small_alpha_need)
punctuation_need = input('Включать знаки пунктуации в пароль? (y/n) ')
l_ques.append(punctuation_need)

char = ''

while is_digit() == False:
    print('Ало, цифры надо вводить')
    if not count.isdigit():
        count = input('Введите необходимое количество сгенерированных паролей ')
    if not len_passw.isdigit():
        len_passw = input('Введите необходимую длину пароля: ')

while is_yes_or_no() == False:
    print('Ало, нужно вводить только y или n')
    if dig_need.lower() not in ['y', 'n']:
        dig_need = input('Включать цифры в пароль? (y/n) ')
        l_ques[0] = dig_need
    if big_alpha_need.lower() not in ['y', 'n']:
        big_alpha_need = input('Включать заглавные буквы в пароль? (y/n) ')
        l_ques[1] = big_alpha_need
    if small_alpha_need.lower() not in ['y', 'n']:
        small_alpha_need = input('Включать строчные буквы в пароль? (y/n) ')
        l_ques[2] = small_alpha_need
    if punctuation_need.lower() not in ['y', 'n']:
        punctuation_need = input('Включать знаки пунктуации в пароль? (y/n) ')
        l_ques[3] = punctuation_need

for i in l_ques:
    if i.lower() == 'y':
        char += l_simw[l_ques.index(i)]
        l_ques[l_ques.index(i)] = 'n'

print(*password(), sep='\n')
