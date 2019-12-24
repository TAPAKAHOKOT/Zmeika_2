import turtle as tt
import numpy as np
import math as m
import json

# Объект голова змеи


class Head:
    # Инициализация переменных
    def __init__(self, border_size, cols):
        # Перо прорисовки головы змеи
        self.dwr = tt.Turtle()
        self.dwr.speed(0)
        self.dwr.color("White")
        # Перо прорисовки хвоста змеии
        self.tail = tt.Turtle()
        self.tail.speed(0)
        self.tail.hideturtle()
        self.tail.color("White")

        self.border_size = border_size
        self.colors = cols

        self.angle = 0
        # Скорость движения и поворота змеи
        self.speed = 3
        self.rotation_speed = 7

        self.right = False
        self.left = False

        self.border_x = True
        self.border_y = True

        self.tail_len = 1
        self.game_score = 0
        # Создание листа с координатами хвоста змеи
        self.arr = [[0, 0]] * self.tail_len * 3

    # Прорисовка змеи
    def draw(self):
        # Изменение координат хвоста змеи
        for i in range(1, len(self.arr)):
            self.arr[-i] = self.arr[-i - 1]
        self.arr[0] = self.dwr.pos()

        # перемещение пера в конец хвоста
        self.tail.clear()
        self.tail.up()
        self.tail.goto(self.arr[-1])
        self.tail.down()

        # проверка на пересечение головы змеи и хвоста
        r = 4
        for k in self.arr[5:]:
            if k[0] - r < self.dwr.pos()[0] < k[0] + r and\
                    k[1] - r < self.dwr.pos()[1] < k[1] + r and self.game_score != 0:
                # Game Over
                # Вытаскиваем данные о рекорде из json файла
                with open("data.json", "a") as f:
                    f.close()
                with open("data.json", "r") as f:
                    try:
                        data = json.loads(f.read())
                    except:
                        data = self.game_score
                    f.close()

                # Сравнение рекорда и счета
                if data < self.game_score:
                    data = self.game_score

                    # Запись в json файл нового рекорда
                    with open("data.json", "w") as f:
                        json.dump(data, f)
                        f.close()
                # Сообщение о поражении
                print("-" * 15 + "You Loooose'r" + "-" * 15)
                print("___Your score is %s___" % self.game_score)
                print(">>>Best score is %s<<<" % data)
                print("-" * (30 + len("You Loooose'r")) + "\n")
                self.remove_tail()

        # прорисовка хвоста змеи
        for i, k in enumerate(self.arr[::-3]):
            if i < 10:
                self.tail.color("#" + ("%X" % (15 - i)) * 6)
            self.tail.goto(k)

        self.tail.goto(self.arr[0])

        # Передвижение головы хмеи
        self.dwr.up()
        self.dwr.setheading(self.angle)
        self.dwr.fd(self.speed)

        # Отскок змеи от границ экрана
        if (self.border_size < self.dwr.pos()[0] or -self.border_size > self.dwr.pos()[0]) and self.border_x:
            self.border_x = False
            self.angle = 180 - self.angle

        if (self.border_size < self.dwr.pos()[1] or -self.border_size > self.dwr.pos()[1]) and self.border_y:
            self.border_y = False
            self.angle = 360 - self.angle

        if -self.border_size < self.dwr.pos()[0] < self.border_size or self.dwr.pos()[0] < self.border_size:
            self.border_x = True

        if -self.border_size < self.dwr.pos()[1] < self.border_size or self.dwr.pos()[1] < self.border_size:
            self.border_y = True

        self.dwr.down()

    # Обновление угла наклона головы змеи
    def update(self):
        if self.right:
            self.angle -= self.rotation_speed
        if self.left:
            self.angle += self.rotation_speed

    # Удаление элементов хвоста
    def increase_tial(self, num):
        self.tail_len += num
        self.game_score += num

        for k in range(num):
            self.arr.append(self.arr[-1])

    # Увеличение хвоста
    def remove_tail(self):
        self.arr = self.arr[: 2]
        self.game_score = 0
        self.tail_len = 1
