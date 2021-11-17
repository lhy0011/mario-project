from pico2d import *


class Timer:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 32)
        self.time = 300
        self.isStop = False
        pass

    def update(self):
        #현재시간 받아와서 현재시간 또받은 거 빼기
        pass

    def draw(self):
        if self.isStop == False:
            self.font.draw(870, 560, 'TIME', (255,255,255))
            self.font.draw(880, 530, '%d' % (int(self.time - get_time())), (255,255,255))
        pass

    def stop(self):
        self.isStop = True