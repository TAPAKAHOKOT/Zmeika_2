import turtle as tt
from head import Head
import time
import numpy as np
from apple import Apple
from random import randint as rnd
from sub import Sub

# Создаем лист из цветов от красного к оранжевом
cols = []

x, y = 255, 0
m_x, m_y = 0, 1

for k in range(255 + (255 - 204)):
    x -= m_x
    y += m_y

    if y >= 255:
        y = 255
        m_x = 1
        m_y = 0

    x1 = "%X" % x
    y1 = "%X" % y

    # print(x, y)

    if len(x1) == 1:
        x1 = "0" + x1
    if len(y1) == 1:
        y1 = "0" + y1
    cols.append("#{}{}00".format(x1, y1))

# Отключение автообновления скрина черепашки
tt.tracer(0, 0)
# Настройки скрина черепашки
screen = tt.Screen()
screen.bgcolor("Black")

# Создание пера для границ поля
border = tt.Turtle()
border.speed(0)
border.hideturtle()

# Прорисовка границ поля
border_size = 350

for k in range(3):
    border.up()
    border.goto(-border_size, border_size)
    border.down()

    border.color("#" + "{}0".format(3 - k) * 3)

    border.goto(border_size, border_size)
    border.goto(border_size, -border_size)
    border.goto(-border_size, -border_size)
    border.goto(-border_size, border_size)

    border_size += 10

border_size = 350

# Создание пера для эквалайзера
sub_dwr = tt.Turtle()
sub_dwr.speed(0)
sub_dwr.color("White")
sub_dwr.hideturtle()

# Создание обьекта "голова змеи"
head = Head(border_size, cols)
# Создание обьекта "эквалайзер"
sub = Sub(cols, sub_dwr)
# Запуск эквалайзера
sub.run_callback()

# Реакция на нажатие кнопок


def move_right_start(): head.right = True


def move_right_stop(): head.right = False


def move_left_start(): head.left = True


def move_left_stop(): head.left = False


screen.onkeypress(move_right_start, "Right")
screen.onkeyrelease(move_right_stop, "Right")

screen.onkeypress(move_left_start, "Left")
screen.onkeyrelease(move_left_stop, "Left")

screen.listen()

# Проверка на пересечение яблока и змеи


def ch_clip():
    pos = head.dwr.pos()

    for apple in apples:

        if apple.rect[0][0] < pos[0] < apple.rect[0][1]:
            if apple.rect[1][0] < pos[1] < apple.rect[1][1]:
                apple.dwr.clear()
                apples.remove(apple)

                head.increase_tial(10)


apples = []

# основной цикл
while True:
    # Обновление змеи
    head.draw()
    head.update()

    # обновление эквалайзера
    sub_dwr.clear()
    sub.draw()

    # прорисовка яблок
    if not apples:
        apples.append(Apple([rnd(-300, 300), rnd(-300, 300)]))
        apples[-1].draw()

        # print(head.dwr.pos())
    # чек пересечения яблока и змеи
    if apples:
        ch_clip()

    # обновление экрана
    tt.update()
    time.sleep(0.003)


tt.mainloop()
