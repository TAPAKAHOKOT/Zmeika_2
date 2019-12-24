import turtle as tt


# объект яблоко
class Apple:
    # Инициализация переменных
    def __init__(self, pos):

        self.dwr = tt.Turtle()
        self.dwr.speed(0)
        self.dwr.hideturtle()
        self.dwr.color("white")

        self.rad = 10

        self.pos = pos

        # Создание границ яблока
        self.rect = [
            [
                self.pos[0] - self.rad,
                self.pos[0] + self.rad
            ],
            [
                self.pos[1],
                self.pos[1] + self.rad * 2
            ]
        ]

    # Прорисовка яблока
    def draw(self):
        self.dwr.up()
        self.dwr.goto(self.pos)
        self.dwr.down()

        self.dwr.circle(self.rad)
