import sounddevice as sd
from threading import Thread
import numpy as np
import turtle as tt


# объект эквалайзер
class Sub:
    # инициализация переменных
    def __init__(self, cols, dwr):
        self.dwr = dwr

        self.dwr.left(90)

        self.colors = cols

        self.g = 0
        self.t = 0

    # запуск измерения громкости звука через микрофон
    def run_callback(self):

        duration = 10

        # Функция получения громкости звука
        def audio_callback(indata, frames, time, status):
            volume_norm = np.linalg.norm(indata) * 10

            self.g = int(volume_norm)

        stream = sd.InputStream(callback=audio_callback)

        # функция запуска
        def o():
            with stream:
                sd.sleep(duration**8)

        # запуск отдельного потока для проверки громкости звука
        thre = Thread(target=o)
        thre.start()

    # Прорисовка эквалайзера
    def draw(self):

        num = 31
        st = (num - 1) // 2
        dist = 20
        all_dist = st * dist

        if self.t < self.g:
            self.t += abs(self.g - self.t) / 3
        else:
            self.t -= abs(self.g - self.t) / 3

        for k in range(num):
            self.dwr.up()
            self.dwr.goto(-all_dist + dist * k, -300)
            self.dwr.down()

            try:
                self.dwr.color(
                    self.colors[int(self.t * (st - abs(k - st)) / 4)])
            except:
                self.dwr.color(self.colors[-1])

            self.dwr.fd(self.t * (st - abs(k - st)))
