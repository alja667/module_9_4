import os
import random

first = 'Мама мыла раму'
second = 'Рамена мало было'




result = list(map(lambda x,y:x in y, first, second))
print(result)


def get_advanced_writer(file_name):
    file= open(file_name, 'a', encoding = 'utf-8')
    def  write_everything(*data_set):
        word = data_set
        for i in word:
            file.write(f'{i}\n')
        file.close()

    return write_everything

from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__ (self):
        return random.choice(self.words)



first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


